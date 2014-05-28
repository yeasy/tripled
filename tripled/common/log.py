__author__ = 'baohua'

import logging
from logging import Logger
from logging.handlers import RotatingFileHandler
from oslo.config import cfg
from tripled.common import config  #noqa

OUTPUT = 25

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'output': OUTPUT,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

LOGLEVELDEFAULT = LEVELS.get(cfg.CONF.LOG.logging_default_level, OUTPUT)


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


class NewLogger(Logger, object):
    __metaclass__ = Singleton

    def __init__(self):

        Logger.__init__(self, "tripled")
        # create console handler
        ch = RotatingFileHandler(cfg.CONF.LOG.log_file, maxBytes=10 * 1024 * 1024, backupCount=5)
        # create formatter
        formatter = logging.Formatter(cfg.CONF.LOG.logging_default_format_string)
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
        print msg, args, kwargs
        return
        if self.manager.disable >= OUTPUT:
            return
        if self.isEnabledFor(OUTPUT):
            self._log(OUTPUT, msg, args, kwargs)


lg = NewLogger()
info, output, warn, error, debug = (
    lg.info, lg.output, lg.warn, lg.error, lg.debug)

setLogLevel = lg.set_log_level
