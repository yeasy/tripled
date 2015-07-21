#!/usr/bin/env bash

# TripleD install script for Ubuntu, Debian, CentOS and Fedora

# Fail on error
set -e

# Fail on unset var usage
set -o nounset

# Get the base project directory
BASE_DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd -P )"
BIN='bin/tripled'

# Set up build directory, which by default is the working directory
#  unless the working directory is a subdirectory,
BUILD_DIR="$(pwd -P)"
case $BUILD_DIR in
  $BASE_DIR/*) BUILD_DIR=$BASE_DIR;; # currect directory is a subdirectory
  *) BUILD_DIR=$BUILD_DIR;;
esac

# Attempt to identify Linux release
DIST=Unknown
RELEASE=Unknown
CODENAME=Unknown
ARCH=`uname -m`
if [ "$ARCH" = "x86_64" ]; then ARCH="amd64"; fi
if [ "$ARCH" = "i686" ]; then ARCH="i386"; fi

test -e /etc/debian_version && DIST="Debian"
grep Ubuntu /etc/lsb-release &> /dev/null && DIST="Ubuntu"
if [ "$DIST" = "Ubuntu" ] || [ "$DIST" = "Debian" ]; then
    install='sudo apt-get -y install'
    remove='sudo apt-get -y remove'
    pkginst='sudo dpkg -i'
    # Prereqs for this script
    if ! which lsb_release &> /dev/null; then
        $install lsb-release > /dev/null
    fi
fi
test -e /etc/fedora-release && DIST="Fedora"
test -e /etc/centos-release && DIST="CentOS"
if [ "$DIST" = "Fedora" -o  "$DIST" = "CentOS" ]; then
    install='sudo yum -y install'
    remove='sudo yum -y erase'
    pkginst='sudo rpm -ivh'
    # Prereqs for this script
    if ! which lsb_release &> /dev/null; then
        $install redhat-lsb-core
    fi
fi
if which lsb_release &> /dev/null; then
    DIST=`lsb_release -is`
    RELEASE=`lsb_release -rs`
    CODENAME=`lsb_release -cs`
fi
echo "Detected Linux distribution: $DIST $RELEASE $CODENAME $ARCH"

if [ "$DIST" = "Ubuntu" -o "$DIST" = "Debian" ]; then
    KERNEL_NAME=`uname -r`
    KERNEL_HEADERS=linux-headers-${KERNEL_NAME}
elif [ "$DIST" = "Fedora" -o  "$DIST" = "CentOS" ]; then
    KERNEL_NAME=`uname -r`
    KERNEL_HEADERS=kernel-headers-${KERNEL_NAME}
else
    echo "Install.sh currently supports Ubuntu, Debian, CentOS and Fedora."
    exit 1
fi

# Install TripleD core
function core {
    echo "Installing TripleD core files"
    chmod a+x ${BIN}
	[ ! -d /etc/tripled ] && mkdir /etc/tripled
    sudo make install
    chmod u+s /usr/local/bin/tripled
}

# Install TripleD deps
function dep {
    echo "Installing TripleD dependencies"
    if [ "$DIST" = "Fedora" -o "$DIST" = "CentOS" ]; then
        $install gcc make  python-setuptools python-pip python-devel help2man \
        openssl-devel libffi-dev pyflakes pylint python-pep8 > /dev/null
    else
        $install gcc make python-setuptools  python-pip python-dev help2man \
        libssl-dev libffi-dev pyflakes pylint pep8 > /dev/null
    fi
}

# Install TripleD developer dependencies
function dev {
    echo "Installing TripleD developer dependencies"
    $install doxygen doxypy
}

function all {
    echo "Installing the dependencies and the core packages)..."
    dep
    core
    echo "TripleD Installation Done!"
    echo "Enjoy TripleD!"
}

function usage {
    printf '\nUsage: %s [-aehpsu]\n\n' $(basename $0) >&2

    printf 'This install script attempts to install useful packages\n' >&2
    printf 'for TripleD. It should work on Ubuntu 11.10+ or CentOS 6.5+\n' >&2
    printf 'If run into trouble, try installing one thing at a time,\n' >&2
    printf 'and looking at the specific function in this script.\n\n' >&2

    printf 'options:\n' >&2
    printf -- ' -a: (default) install (A)ll packages - good luck!\n' >&2
    printf -- ' -e: install TripleD d(E)veloper dependencies\n' >&2
    printf -- ' -h: print this (H)elp message\n' >&2
    printf -- ' -p: install TripleD de(P)endencies\n' >&2
    printf -- ' -s <dir>: place dependency (S)ource/build trees in <dir>\n' >&2
    printf -- ' -u: (U)pgrade, only install TripleD core files\n' >&2
    exit 2
}

if [ $# -eq 0 ]
then
    all
else
    while getopts 'aehpsu' OPTION
    do
      case $OPTION in
      a)    all;;
      e)    dev;;
      h)    usage;;
      p)    dep;;
      s)    mkdir -p $OPTARG; # ensure the directory is created
            BUILD_DIR="$( cd -P "$OPTARG" && pwd )"; # get the full path
            echo "Dependency installation directory: $BUILD_DIR";;
      u)    core;;
      ?)    usage;;
      esac
    done
    shift $(($OPTIND - 1))
fi
