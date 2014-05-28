__author__ = 'baohua'

from subprocess import PIPE, Popen

from tripled.common.constants import NODE_ROLES


class Node(object):
    """
    An instance of the server in the stack.
    """

    def __init__(self, ip, role):
        self.ip = ip
        self.role = NODE_ROLES.get(role, NODE_ROLES['compute'])

    def is_reachable(self, dst):
        """
        Return whether the dst is reachable from the node.
        >>> Node().is_reachable(Node('127.0.0.1'))
        True
        >>> Node().is_reachable(Node('169.254.254.254'))
        False
        """
        cmd = 'ping %s -c 3 -W 2' % dst.ip
        output, error = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True).communicate()
        if not error and output and '0% packet loss' in output:
            return True
        else:
            return False


class Control(Node):
    """
    An instance of the control node in the stack.
    """

    def __init__(self, ip='127.0.0.1'):
        super(Control, self).__init__(ip, role='control')


class Network(Node):
    """
    An instance of the control node in the stack.
    """

    def __init__(self, ip='127.0.0.1'):
        super(Network, self).__init__(ip, role='network')


class Compute(Node):
    """
    An instance of the control node in the stack.
    """

    def __init__(self, ip='127.0.0.1'):
        super(Compute, self).__init__(ip, role='compute')


if __name__ == '__main__':
    import doctest

    doctest.testmod()
