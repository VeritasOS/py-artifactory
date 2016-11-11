# -*- coding: utf-8 -*-
"""
Artifactory client
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."


# project imports
from .http import Api
from .system import (
        System,
        Version
        )
from .repository import Repository
from .security import Security
from .ldapgroup import LdapGroups
from .replication import Replications
from .search import Search
from .logger import log


class Artifactory(object):

    def __init__(self, url, username, password,
            redirect="artifactory", log=log, *args, **kwargs):
        self.log = log
        self.api = Api(url, username, password,
                redirect=redirect)

    @property
    def system(self):
        self.log.debug("Initializing artifactory system api")
        return System(self.api)

    @property
    def repository(self):
        self.log.debug("Initializing artifactory repository api")
        return Repository(self.api)

    @property
    def security(self):
        self.log.debug("Initializing artifactory security api")
        return Security(self.api)

    @property
    def ldap_groups(self):
        self.log.debug("Initializing artifactory ldap group api")
        return LdapGroups(self.api)

    @property
    def replications(self):
        self.log.debug("Initializing artifactory repository replication api")
        return Replications(self.api)

    def version(self):
        self.log.debug("Initializing artifactory system/version api")
        return Version(self.api).fetch()

    @property
    def search(self):
        self.log.debug("Initializing artifactory search api")
        return Search(self.api)
