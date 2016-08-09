# -*- coding: utf-8 -*-
import mock
import pytest


class TestArtifactoryRepository:

    @pytest.mark.parametrize('mockup_get', ["repository/list.json"], indirect=True)
    @mock.patch("requests.get")
    def test_list(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "demo-auto-images-releases-dev"

        repos = artifactory.repository.list()
        assert repos[0].key == expected_value

    @pytest.mark.parametrize('mockup_get', ["repository/list_by_type.json"], indirect=True)
    @mock.patch("requests.get")
    def test_list_by_type(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "libs-release"

        repos = artifactory.repository.list(type="virtual")
        assert repos[0].key == expected_value

    @pytest.mark.parametrize('mockup_get', ["repository/fetch.json"], indirect=True)
    @mock.patch("requests.get")
    def test_fetch(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "libs-release"

        repo = artifactory.repository.fetch("libs-release")
        assert repo.key == expected_value

    @pytest.mark.parametrize('mockup_delete', ["repository/delete.txt"], indirect=True)
    @pytest.mark.parametrize('mockup_get', ["repository/fetch.json"], indirect=True)
    @mock.patch("requests.delete")
    @mock.patch("requests.get")
    def test_remove(self, http_get, http_delete,
            artifactory, mockup_get, mockup_delete):

        http_get.return_value = mockup_get
        http_delete.return_value = mockup_delete
        expected_value = 'Repository virtual-repo1 has been removed successfully.\n'

        repo = artifactory.repository.fetch("libs-release")
        response = repo.remove()

        assert response == expected_value

    @pytest.mark.parametrize('mockup_post', ["repository/update.txt"], indirect=True)
    @pytest.mark.parametrize('mockup_get', ["repository/fetch.json"], indirect=True)
    @mock.patch("requests.post")
    @mock.patch("requests.get")
    def test_update(self, http_get, http_post,
            artifactory, mockup_get, mockup_post):

        http_get.return_value = mockup_get
        http_post.return_value = mockup_post
        expected_value = "Repository virtual-repo1 update successfully.\n"

        repo = artifactory.repository.fetch("virtual-repo1")
        repo.description = "Virtual test repo"
        response = repo.update()

        assert response == expected_value

    @pytest.mark.parametrize('mockup_put', ["repository/create_virtual.txt"], indirect=True)
    @mock.patch("requests.put")
    def test_create_virtual(self, http_put,
            artifactory, mockup_put):

        http_put.return_value = mockup_put
        expected_value = "Successfully created repository 'virtual-repo1'\n"

        virtual_repo = artifactory.repository.virtual()
        virtual_repo.key = "virtual-repo1"
        virtual_repo.package_type = "maven"
        virtual_repo.repositories = ["test-repo"]
        response = virtual_repo.create()

        assert response == expected_value

    @pytest.mark.parametrize('mockup_put', ["repository/create_local.txt"], indirect=True)
    @mock.patch("requests.put")
    def test_create_local(self, http_put,
            artifactory, mockup_put):

        http_put.return_value = mockup_put
        expected_value = "Successfully created repository 'test-local-repo'\n"

        local_repo = artifactory.repository.local()
        local_repo.key = "test-local-repo"
        local_repo.package_type = "docker"
        response = local_repo.create()

        assert response == expected_value

    @pytest.mark.parametrize('mockup_put', ["repository/create_remote.txt"], indirect=True)
    @mock.patch("requests.put")
    def test_create_remote(self, http_put,
            artifactory, mockup_put):

        http_put.return_value = mockup_put
        expected_value = "Successfully created repository 'test-remote-repo'\n"

        remote_repo = artifactory.repository.remote()
        remote_repo.key = "test-remote-repo"
        remote_repo.package_type = "docker"
        remote_repo.url = "http://www.docker.com"
        response = remote_repo.create()

        assert response == expected_value
