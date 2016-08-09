# -*- coding: utf-8 -*-
"""
Artifactory version
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP


class Version(HTTP):
    endpoint = "system/version"

    _required = []

    _optional = [
            ("version", "version", ""),
            ("revision", "revision", ""),
            ("addons", "addons", []),
            ("license", "license", ""),
            ]

    def __init__(self, api):
        super(Version, self).__init__(api)

    def fetch(self):
        return self.get(instance_class=Version)
