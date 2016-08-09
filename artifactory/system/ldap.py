# -*- coding: utf-8 -*-
"""
Artifactory ldap configuration
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# thrid party imports
from lxml import etree

# project imports
from ..http import HTTP
from .. import TEMPLATE_DIR


class LDAP(HTTP):
    endpoint = "system/configuration"

    # For ldap configuration xml is used for communication
    # so tag name can match the field name and
    # field/tag name is substituted to xml template
    _required = [
            # (field, tag, default)
            ("name", "name", ""),
            ("url", "url", ""),
            ("search_filter", "search_filter", ""),
            ("manager_dn", "manager_dn", ""),
            ("manager_password", "manager_password", ""),
            ("email_attribute", "email_attribute", ""),

            # ldap settings
            ("group_name", "group_name", ""),
            ("group_search_base", "group_search_base", ""),
            ("group_name_attribute", "group_name_attribute", ""),
            ("group_member_attribute", "group_member_attribute", ""),
            ("group_filter", "group_filter", ""),
            ("description_attribute", "description_attribute", ""),
            ]

    _optional = [
            # (field, tag, default)
            ("search_base", "search_base", ""),
            ("enable_ldap_settings", "enable_ldap_settings", True),
            ("enable_subtree_search", "enable_subtree_search", True),
            ("enable_auto_create_user", "enable_auto_create_user", True),

            # ldap group settings
            ("mapping_strategy", "mapping_strategy", "STATIC"),
            ("enable_group_subtree_search", "enable_group_subtree_search", True),
            ]

    def __init__(self, api, system_config=None, nsmap=""):

        if not system_config:
            message = "Existing system configuration xml required."
            self.log.error(message)
            raise Exception(message)

        super(LDAP, self).__init__(api)
        self.system_config = system_config
        self.nsmap = nsmap

    def update(self):
        # Steps:
        # 1 - Get all fields for ldap
        # 2 - Interpolate arguments with ldap settings and ldap group settings templates (xml)
        # 3 - In system_config replace ldap settings and ldap group settings with new templates (xml)

        context = self.to_dict()
        context["nsmap"] = self.nsmap.get("artifactory")
        security_config = self.system_config.find("artifactory:security", namespaces=self.nsmap)

        # Interpolate and replace ldap settings
        ldap_settings_template = TEMPLATE_DIR.get_template("ldap_settings.xml")
        ldap_settings_content = ldap_settings_template.render(context)
        self.log.debug("Configured ldap settings {0}".format(ldap_settings_content))

        new_ldap_settings_element = etree.fromstring(ldap_settings_content)
        old_ldap_settings_element = security_config.find("artifactory:ldapSettings", namespaces=self.nsmap)
        security_config.replace(old_ldap_settings_element, new_ldap_settings_element)
        self.log.debug("Replaced ldap settings")

        # Interpolate and replace ldap group settings
        ldap_group_settings_template = TEMPLATE_DIR.get_template("ldap_group_settings.xml")
        ldap_group_settings_content = ldap_group_settings_template.render(context)
        self.log.debug("Configured ldap group settings {0}".format(ldap_group_settings_content))

        new_ldap_group_settings_element = etree.fromstring(ldap_group_settings_content)
        old_ldap_group_settings_element = security_config.find("artifactory:ldapGroupSettings", namespaces=self.nsmap)
        security_config.replace(old_ldap_group_settings_element, new_ldap_group_settings_element)
        self.log.debug("Replaced ldap group settings")

        data = etree.tostring(self.system_config)
        return self.post(headers={"Content-Type": "application/xml"},
                data=data)
