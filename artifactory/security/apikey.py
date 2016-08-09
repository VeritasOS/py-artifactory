# -*- coding: utf-8 -*-
"""
Artifactory user api keys
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP


class ApiKeys(HTTP):
    endpoint = "security/apiKey"

    _required = []

    _optional = [
            ("api_key", "apiKey", ""),
            ]

    def fetch(self):
        return self.get(endpoint=self.endpoint,
                instance_class=ApiKey)

    def revoke(self, user=""):
        if user:
            endpoint = "{0}/{1}".format(self.endpoint, user)
        else:
            endpoint = self.endpoint
        return self.delete(endpoint=endpoint)

    def new(self):
        return ApiKey(self.api)


class ApiKey(HTTP):
    endpoint = "security/apiKey"

    _required = []

    _optional = [
            ("api_key", "apiKey", ""),
            ]

    def __init__(self, api):
        super(ApiKey, self).__init__(api)

    def create(self):
        return self.post(endpoint=self.endpoint,
                instance_class=ApiKey)
