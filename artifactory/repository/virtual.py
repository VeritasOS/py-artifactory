# -*- coding: utf-8 -*-
"""
Artifactory virtual repo
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from .repotype import RepositoryType


class Virtual(RepositoryType):
    endpoint = "repositories"

    _required = [
            ("key", "key", ""),
            ("rclass", "rclass", "virtual"),
            ("package_type", "packageType", ""),
            ]

    _optional = [
            ("repositories", "repositories", []),
            ("description", "description", ""),
            ("notes", "notes", ""),
            ("includes_pattern", "includesPattern", "**/*"),
            ("excludes_pattern", "excludesPattern", ""),
            ("debian_trivial_layout", "debianTrivialLayout", False),
            ("artifactory_requests_can_retrieve_remote_artifacts", "artifactoryRequestsCanRetrieveRemoteArtifacts", False),
            ("key_pair", "keyPair", ""),
            ("pom_repository_references_cleanup_policy", "pomRepositoryReferencesCleanupPolicy", "discard_active_reference"),
            ("default_deployment_repo", "defaultDeploymentRepo", ""),
            ]

    def __init__(self, api):
        super(Virtual, self).__init__(api)
