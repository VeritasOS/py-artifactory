# -*- coding: utf-8 -*-
import mock
import pytest


class TestArtifactoryPermissions:

    @pytest.mark.parametrize('mockup_get', ["permission/list.json"], indirect=True)
    @mock.patch("requests.get")
    def test_list(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "demo-permissions-dev"

        permission_list = artifactory.security.permissions.list()
        assert permission_list[0].name == expected_value

    @pytest.mark.parametrize('mockup_get', ["permission/fetch.json"], indirect=True)
    @mock.patch("requests.get")
    def test_fetch(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "demo-permissions-dev"

        permission = artifactory.security.permissions.fetch("demo-permission-dev")
        assert permission.name == expected_value

    @pytest.mark.parametrize('mockup_put', ["permission/create.txt"], indirect=True)
    @mock.patch("requests.put")
    def test_create(self, http_put,
            artifactory, mockup_put):

        http_put.return_value = mockup_put
        expected_value = "\n"

        permission = artifactory.security.permissions.new()
        permission.name = "test_permissions"
        permission.repositories = ["test-local-repo"]

        permission_matrix = {
                "users" : {
                    "first.last": ["r","w","m"],
                    },
                "groups" : {
                    "readers" : ["r"]
                    }
                }

        permission.principals = permission_matrix
        response = permission.create()

        assert response == expected_value

    @pytest.mark.parametrize('mockup_put', ["permission/update.txt"], indirect=True)
    @pytest.mark.parametrize('mockup_get', ["permission/fetch.json"], indirect=True)
    @mock.patch("requests.put")
    @mock.patch("requests.get")
    def test_update(self, http_get, http_put,
            artifactory, mockup_get, mockup_put):

        http_get.return_value = mockup_get
        http_put.return_value = mockup_put
        expected_value = ""

        permission = artifactory.security.permissions.fetch("test_permissions")
        permission.repositories = ["test-local-repo", "ANY"]
        response = permission.update()

        assert response == expected_value

    @pytest.mark.parametrize('mockup_delete', ["permission/delete.txt"], indirect=True)
    @pytest.mark.parametrize('mockup_get', ["permission/fetch.json"], indirect=True)
    @mock.patch("requests.delete")
    @mock.patch("requests.get")
    def test_remove(self, http_get, http_delete,
            artifactory, mockup_get, mockup_delete):

        http_get.return_value = mockup_get
        http_delete.return_value = mockup_delete
        expected_value = "Successfully deleted permission Target 'test_permissions'\n"

        permission = artifactory.security.permissions.fetch("test_permissions")
        response = permission.remove()

        assert response == expected_value
