# -*- coding: utf-8 -*-
import mock
import pytest


class TestArtifactoryApiKeys:

    @pytest.mark.parametrize('mockup_get', ["apikey/fetch.json"], indirect=True)
    @mock.patch("requests.get")
    def test_fetch(self, http_get,
            artifactory, mockup_get):

        http_get.return_value = mockup_get
        expected_value = "AKCp2UPB1D6s36jAE6rhQ4p319SmEdqPRe2RKVUuKKvVf9HxETccKMt5SGgY4tKNEAY62bWmM"

        apikey = artifactory.security.apikeys.fetch()
        assert apikey.api_key == expected_value

    @pytest.mark.parametrize('mockup_post', ["apikey/create.json"], indirect=True)
    @mock.patch("requests.post")
    def test_create(self, http_post,
            artifactory, mockup_post):

        http_post.return_value = mockup_post
        expected_value = "AKCp2UPB1D6s36jAE6rhQ4p319SmEdqPRe2RKVUuKKvVf9HxETccKMt5SGgY4tKNEAY62bWmM"

        apikey = artifactory.security.apikeys.new()
        apikey.api_key = "my-key"
        apikey = apikey.create()

        assert apikey.api_key == expected_value

    @pytest.mark.parametrize('mockup_delete', ["apikey/delete.json"], indirect=True)
    @mock.patch("requests.delete")
    def test_revoke(self, http_delete,
            artifactory, mockup_delete):

        http_delete.return_value = mockup_delete
        expected_value = "Api key for user: 'first.last' has been successfully revoked"

        response = artifactory.security.apikeys.revoke("first.last")
        assert response.get("info") == expected_value
