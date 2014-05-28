__author__ = 'baohua'

import pkgutil
import subprocess
from tripled.common.log import warn, debug, info, error


def color_str(color, raw_str):
    """Format a string with color.

    :param color: a color name, can be r, g, b or y
    :param raw_str: the string to be formatted
    :returns: a colorful string
    """
    if color == 'r':
        fore = 31
    elif color == 'g':
        fore = 32
    elif color == 'b':
        fore = 36
    elif color == 'y':
        fore = 33
    else:
        fore = 37
    color = "\x1B[%d;%dm" % (1, fore)
    return "%s%s\x1B[0m" % (color, raw_str)


def get_pkg_modules(pkg_name):
    """Get the modules inside a package

    :param pkg_name: the package name to be processed
    :returns: a list of modules or None
    """
    try:
        modules = []
        cmd = "import %s" % (pkg_name)
        exec (cmd)
        cmd = "modules = [name for _, name, _ in pkgutil.iter_modules(%s.__path__)]" % pkg_name
        exec (cmd)
        return modules
    except ImportError:
        return None


def get_valid_checks():
    """Get the available checks in the system.

    :param :
    :returns: a list of available checks or None
    """
    return get_pkg_modules('tripled.case')


def run_check(name):
    """Run a check inside the stack.

    :param name: the check name, e.g., system or nova
    :returns:
    """
    if name not in get_valid_checks():
        warn(_("The check %s is not registered" % name))
    pkg_name = 'tripled.case.%s' % name
    cases = get_pkg_modules(pkg_name)
    for case in cases:
        cmd = 'sudo python -m %s' % pkg_name + '.' + case
        info("cmd = %s" % cmd)
        result, err = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
        if err:
            error(err)
        print result

if __name__ == "__main__":
    run_check("system")
