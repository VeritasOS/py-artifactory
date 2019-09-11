# -*- coding: utf-8 -*-
"""
Artifactory groups
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP


class Groups(HTTP):
    endpoint = "security/groups"

    _required = [
            ("name", "name", ""),
            ("uri", "uri", ""),
            ]

    _optional = []

    def list(self):
        return self.get(instance_class=Group)

    def fetch(self, name):
        endpoint = "{0}/{1}".format(self.endpoint, name)
        return self.get(endpoint=endpoint, instance_class=Group)

    def new(self):
        return Group(self.api)


class Group(HTTP):
    endpoint = "security/groups"

    _required = [
            ("name", "name", ""),
            ]

    _optional = [
            ("uri", "uri", ""),
            ("description", "description", ""),
            ("auto_join", "autoJoin", False),
            ("admin_privileges", "adminPrivileges", False),
            ("realm", "realm", ""),
            ("realm_attributes", "realmAttributes", ""),
            ]

    def __init__(self, api):
        super(Group, self).__init__(api)

    def create(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.name)
        return self.put(endpoint=endpoint)

    def update(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.name)
        return self.put(endpoint=endpoint)

    def remove(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.name)
        return self.delete(endpoint=endpoint)
