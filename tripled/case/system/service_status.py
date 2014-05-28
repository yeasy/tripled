__author__ = 'baohua'

from tripled.stack.stack import stack
from tripled.common.log import info
from tripled.stack.nova import NovaClient
from nova import servicegroup
from nova.cmd.manage import ServiceCommands
from tripled.common.case import Case


class ServiceStatus(Case):
    def __init__(self):
        super(ServiceStatus, self).__init__()

    def run_case(self, stack):
        """Check the service status.

        :param stack: the stack instance
        :returns: True or False
        """
        novaclient = NovaClient()
        novaclient.get_services().list()
        service_command = ServiceCommands()
        service_command.list()
        self.result = True
        super(ServiceStatus, self).run_case()


if __name__ == '__main__':
    ServiceStatus().run()
