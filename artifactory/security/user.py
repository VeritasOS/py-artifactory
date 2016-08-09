# -*- coding: utf-8 -*-
"""
Artifactory users
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP


class Users(HTTP):
    endpoint = "security/users"

    _required = [
            ("name", "name", ""),
            ("uri", "uri", ""),
            ]

    _optional = []

    def list(self):
        return self.get(instance_class=User)

    def fetch(self, name):
        endpoint = "{0}/{1}".format(self.endpoint, name)
        return self.get(endpoint=endpoint, instance_class=User)

    def new(self):
        return User(self.api)


class User(HTTP):
    endpoint = "security/users"

    _required = [
            ("name", "name", ""),
            ("email", "email", ""),
            ]

    _optional = [
            ("uri", "uri", ""),
            ("password", "password", ""),
            ("admin", "admin", False),
            ("profile_updatable", "profileUpdatable", True),
            ("internal_password_disabled", "internal_password_disabled", False),
            ("last_logged_in", "lastLoggedIn", ""),
            ("realm", "realm", ""),
            ("groups", "groups", []),
            ]

    def __init__(self, api):
        super(User, self).__init__(api)

    def create(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.name)
        return self.put(endpoint=endpoint)

    def update(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.name)
        return self.put(endpoint=endpoint)

    def remove(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.name)
        return self.delete(endpoint=endpoint)
