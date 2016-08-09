# -*- coding: utf-8 -*-
"""
Artifactory repository endpoint
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP
from .repotype import RepositoryType
from .virtual import Virtual
from .local import Local
from .remote import Remote

# define all repo types
REPO_TYPE = {
        "local": Local,
        "remote": Remote,
        "virtual": Virtual,
        }


class Repository(HTTP):
    endpoint = "repositories"

    _required = [
            ("key", "key", ""),
            ("type", "type", ""),
            ("url", "url", ""),
            ]

    _optional = [
            ("description", "description", ""),
            ]

    def __init__(self, api):
        self.api = api
        super(Repository, self).__init__(self.api)

    def virtual(self):
        return Virtual(self.api)

    def local(self):
        return Local(self.api)

    def remote(self):
        return Remote(self.api)

    def list(self, type=None):
        """
        Repository types - (local|remote|virtual)
        """
        if type:
            endpoint = "{0}/?type={1}".format(self.endpoint, type)
            return self.get(endpoint=endpoint, instance_class=Repository)
        else:
            return self.get(instance_class=Repository)

    def fetch(self, name=""):
        if not name:
            name = getattr(self, "key", "")

        if not name:
            message = "Repository name is required"
            self.log.error(message)
            raise Exception(message)

        endpoint = "{0}/{1}".format(self.endpoint, name)
        return self.get(endpoint=endpoint, instance_class=RepositoryType)


    def _get_instance(self, data, instance):

        # TODO: this is disgusting hack, need to improve this in future
        if not instance in [RepositoryType]:
            return super(Repository, self)._get_instance(data, instance)
        else:
            self.log.debug("Instance RepositoryType found with type {0}".format(
                data.get("rclass")))

        repo_instance = REPO_TYPE.get(data.get("rclass"))
        if not repo_instance:
            message = "Repository type {0} not supported".format(
                    data.get("rclass"))
            self.log.error(message)
            raise Exception(message)

        self.log.debug("Returning RepositoryType instance {0}".format(
            repo_instance))
        return repo_instance(self.api)
