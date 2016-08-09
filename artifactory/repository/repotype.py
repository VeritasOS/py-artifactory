# -*- coding: utf-8 -*-
"""
Artifactory supported types of repositories
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP


class RepositoryType(HTTP):
    endpoint = "repositories"

    def __init__(self, api):
        super(RepositoryType, self).__init__(api)

    def create(self, pos=1):
        endpoint = "{0}/{1}?pos={2}".format(self.endpoint,
                self.key, pos)
        return self.put(endpoint=endpoint)

    def update(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.key)
        return self.post(endpoint=endpoint)

    def remove(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.key)
        return self.delete(endpoint=endpoint)
