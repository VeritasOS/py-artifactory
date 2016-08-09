# -*- coding: utf-8 -*-
"""
Artifactory security permission
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP


class Permissions(HTTP):
    endpoint = "security/permissions"

    _required = [
            ("name", "name", ""),
            ("uri", "uri", ""),
            ]

    _optional = []

    def list(self):
        return self.get(instance_class=Permission)

    def fetch(self, name):
        endpoint = "{0}/{1}".format(self.endpoint, name)
        return self.get(endpoint=endpoint, instance_class=Permission)

    def new(self):
        return Permission(self.api)


class Permission(HTTP):
    endpoint = "security/permissions"

    _required = [
            ("name", "name", ""),
            ("repositories", "repositories", []),
            ]

    _optional = [
            ("uri", "uri", ""),
            ("includes_pattern", "includesPattern", "**/*"),
            ("excludes_pattern", "excludesPattern", ""),
            ("principals", "principals", {}),
            ]

    def __init__(self, api):
        super(Permission, self).__init__(api)

    def create(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.name)
        return self.put(endpoint=endpoint)

    def update(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.name)
        return self.put(endpoint=endpoint)

    def remove(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.name)
        return self.delete(endpoint=endpoint)
