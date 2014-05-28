__author__ = 'baohua'

from tripled.common.log import warn, info, output
from tripled.stack.stack import stack
from tripled.common.util import color_str
from tripled.common.case import Case


class UnderlayConnectivity(Case):
    def __init__(self):
        super(UnderlayConnectivity, self).__init__()

    def test_connectivity(self, nodes_src, nodes_dst):
        """Check every pair from the given node list are connected.

        :param node_src, nodes_dst: nodes pairs to check
        :returns: True or False
        """
        for src in nodes_src:
            for dst in nodes_dst:
                if not src.is_reachable(dst):
                    self.fail_msg.append('Node %s cannot reach %s' % (src.ip, dst.ip))
                    warn('node %s cannot reach %s' % (src.ip, dst.ip))
                    return False
        return True

    def run_case(self, stack):
        """Check the underlay connectivity status.

        :param stack: the stack instance
        :returns: True or False
        """
        control_nodes = stack.get_control_nodes()
        network_nodes = stack.get_network_nodes()
        compute_nodes = stack.get_computer_nodes()
        self.result = self.test_connectivity(control_nodes, compute_nodes) and \
                      self.test_connectivity(network_nodes, compute_nodes) and \
                      self.test_connectivity(control_nodes, network_nodes)
        super(UnderlayConnectivity, self).run_case(module_name='Underlay Connectivity')


if __name__ == '__main__':
    UnderlayConnectivity().run()
