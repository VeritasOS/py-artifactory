# -*- coding: utf-8 -*-
import mock
import pytest


class TestArtifactoryUsers:

    @pytest.mark.parametrize('mockup_get', ["user/list.json"], indirect=True)
    @mock.patch("requests.get")
    def test_list(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "first.last"

        user_list = artifactory.security.users.list()
        assert user_list[0].name == expected_value

    @pytest.mark.parametrize('mockup_get', ["user/fetch.json"], indirect=True)
    @mock.patch("requests.get")
    def test_fetch(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "first.last"

        user = artifactory.security.users.fetch("first.last")
        assert user.name == expected_value

    @pytest.mark.parametrize('mockup_put', ["user/create.txt"], indirect=True)
    @mock.patch("requests.put")
    def test_create(self, http_put,
            artifactory, mockup_put):

        http_put.return_value = mockup_put
        expected_value = ""

        user = artifactory.security.users.new()
        user.name = "first.last"
        user.password = "test"
        user.email = "first.last@testartifactory.com"
        user.groups = ["readers"]
        response = user.create()

        assert response == expected_value

    @pytest.mark.parametrize('mockup_put', ["user/update.txt"], indirect=True)
    @pytest.mark.parametrize('mockup_get', ["user/fetch.json"], indirect=True)
    @mock.patch("requests.put")
    @mock.patch("requests.get")
    def test_update(self, http_get, http_put,
            artifactory, mockup_get, mockup_put):

        http_get.return_value = mockup_get
        http_put.return_value = mockup_put
        expected_value = ""

        user = artifactory.security.users.fetch("first.last")
        user.password = "test"  # password is required to update account details
        user.admin = False
        response = user.update()

        assert response == expected_value

    @pytest.mark.parametrize('mockup_delete', ["user/delete.txt"], indirect=True)
    @pytest.mark.parametrize('mockup_get', ["user/fetch.json"], indirect=True)
    @mock.patch("requests.delete")
    @mock.patch("requests.get")
    def test_remove(self, http_get, http_delete,
            artifactory, mockup_get, mockup_delete):

        http_get.return_value = mockup_get
        http_delete.return_value = mockup_delete
        expected_value = "User 'first.name' has been removed successfully\n"

        user = artifactory.security.users.fetch("first.name")
        response = user.remove()

        assert response == expected_value
