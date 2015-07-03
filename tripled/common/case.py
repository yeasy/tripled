__author__ = 'baohua'

from tripled.common.log import warn, info, output
from tripled.stack.stack import stack as the_stack
from tripled.common.util import color_str
import sys


class Case(object):
    """
    A check case.
    """

    def __init__(self, stack=the_stack):
        self.success_msg = []
        self.fail_msg = []
        self.stat_msg = []
        self.result = True

    def run_case(self, **kwargs):
        """Run the case with given options.

        :param module_name: The name of modules, will be shown in the msg
        :returns:
        """
        module_name = kwargs.get('module_name', None)
        if self.result:
            self.success_msg.append('>>>%s PASSED' % module_name or sys.modules[__name__])
        else:
            self.fail_msg.insert(0, '>>>%s FAILED' % module_name or sys.modules[__name__])

    def show_msg(self):
        """Show the success or failed msg.

        :param:
        :returns:
        """
        if self.result and self.success_msg:
            print color_str('g', '\n'.join(self.success_msg))
        elif self.result == False and self.fail_msg:
            print color_str('r', '\n'.join(self.fail_msg))
        if self.stat_msg:
            print color_str('b', '\n'.join(self.stat_msg))

    def run(self, stack=the_stack, **kwargs):
        """Run the case and show it's output msg.

        :param statck: The stack instance
        :returns:
        """
        self.run_case(stack=the_stack, **kwargs)
        self.show_msg()
