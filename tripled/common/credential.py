__author__ = 'baohua'

import os
from oslo.config import cfg


def get_creds():
    """Get the Keystone credentials.

    :param : none
    :returns: a map of credentials or None
    """
    d = {}
    AUTH = cfg.CONF.AUTH
    d['username'] = AUTH.username or os.environ['OS_USERNAME'] or None
    d['password'] = AUTH.password or os.environ['OS_PASSWORD'] or None
    d['tenant_name'] = AUTH.tenant_name or os.environ['OS_TENANT_NAME'] or None
    d['auth_url'] = AUTH.auth_url or os.environ['OS_AUTH_URL'] or None
    if d['username'] and d['password'] and d['tenant_name'] and d['auth_url']:
        return d
    else:
        cfg.CONF('neutron')
        keystone_conf = cfg.CONF.keystone_authtoken
        keystone_auth_url = ('%s://%s:%s/v2.0/' %
                             (keystone_conf.auth_protocol,
                              keystone_conf.auth_host,
                              keystone_conf.auth_port))

        d['username'] = keystone_conf.admin_user
        d['password'] = keystone_conf.admin_tenant_name
        d['tenant_name'] = keystone_conf.admin_password
        d['auth_url'] = keystone_auth_url
        if d['username'] and d['password'] and d['tenant_name'] and d['auth_url']:
            return d
        else:
            return None
