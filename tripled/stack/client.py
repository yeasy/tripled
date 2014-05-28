__author__ = 'baohua'

from tripled.common.credential import get_creds


class Client(object):
    def __init__(self, username=None, tenant_name=None, password=None,
                 auth_url=None):
        d = get_creds()
        if d:
            username = username or d['username']
            tenant_name = tenant_name or d['tenant_name']
            password = password or d['password']
