__author__ = 'baohua'

from tripled.common.log import output
from tripled.common.log import info
from tripled.common.case import Case


class DHCP(Case):
    def __init__(self):
        super(DHCP, self).__init__()

    def run_case(self, stack):
        """Check the service status.

        :param stack: the stack instance
        :returns: True or False
        """
        self.result = True
        super(DHCP, self).run_case(module_name='DHCP')


if __name__ == '__main__':
    DHCP().run()
