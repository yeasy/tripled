# vim: tabstop=4 shiftwidth=4 softtabstop=4
__author__ = 'baohua'

from oslo_config import cfg
from gettext import gettext as _

DEFAULT_CONTROL_NODES = []
DEFAULT_NETWORK_NODES = []
DEFAULT_COMPUTE_NODES = []

stack_opts = [
    cfg.ListOpt('control_nodes',
                default=DEFAULT_CONTROL_NODES,
                help=_("List of control_nodes:<ips>")),
    cfg.ListOpt('network_nodes',
                default=DEFAULT_NETWORK_NODES,
                help=_("List of network_nodes:<ips>")),
    cfg.ListOpt('compute_nodes',
                default=DEFAULT_COMPUTE_NODES,
                help=_("List of compute_nodes:<ips>")),
]
cfg.CONF.register_opts(stack_opts, "STACK")

check_opts = [
    cfg.BoolOpt('glance',
                default=True,
                help=_("Whether to run the checks of glance")),
    cfg.BoolOpt('keystone',
                default=True,
                help=_("Whether to run the checks of keystone")),
    cfg.BoolOpt('system',
                default=True,
                help=_("Whether to run the checks of system")),
    cfg.BoolOpt('neutron',
                default=True,
                help=_("Whether to run the checks of neutron")),
    cfg.BoolOpt('nova',
                default=True,
                help=_("Whether to run the checks of nova")),
]
cfg.CONF.register_opts(check_opts, "CHECK")

log_cli_opts = [
    cfg.StrOpt('log_file',
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
    cfg.StrOpt('msg_format',
               default='%(asctime)s.%(msecs)03d %(process)d %(levelname)s '
                       '%(name)s [-] %(message)s',
               help='format string to use for log messages without context'),
    cfg.StrOpt('level',
               default='info',
               help='default log level'),
]
log_group = cfg.OptGroup(name='LOG', title='Log options')
cfg.CONF.register_cli_opts(log_cli_opts, group=log_group)
cfg.CONF.register_opts(log_opts, group=log_group)

auth_opts = [
    cfg.StrOpt('auth_url',
               default='http://127.0.0.1:5000/v2.0',
               help='authentication url in keystone'),
    cfg.StrOpt('username',
               default='admin',
               help='username in keystone'),
    cfg.StrOpt('password',
               default='admin',
               help='username in keystone'),
    cfg.StrOpt('tenant_name',
               default='admin',
               help='the tenant name to check'),
]
cfg.CONF.register_opts(auth_opts, "AUTH")
