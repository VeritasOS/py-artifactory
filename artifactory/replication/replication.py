# -*- coding: utf-8 -*-
"""
Artifactory repository replication
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# stdlib imports
import httplib

# third party imports
import requests

# project imports
from ..http import HTTP
from .multiple import MultipleReplication
from .status import Status


class Replications(HTTP):
    endpoint = "replications"

    _required = []

    _optional = []

    def list(self, repo_name):
        endpoint = "{0}/{1}".format(self.endpoint, repo_name)
        try:
            return self.get(endpoint=endpoint, instance_class=Replication)
        except requests.exceptions.HTTPError as e:
            # NOTE: As artifactory api sends execption instead of
            # empty data structure
            if e.response.status_code != httplib.NOT_FOUND:
                raise
            return []

    def fetch(self, repo_name, remote_repo_url):
        endpoint = "{0}/{1}".format(self.endpoint, repo_name)
        replications = self.get(endpoint=endpoint, instance_class=Replication)

        replication = [rep for rep in replications
                if rep.url == remote_repo_url]

        if not replication:
            message = "Replication url {0} for repository {1} not found".format(
                remote_repo_url, repo_name)
            self.log.error(message)
            raise Exception(message)

        self.log.debug("Found replication url {0} for repository {1}".format(
            remote_repo_url, repo_name))
        return replication[0]

    def new(self):
        return Replication(self.api)

    def multiple(self):
        return MultipleReplication(self.api)

    def purge(self, repo_name):
        endpoint = "{0}/{1}".format(self.endpoint, repo_name)
        return self.delete(endpoint=endpoint)

    def status(self, repo_name):
        endpoint = "{0}/{1}".format(Status.endpoint, repo_name)
        return self.get(endpoint=endpoint, instance_class=Status)


class Replication(HTTP):
    endpoint = "replications"

    _required = [
            ("repo_key", "repoKey", ""),
            ("url", "url", ""),
            ("username", "username", ""),
            ("password", "password", ""),
            ("cron_expression", "cronExp", ""),
            ]

    _optional = [
            ("socket_timeout", "socketTimeoutMillis", 15000),
            ("enable_event_replication", "enableEventReplication", False),
            ("enabled", "enabled", True),
            ("sync_deleted_artifacts", "syncDeletes", False),
            ("sync_artifact_properties", "syncProperties", True),
            ]

    def __init__(self, api):
        super(Replication, self).__init__(api)

    def create(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.repo_key)
        return self.put(endpoint=endpoint)

    def update(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.repo_key)
        return self.post(endpoint=endpoint)

    def remove(self):
        endpoint = "{0}/{1}?url={2}".format(self.endpoint,
                self.repo_key, self.url)
        return self.delete(endpoint=endpoint)
