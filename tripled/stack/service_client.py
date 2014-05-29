__author__ = 'baohua'

from tripled.common.credential import get_creds


class ServiceClient(object):
    """
    ServiceClient :client to get service resources.
    """

    def __init__(self, username=None, tenant_name=None, password=None,
                 auth_url=None):
        d = get_creds()
        if d:
            self.username = username or d['username']
            self.tenant_name = tenant_name or d['tenant_name']
            self.password = password or d['password']
            self.auth_url = auth_url or d['auth_url']
        self.client = None
        self.resources = {}  #store the name: attributes of each resource

    def get_res_stat(self):
        """Get a dict of each resources.

        :param:
        :returns: a dict e.g., {'resource_name':[string1, string2, ...]}
        """
        result = {}
        for r in self.resources:
            result[r] = self.get_res_str(*(self.resources[r]), resource_name=r)
        return result

    def get_res_str(self, *args, **kwargs):
        """Get strings

        :param *args: the attributes list of the resource
        :param **kwargs: the options to do list()
        :returns: a list e.g., {'resource1_str', 'resource2_str', ...]}
        """
        if not args:
            return None
        res_name = kwargs.pop('resource_name', None)
        if not res_name:
            return None
        result = []
        for e in eval('self.client.%s' % res_name).list(**kwargs):
            result.append('\t'.join([eval('e.%s' % r) for r in args if r]))
        return result
