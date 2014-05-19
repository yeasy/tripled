__author__ = 'baohua'

from oslo.config import cfg

from tripled.stack.node import Control, Network, Compute

nodes_group = cfg.OptGroup(name='NODES', title='Nodes options')

DEFAULT_CONTROL_IPS = ['127.0.0.1']
DEFAULT_NETWORK_IPS = ['127.0.0.1']
DEFAULT_COMPUTE_IPS = ['127.0.0.1']

nodes_opts = [
    cfg.ListOpt('control_ips', default=DEFAULT_CONTROL_IPS,
                help='List of IP addresses of OpenStack control node(s)'),
    cfg.ListOpt('network_ips', default=DEFAULT_NETWORK_IPS,
                help='List of IP addresses of OpenStack network node(s)'),
    cfg.ListOpt('compute_ips', default=DEFAULT_COMPUTE_IPS,
                help='List of IP addresses of OpenStack compute node(s)'),
    ]

cfg.CONF(project='tripled')
CONF = cfg.CONF
CONF.register_opts(nodes_opts,group=nodes_group)

class Stack(object):
    """
    An instance of the operational stack.
    """

    def __init__(self):
        self.control_nodes = map(lambda x: Control(x), CONF.NODES.control_ips)
        self.network_nodes = map(lambda x: Network(x), CONF.NODES.network_ips)
        self.compute_nodes = map(lambda x: Compute(x), CONF.NODES.compute_ips)
        pass

    def get_control_nodes(self):
        return self.control_nodes

    def get_network_nodes(self):
        return self.network_nodes

    def get_computer_nodes(self):
        return self.compute_nodes

    def get_nodes(self):
        return self.get_control_nodes() + self.get_network_nodes() + self.get_computer_nodes()

stack = Stack()

if __name__ == '__main__':
    s = Stack()
    for n in s.get_nodes():
        print n.ip