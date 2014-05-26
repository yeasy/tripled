__author__ = 'baohua'

import pkgutil
import subprocess
from tripled.common.log import warn
from tripled.common.constants import CHECKS


def get_pkg_modules(pkg_name):
    try:
        modules = []
        cmd = "import %s" % (pkg_name)
        exec (cmd)
        cmd = "modules = [name for _, name, _ in pkgutil.iter_modules(%s.__path__)]" % pkg_name
        exec (cmd)
        return modules
    except ImportError:
        return None


def run_check(name):
    if name not in CHECKS:
        warn(_("The check %s is not registered" % name))
        return
    pkg_name = 'tripled.case.%s' % name
    cases = get_pkg_modules(pkg_name)
    for case in cases:
        cmd = 'python -m %s' % pkg_name + '.' + case
        print cmd
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout.read()
        print result


if __name__ == "__main__":
    run_check("system")
