__author__ = 'baohua'

from tripled.common.log import warn, info
from tripled.stack.stack import stack

def test_connectivity(nodes_src, nodes_dst):
    """
    Test every pair from the given node list are connected.
    """
    for src in nodes_src:
        for dst in nodes_dst:
            if not src.is_reachable(dst):
                warn('node %s cannot reach %s' % (src.ip, dst.ip))
                return False
    return True

def underlay_connectivity(stack):
    control_nodes = stack.get_control_nodes()
    network_nodes = stack.get_network_nodes()
    compute_nodes = stack.get_computer_nodes()
    print "test_connectivity", control_nodes, network_nodes, compute_nodes
    return test_connectivity(control_nodes, compute_nodes) and \
           test_connectivity(network_nodes, compute_nodes) and \
           test_connectivity(control_nodes, network_nodes)

if __name__ == '__main__':
    info('run test case')
    for n in stack.get_nodes():
        print n.ip
    print underlay_connectivity(stack)
