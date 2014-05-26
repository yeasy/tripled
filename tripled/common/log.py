__author__ = 'baohua'

import logging
from logging import Logger
from logging.handlers import RotatingFileHandler
from oslo.config import cfg


log_group = cfg.OptGroup(name='Log', title='Log options')

logging_cli_opts = [
    cfg.StrOpt('log-file',
               default='/var/log/tripled.log',
               metavar='PATH',
               deprecated_name='logfile',
               help='(Optional) Name of log file to output to. '
                    'If no default is set, logging will go to stdout.'),
]

log_opts = [
    cfg.BoolOpt('use_stderr',
                default=True,
                help='Log output to standard error'),
    cfg.StrOpt('logging_default_format_string',
               default='%(asctime)s.%(msecs)03d %(process)d %(levelname)s '
                       '%(name)s [-] %(instance)s%(message)s',
               help='format string to use for log messages without context'),
]

CONF = cfg.CONF
CONF.register_opts(log_opts, group=log_group)
CONF.register_cli_opts(logging_cli_opts, group=log_group)

OUTPUT = 25

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'output': OUTPUT,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

LOGLEVELDEFAULT = LEVELS['output']

#default: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGMSGFORMAT = '%(message)s'


class Singleton(type):
    """Singleton pattern from Wikipedia
       See http://en.wikipedia.org/wiki/Singleton_Pattern

       Intended to be used as a __metaclass_ param, as shown for the class
       below."""

    def __init__(cls, name, bases, dict_):
        super(Singleton, cls).__init__(name, bases, dict_)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
            return cls.instance


LOGMSGFORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


class NewLogger(Logger, object):
    __metaclass__ = Singleton

    def __init__(self):

        Logger.__init__(self, "tripled")

        # create console handler
        ch = RotatingFileHandler(CONF.Log.log_file, maxBytes=10 * 1024 * 1024, backupCount=5)
        # create formatter
        formatter = logging.Formatter(LOGMSGFORMAT)
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to lg
        self.addHandler(ch)
        self.set_log_level()

    def set_log_level(self, levelname=None):
        level = LOGLEVELDEFAULT
        if levelname is not None:
            if levelname not in LEVELS:
                raise Exception('unknown levelname seen in set_log_level')
            else:
                level = LEVELS.get(levelname, level)

        self.setLevel(level)
        self.handlers[0].setLevel(level)

    def output(self, msg, *args, **kwargs):
        """Log 'msg % args' with severity 'OUTPUT'.

           To pass exception information, use the keyword argument exc_info
           with a true value, e.g.

           logger.warning("Houston, we have a %s", "cli output", exc_info=1)
        """
        if self.manager.disable >= OUTPUT:
            return
        if self.isEnabledFor(OUTPUT):
            self._log(OUTPUT, msg, args, kwargs)


lg = NewLogger()
info, output, warn, error, debug = (
    lg.info, lg.output, lg.warn, lg.error, lg.debug)

setLogLevel = lg.set_log_level
