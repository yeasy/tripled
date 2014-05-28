__author__ = 'baohua'

from tripled.common.log import warn, info, output
from tripled.stack.stack import stack as the_stack
from tripled.common.util import color_str
import sys


class Case(object):
    def __init__(self, stack=the_stack):
        self.success_msg = []
        self.fail_msg = []
        self.result = True
        pass

    def run_case(self, **kwargs):
        module_name = kwargs.get('module_name', None)
        if self.result:
            self.success_msg.append('>>>%s PASSED' % module_name or sys.modules[__name__])
        else:
            self.fail_msg.insert(0, '>>>%s FAILED' % module_name or sys.modules[__name__])

    def show_msg(self):
        if self.fail_msg:
            print color_str('r', '\n'.join(self.fail_msg))
        elif self.success_msg:
            print color_str('g', '\n'.join(self.success_msg))
        else:
            print color_str('g', '%s PASSED' % sys.modules[__name__])

    def run(self, stack=the_stack, **kwargs):
        self.run_case(stack=the_stack, **kwargs)
        self.show_msg()
