# -*- coding: utf-8 -*-
"""
Artifactory system api
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP
from .configuration import Configuration


class System(HTTP):
    endpoint = "system/"

    def __init__(self, api):
        self.api = api
        super(System, self).__init__(self.api)

    @property
    def configuration(self):
        self.log.debug("Initializing artifactory system/configuration api")
        return Configuration(self.api)
