# -*- coding: utf-8 -*-
"""
Artifactory repository replication status
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP


class Status(HTTP):
    endpoint = "replication"

    _required = []

    _optional = [
            ("status", "status", ""),
            ("last_completed", "lastCompleted", ""),
            ("repositories", "repositories", []),
            ]

    def __init__(self, api):
        super(Status, self).__init__(api)
