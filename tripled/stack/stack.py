__author__ = 'baohua'

from oslo.config import cfg

from tripled.stack.node import Control, Network, Compute
from tripled.stack.keystone import KeystoneClient
from tripled.stack.nova import NovaClient
from tripled.stack.neutron import NeutronClient


class Stack(object):
    """
    An instance of the operational stack.
    """

    def __init__(self):
        cfg.CONF(project='tripled')
        CONF = cfg.CONF
        self.control_nodes = map(lambda x: Control(x), CONF.STACK.control_nodes)
        self.network_nodes = map(lambda x: Network(x), CONF.STACK.network_nodes)
        self.compute_nodes = map(lambda x: Compute(x), CONF.STACK.compute_nodes)
        #self.keystone = KeystoneClient()
        #self.nova = NovaClient()
        #self.neutron = NeutronClient()

    def get_control_nodes(self):
        """
        :param
        :return: A list of control node instances generated from the conf file.
        """
        return self.control_nodes

    def get_network_nodes(self):
        """
        :param
        :return: A list of network node instances generated from the conf file.
        """
        return self.network_nodes

    def get_computer_nodes(self):
        """
        :param
        :return: A list of compute node instances generated from the conf file.
        """
        return self.compute_nodes

    def get_nodes(self):
        """
        :param
        :return: A list of all node instances generated from the conf file.
        """
        return self.get_control_nodes() + self.get_network_nodes() + self.get_computer_nodes()


stack = Stack()

if __name__ == '__main__':
    s = Stack()
    for n in s.get_nodes():
        print n.ip
