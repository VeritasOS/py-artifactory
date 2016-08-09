# -*- coding: utf-8 -*-
"""
Artifactory repository multiple replication
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP


class MultipleReplication(HTTP):
    endpoint = "replications/multiple"

    _required = []

    _optional = [
            ("cron_expression", "cronExp", ""),
            ("enable_event_replication", "enableEventReplication", False),
            ("replications", "replications", []),
            ]

    def __init__(self, api):
        super(MultipleReplication, self).__init__(api)

    def _set_replications(self):
        # assign all remote servers
        self.replications = [remote.to_dict()
                for remote in self.replications]

    def create(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.repo_key)
        self._set_replications()
        return self.put(endpoint=endpoint)

    def update(self):
        endpoint = "{0}/{1}".format(self.endpoint, self.repo_key)
        self._set_replications()
        return self.post(endpoint=endpoint)
