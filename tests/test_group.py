# -*- coding: utf-8 -*-
import mock
import pytest


class TestArtifactoryGroups:

    @pytest.mark.parametrize('mockup_get', ["group/list.json"], indirect=True)
    @mock.patch("requests.get")
    def test_list(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "test_group"

        group_list = artifactory.security.groups.list()
        assert group_list[0].name == expected_value

    @pytest.mark.parametrize('mockup_get', ["group/fetch.json"], indirect=True)
    @mock.patch("requests.get")
    def test_fetch(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "test_group"

        group = artifactory.security.groups.fetch("test_group")
        assert group.name == expected_value

    @pytest.mark.parametrize('mockup_put', ["group/create.txt"], indirect=True)
    @mock.patch("requests.put")
    def test_create(self, http_put,
            artifactory, mockup_put):

        http_put.return_value = mockup_put
        expected_value = ""

        group = artifactory.security.groups.new()
        group.name = "test_group"
        group.description = "group for testing"
        response = group.create()

        assert response == expected_value

    @pytest.mark.parametrize('mockup_put', ["group/update.txt"], indirect=True)
    @pytest.mark.parametrize('mockup_get', ["group/fetch.json"], indirect=True)
    @mock.patch("requests.put")
    @mock.patch("requests.get")
    def test_update(self, http_get, http_put,
            artifactory, mockup_get, mockup_put):

        http_get.return_value = mockup_get
        http_put.return_value = mockup_put
        expected_value = ""

        group = artifactory.security.groups.fetch("test_group")
        group.auto_join = True
        response = group.update()

        assert response == expected_value

    @pytest.mark.parametrize('mockup_delete', ["group/delete.txt"], indirect=True)
    @pytest.mark.parametrize('mockup_get', ["group/fetch.json"], indirect=True)
    @mock.patch("requests.delete")
    @mock.patch("requests.get")
    def test_remove(self, http_get, http_delete,
            artifactory, mockup_get, mockup_delete):

        http_get.return_value = mockup_get
        http_delete.return_value = mockup_delete
        expected_value = "Group 'test_group' has been removed successfully.\n"

        group = artifactory.security.groups.fetch("test_group")
        response = group.remove()

        assert response == expected_value
