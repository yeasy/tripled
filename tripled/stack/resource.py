__author__ = 'baohua'


class Resource(object):
    """
    Resource :
    """

    def __init__(self, name=None, *args, **kwargs):
        self.name = name
        self.attributes = args
        self.options = kwargs

    def __str__(self):
        """Get string to show the resource attributes

        :param:
        :returns: a dict e.g., {'resource_name':[string1, string2, ...]}
        """
        return '\t'.join([eval('e.%s' % r) for r in self.attributes])
