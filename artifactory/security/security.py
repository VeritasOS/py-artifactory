# -*- coding: utf-8 -*-
"""
Artifactory security api
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP
from .permission import Permissions
from .user import Users
from .group import Groups
from .apikey import ApiKeys


class Security(HTTP):
    endpoint = "security"

    _required = []

    _optional = []

    def __init__(self, api):
        self.api = api
        super(Security, self).__init__(self.api)

    @property
    def permissions(self):
        self.log.debug("Initializing artifactory security/permissions api")
        return Permissions(self.api)

    @property
    def users(self):
        self.log.debug("Initializing artifactory security/users api")
        return Users(self.api)

    @property
    def groups(self):
        self.log.debug("Initializing artifactory security/groups api")
        return Groups(self.api)

    @property
    def apikeys(self):
        self.log.debug("Initializing artifactory security/apikey api")
        return ApiKeys(self.api)
