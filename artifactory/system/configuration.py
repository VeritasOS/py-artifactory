# -*- coding: utf-8 -*-
"""
Artifactory system/configuration api
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# std imports
import inspect

# thrid party imports
from lxml import etree

# project imports
from ..http import HTTP
from .. import TEMPLATE_DIR
from .ldap import LDAP


class Configuration(HTTP):
    endpoint = "system/configuration"
    nsmap_name = "artifactory"

    _required = []
    _optional = []

    def __init__(self, api):
        self.api = api
        super(Configuration, self).__init__(self.api)

    def ldap(self):
        system_config = self.get(headers={"Content-Type": "application/xml"})
        return LDAP(self.api,
                system_config=system_config,
                nsmap=self._find_nsmap(system_config))

    def _find_nsmap(self, system_config):

        try:
            return {self.nsmap_name: [nsmap for nsmap in system_config.nsmap.values()
                if "xsd" in nsmap][0]}
        except:
            message = "XML nsmap not found"
            self.log.error(message)
            raise Exception(message)
