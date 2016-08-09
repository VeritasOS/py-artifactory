# -*- coding: utf-8 -*-
"""
Artifactory ldap group settings
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP


class LdapGroups(HTTP):
    endpoint = "ldapgroups"

    _required = [
            ("name", "name", ""),
            ("uri", "uri", ""),
            ]

    _optional = []

    def new(self):
        return LdapGroupImport(self.api)

    # TODO: Implement LdapGroup using new json api
    # def list(self):
    #     return self.get(instance_class=LdapGroup)
    #
    # def fetch(self, name):
    #     endpoint = "{0}/{1}".format(self.endpoint, name)
    #     return self.get(endpoint=endpoint, instance_class=LdapGroup)
    #
    # def new(self):
    #     return LdapGroup(self.api)


# TODO: Implement LdapGroup using new json api
# class LdapGroup(HTTP):
#     endpoint = "ldapgroups"
#
#     _required = [
#             ("name", "name", ""),
#             ("email", "email", ""),
#             ]
#
#     _optional = [
#             ("uri", "uri", ""),
#             ("password", "password", ""),
#             ("admin", "admin", False),
#             ("profile_updatable", "profileUpdatable", True),
#             ("internal_password_disabled", "internal_password_disabled", False),
#             ("last_logged_in", "lastLoggedIn", ""),
#             ("realm", "realm", ""),
#             ("groups", "groups", []),
#             ]
#
#     def __init__(self, api):
#         super(LdapGroup, self).__init__(api)
#
#     def create(self):
#         endpoint = "{0}/{1}".format(self.endpoint, self.name)
#         return self.put(endpoint=endpoint)
#
#     def update(self):
#         endpoint = "{0}/{1}".format(self.endpoint, self.name)
#         return self.put(endpoint=endpoint)
#
#     def remove(self):
#         endpoint = "{0}/{1}".format(self.endpoint, self.name)
#         return self.delete(endpoint=endpoint)


class LdapGroupImport(HTTP):
    endpoint = "ldapgroups"

    _required = [
            ("ldap_group_settings", "ldapGroupSettings", ""),
            ("import_groups", "importGroups", []),
            ]

    _optional = []

    def __init__(self, api):
        super(LdapGroupImport, self).__init__(api)

    def import_group(self):
        self.ldap_group_settings = {"name": self.group_name}
        self.import_groups = [{"groupName": group} for group in self.group_list]
        endpoint = "{0}/{1}/import".format(self.endpoint, self.group_name)
        return self.post(endpoint=endpoint)
