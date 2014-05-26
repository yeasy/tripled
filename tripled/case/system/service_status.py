__author__ = 'baohua'

from tripled.stack.stack import stack
from tripled.common.log import info


def service_status(stack):
    control_nodes = stack.get_control_nodes()
    network_nodes = stack.get_network_nodes()
    compute_nodes = stack.get_computer_nodes()


if __name__ == '__main__':
    info('run test case')
    print service_status(stack)
