# -*- coding: utf-8 -*-
import mock
import pytest


class TestArtifactoryReplications:

    @pytest.mark.parametrize('mockup_get', ["replication/list.json"], indirect=True)
    @mock.patch("requests.get")
    def test_list(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "http://127.0.0.1:8081/artifactory/remote-repo"

        # list replications for provided repository
        replication_list = artifactory.replications.list(
                repo_name="test-repo")

        assert replication_list[0].url == expected_value

    @pytest.mark.parametrize('mockup_get', ["replication/list.json"], indirect=True)
    @mock.patch("requests.get")
    def test_fetch(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "http://127.0.0.1:8081/artifactory/remote-repo"

        replication = artifactory.replications.fetch(
                repo_name="test-repo",
                remote_repo_url="http://127.0.0.1:8081/artifactory/remote-repo",
                )

        assert replication.url == expected_value

    @pytest.mark.parametrize('mockup_put', ["replication/response.txt"], indirect=True)
    @mock.patch("requests.put")
    def test_create(self, http_put,
            artifactory, mockup_put):

        http_put.return_value = mockup_put
        expected_value = ""

        # required
        replication = artifactory.replications.new()
        replication.repo_key = "test-repo"  # repository name
        replication.url = "http://127.0.0.1:8081/artifactory/remote-repo"
        replication.username = "admin"
        replication.password = "password"
        replication.cron_expression = "0 0 12 * * ?"

        # optional/defaults
        replication.socket_timeout = 1500
        replication.enabled = True
        replication.enable_event_replication = False
        replication.sync_deleted_artifacts = False
        replication.sync_artifact_properties = True

        response = replication.create()
        assert response == expected_value

    @pytest.mark.parametrize('mockup_post', ["replication/response.txt"], indirect=True)
    @pytest.mark.parametrize('mockup_get', ["replication/list.json"], indirect=True)
    @mock.patch("requests.post")
    @mock.patch("requests.get")
    def test_update(self, http_get, http_post,
            artifactory, mockup_get, mockup_post):

        http_get.return_value = mockup_get
        http_post.return_value = mockup_post
        expected_value = ""

        replication = artifactory.replications.fetch(
                repo_name="test-repo",
                remote_repo_url="http://127.0.0.1:8081/artifactory/remote-repo",
                )
        replication.sync_deleted_artifacts = True

        response = replication.update()
        assert response == expected_value

    @pytest.mark.parametrize('mockup_delete', ["replication/response.txt"], indirect=True)
    @pytest.mark.parametrize('mockup_get', ["replication/list.json"], indirect=True)
    @mock.patch("requests.delete")
    @mock.patch("requests.get")
    def test_remove(self, http_get, http_delete,
            artifactory, mockup_get, mockup_delete):

        http_get.return_value = mockup_get
        http_delete.return_value = mockup_delete
        expected_value = ""

        replication = artifactory.replications.fetch(
                repo_name="test-repo",
                remote_repo_url="http://127.0.0.1:8081/artifactory/remote-repo",
                )

        response = replication.remove()
        assert response == expected_value


class TestArtifactoryMultipleReplications:

    @pytest.mark.parametrize('mockup_put', ["replication/response.txt"], indirect=True)
    @pytest.mark.parametrize('mockup_get', ["replication/list.json"], indirect=True)
    @mock.patch("requests.put")
    @mock.patch("requests.get")
    def test_create(self, http_get, http_put,
            artifactory, mockup_get, mockup_put):

        http_get.return_value = mockup_get
        http_put.return_value = mockup_put
        expected_value = ""

        # Create new replication
        new_replication = artifactory.replications.new()
        new_replication.repo_key = "test-repo"  # repository name
        new_replication.url = "http://127.0.0.1:8081/artifactory/new-remote-repo"
        new_replication.username = "admin"
        new_replication.password = "password"
        new_replication.cron_expression = "0 0 12 * * ?"

        # Fetch existing replication
        existing_replication = artifactory.replications.fetch(
                repo_name="test-repo",
                remote_repo_url="http://127.0.0.1:8081/artifactory/existing-remote-repo",
                )

        # Create Multiple replications
        multiple_replication = artifactory.replications.multiple()
        multiple_replication.repo_key = "test-repo"
        multiple_replication.cron_expression = "0 0 12 * * ?"
        multiple_replication.enable_event_replication = False

        # assign new replication and an existing replication
        multiple_replication.replications = [new_replication, existing_replication]

        response = multiple_replication.create()
        assert response == expected_value


class TestArtifactoryReplicationsStatus:

    @pytest.mark.parametrize('mockup_get', ["replication/status.json"], indirect=True)
    @mock.patch("requests.get")
    def test_status(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "ok"

        status = artifactory.replications.status(
                repo_name="test-repo")

        assert status.status == expected_value
