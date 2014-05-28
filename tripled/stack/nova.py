__author__ = 'baohua'

from tripled.common.credential import get_creds
import novaclient.v1_1.client as novaclient
from oslo.config import cfg


class NovaClient(object):
    def __init__(self, username=None, tenant_name=None, password=None,
                 auth_url=None):
        d = get_creds()
        if d:
            username = username or d['username']
            tenant_name = tenant_name or d['tenant_name']
            password = password or d['password']
            auth_url = auth_url or d['auth_url']
        self.client = novaclient.Client(username=username,
                                        api_key=password,
                                        project_id=tenant_name,
                                        auth_url=auth_url)

    def get_servers(self):
        return self.client.servers

    def get_services(self):
        return self.client.services

    def get_images(self):
        return self.client.images


if __name__ == '__main__':
    client = NovaClient()
    for image in client.get_images().list(detailed=True):
        print image.id, image.name, image.status
