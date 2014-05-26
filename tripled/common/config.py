# vim: tabstop=4 shiftwidth=4 softtabstop=4
__author__ = 'baohua'

from oslo.config import cfg
from gettext import gettext as _

DEFAULT_CONTROL_NODES=[]
DEFAULT_NETWORK_NODES=[]
DEFAULT_COMPUTE_NODES=[]

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

check_opts = [
    cfg.BoolOpt('system',
                default=True,
                help=_("Whether to run the check checks of system")),
    cfg.BoolOpt('neutron',
                default=True,
                help=_("Whether to run the check checks of neutron")),
    cfg.BoolOpt('nova',
                default=True,
                help=_("Whether to run the check checks of nova")),
]

cfg.CONF.register_opts(stack_opts, "STACK")
cfg.CONF.register_opts(check_opts, "CHECK")
