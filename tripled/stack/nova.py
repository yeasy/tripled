__author__ = 'baohua'

import novaclient.v1_1.client as novaclient
from tripled.stack.service_client import ServiceClient


class NovaClient(ServiceClient):
    """
    NovaClient :client to get nova resources.
    """

    def __init__(self, username=None, tenant_name=None, password=None,
                 auth_url=None):
        super(NovaClient, self).__init__(username, tenant_name, password,
                                         auth_url)
        self.client = novaclient.Client(username=self.username,
                                        api_key=self.password,
                                        project_id=self.tenant_name,
                                        auth_url=self.auth_url)
        self.resources = {'servers': [], 'services': [], 'images': ['id', 'name', 'status']}

    def get_servers(self):
        return self.client.servers

    def get_services(self):
        return self.client.services

    def get_images(self):
        return self.client.images


if __name__ == '__main__':
    client = NovaClient()
    print client.get_res_stat()
