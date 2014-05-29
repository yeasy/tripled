__author__ = 'baohua'

from tripled.stack.nova import NovaClient
from tripled.common.case import Case


class ServiceStatus(Case):
    """
    ServiceStatus : the case to get service status.
    """

    def __init__(self):
        super(ServiceStatus, self).__init__()

    def run_case(self, stack):
        """Check the service status.

        :param stack: the stack instance
        :returns: True or False
        """
        nova_client = NovaClient()
        self.result = True
        res_stat = nova_client.get_res_stat()
        self.stat_msg = [e + '\n' + '\n'.join(res_stat[e]) for e in res_stat if res_stat[e]]
        super(ServiceStatus, self).run_case(module_name='Service Status')


if __name__ == '__main__':
    ServiceStatus().run()