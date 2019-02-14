# -*- coding: utf-8 -*-
"""
Artifactory remote repo
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from .repotype import RepositoryType


class Remote(RepositoryType):
    endpoint = "repositories"

    _required = [
            ("key", "key", ""),
            ("rclass", "rclass", "remote"),
            ("package_type", "packageType", ""),
            ("url", "url", ""),
            ]

    _optional = [
            ("username", "username", ""),
            ("password", "password", ""),
            ("description", "description", ""),
            ("notes", "notes", ""),
            ("includes_pattern", "includesPattern", "**/*"),
            ("excludes_pattern", "excludesPattern", ""),
            ("repo_layout_ref", "repoLayoutRef", "simple-default"),
            ("remote_repo_checksum_policy_type", "remoteRepoChecksumPolicyType", "generate-if-absent"),
            ("handle_releases", "handleReleases", True),
            ("handle_snapshots", "handleSnapshots", True),
            ("max_unique_snapshots", "maxUniqueSnapshots", 0),
            ("suppress_pom_consistency_checks", "suppressPomConsistencyChecks", False),
            ("hard_fail", "hardFail", False),
            ("offline", "offline", False),
            ("blacked_out", "blackedOut", False),
            ("store_artifacts_locally", "storeArtifactsLocally", True),
            ("socket_timeout_millis", "socketTimeoutMillis", 15000),
            ("local_address", "localAddress", ""),
            ("retrieval_cache_period_secs", "retrievalCachePeriodSecs", 43200),
            ("failed_retrieval_cache_period_secs", "failedRetrievalCachePeriodSecs", 30),
            ("missed_retrieval_cache_period_secs", "missedRetrievalCachePeriodSecs", 7200),
            ("unused_artifacts_cleanup_enabled", "unusedArtifactsCleanupEnabled", False),
            ("unused_artifacts_cleanup_period_hours", "unusedArtifactsCleanupPeriodHours", 0),
            ("assumed_offline_period_secs", "assumedOfflinePeriodSecs", 300),
            ("fetch_jars_eagerly", "fetchJarsEagerly", False),
            ("fetch_sources_eagerly", "fetchSourcesEagerly", False),
            ("share_configuration", "shareConfiguration", False),
            ("synchronize_properties", "synchronizeProperties", False),
            ("property_sets", "propertySets", []),
            ("allow_any_host_auth", "allowAnyHostAuth", False),
            ("enable_cookie_management", "enableCookieManagement", False),
            ("bower_registry_url", "bowerRegistryUrl", "https://registry.bower.io"),
            ("composer_registry_url", "composerRegistryUrl", "https://packagist.org"),
            ("py_pi_registry_url", "pyPIRegistryUrl", "https://pypi.org"),
            ("vcs_type", "vcsType", "GIT"),
            ("vcs_git_provider", "vcsGitProvider", "GITHUB"),
            ("vcs_git_download_url", "vcsGitDownloadUrl", ""),
            ("bypass_head_request", "bypassHeadRequest", False),
            ("client_tls_certificate", "clientTlsCertificate", ""),
            ("external_dependencies_enabled", "externalDependenciesEnabled", False),
            ("external_dependencies_patterns", "externalDependenciesPatterns", [ "**/*microsoft*/**", "**/*github*/**" ]),
            ("download_redirect", "downloadRedirect", False),
            ("content_synchronisation", "contentSynchronisation", {}),
            ]

    def __init__(self, api):
        super(Remote, self).__init__(api)
