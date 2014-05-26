#!/usr/bin/env python

"""Setuptools params"""

from setuptools import setup, find_packages
from os.path import join

# Get version number from source tree
import sys

sys.path.append('.')
from tripled.common.constants import VERSION

scripts = [join('bin', filename) for filename in ['tripled']]

modname = distname = 'tripled'

setup(
    name=distname,
    version=VERSION,
    url='https://github.com/yeasy/tripled',
    description='Smart tool to detect, diagnose and debug OpenStack Cloud environment',
    author='Baohua Yang',
    author_email='yangbaohua@gmail.com',
    #packages=['tripled'],
    packages=find_packages(),
    long_description="""
        TripleD provides automatic analysis in a OpenStack Cloud environment,
        and find potential configuration errors or system problem. It will be useful
        when your OpenStack does not behavior normally or efficiently.
        See https://github.com/yeasy/tripled
        """,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience ::  System Administrators",
        "Topic :: System :: Systems Administration",
    ],
    keywords='OpenStack Cloud Diagnosis Debug',
    license='Apache Software License',
    install_requires=[
        'setuptools>=1.0',
        'oslo.config>=1.2',
        'argparse>=1.0',
        'six>=1.5',
    ],
    scripts=scripts,
)
