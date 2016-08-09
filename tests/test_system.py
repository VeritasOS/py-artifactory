# -*- coding: utf-8 -*-
import mock
import pytest


class TestArtifactorySystem:

    @pytest.mark.parametrize('mockup_post', ["ldap/update.txt"], indirect=True)
    @pytest.mark.parametrize('mockup_get', ["ldap/fetch.xml"], indirect=True)
    @mock.patch("requests.post")
    @mock.patch("requests.get")
    def test_ldap(self, http_get, http_post,
            artifactory, mockup_get, mockup_post):

        http_get.return_value = mockup_get
        http_post.return_value = mockup_post
        expected_value = "Reload of new configuration (14 local repos, 4 remote repos, 6 virtual repos) succeeded\n"

        ldap = artifactory.system.configuration.ldap()
        ldap.name="company"
        ldap.url="ldap://ldap-prod.community.company.com:389/DC=community,DC=company,DC=com"
        ldap.search_filter="(&(objectClass=Person)(sAMAccountName={0}))"
        ldap.manager_dn="username"
        ldap.manager_password="password"
        ldap.email_attribute="mail"

        # ldap group settings
        ldap.group_name="companyGroups"
        ldap.group_search_base="OU=Groups"
        ldap.group_name_attribute="cn"
        ldap.group_member_attribute="member:1.2.840.113556.1.4.1941:"
        ldap.group_filter="(objectClass=group)"
        ldap.description_attribute="name"

        response = ldap.update()
        assert expected_value == response


    @pytest.mark.parametrize('mockup_get', ["version.json"], indirect=True)
    @mock.patch("requests.get")
    def test_version(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "4.8.1"

        version = artifactory.version()
        assert version.version == expected_value
