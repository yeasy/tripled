__author__ = 'baohua'

from oslo.config import cfg
from tripled.common import config  #noqa
from tripled.common.log import error
from tripled.common.credential import get_creds
import keystoneclient.v2_0.client as ksclient


class KeystoneClient(object):
    """
    KeystoneClient: client to get keystone resources.
    """

    def __init__(self, username=None, tenant_name=None, password=None,
                 auth_url=None):
        d = get_creds()
        if d:
            username = username or d['username']
            tenant_name = tenant_name or d['tenant_name']
            password = password or d['password']
            auth_url = auth_url or d['auth_url']
        self.client = ksclient.Client(username=username,
                                      password=password,
                                      tenant_name=tenant_name,
                                      auth_url=auth_url)

    def get_tenant_by_id(self, id):
        try:
            return self.client.tenants.get(id)
        except Exception:
            error(_("Did not find tenant: %r"), id)
        return 'not found'

    def get_tenant_name_by_id(self, id):
        tenant = self.get_tenant_by_id(id)
        if tenant:
            return tenant.name

    def get_tokens(self):
        return self.client.tokens

    def get_endpoints(self):
        return self.client.endpoints

    def get_roles(self):
        return self.client.roles

    def get_services(self):
        return self.client.services

    def get_tenants(self):
        return self.client.tenants

    def get_users(self):
        return self.client.users
