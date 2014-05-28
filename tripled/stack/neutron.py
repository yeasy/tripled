__author__ = 'baohua'

from tripled.common.credential import get_creds
import neutronclient.v2_0.client as neutronclient


class NeutronClient(object):
    def __init__(self, username=None, tenant_name=None, password=None,
                 auth_url=None):
        d = get_creds()
        if d:
            username = username or d['username']
            tenant_name = tenant_name or d['tenant_name']
            password = password or d['password']
            auth_url = auth_url or d['auth_url']
        self.client = neutronclient.Client(username=username,
                                           password=password,
                                           tenant_name=tenant_name,
                                           auth_url=auth_url)