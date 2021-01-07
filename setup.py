# -*- coding: utf-8 -*-
# vim:filetype=python:tabstop=4:shiftwidth=4:expandtab:

"""
Installer for Artifactory client
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# std-lib imports
import os
from setuptools import (
        setup,
        find_packages,
        )

def read_md(fname):
    """
    Get long description from README file
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='artifactory',
    version='0.1',
    author='Prathamesh Nevagi',
    description='Artifactory client',
    long_description=read_md('README.md'),

    url='https://github.com/veritasos/py-artifactory',
    download_url='https://github.com/veritasos/py-artifactory.git',

    package_dir = {'artifactory': 'artifactory'},
    packages=find_packages(),
    package_data={
        '': ['README.md'],
        'artifactory': ['templates/*'],
        },
    include_package_data=True,

    install_requires=[
        'Jinja2==2.8',
        'requests==2.20.0',
        'lxml==4.6.2'
    ],
    zip_safe=False,
)
