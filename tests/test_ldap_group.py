# -*- coding: utf-8 -*-
import mock
import pytest


class TestLdapGroups:

    @pytest.mark.parametrize('mockup_post', ["ldap_group/import.json"], indirect=True)
    @mock.patch("requests.post")
    def test_import(self, http_post,
            artifactory, mockup_post):

        http_post.return_value = mockup_post
        expected_value = {u'info': u'Groups successfully imported'}

        ldap_groups = artifactory.ldap_groups.new()
        ldap_groups.group_name = "CompanyGroups"
        ldap_groups.group_list = ["dl-project1", "dl-project2"]
        response = ldap_groups.import_group()

        assert response == expected_value
