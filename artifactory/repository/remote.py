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
            ("missed_retrieval_cache_period_secs", "missedRetrievalCachePeriodSecs", 7200),
            ("unused_artifacts_cleanup_period_hours", "unusedArtifactsCleanupPeriodHours", 0),
            ("fetch_jars_eagerly", "fetchJarsEagerly", False),
            ("fetch_sources_eagerly", "fetchSourcesEagerly", False),
            ("share_configuration", "shareConfiguration", False),
            ("synchronize_properties", "synchronizeProperties", False),
            ("property_sets", "propertySets", []),
            ("allow_any_host_auth", "allowAnyHostAuth", False),
            ("enable_cookie_management", "enableCookieManagement", False),
            ("reject_invalid_jars", "rejectInvalidJars", False),
            ("list_remote_folder_items", "listRemoteFolderItems", True),
            ("archive_browsing_enabled", "archiveBrowsingEnabled", False),
            ("assumed_offline_period_secs", "assumedOfflinePeriodSecs", 300),
            ("enable_git_lfs_support", "enableGitLfsSupport", False),
            ("enable_vagrant_support", "enableVagrantSupport", False),
            ("force_nuget_authentication", "forceNugetAuthentication", False),
            ("force_docker_authentication", "forceDockerAuthentication", False),
            ("docker_api_version", "dockerApiVersion", "V2"),
            ("enable_docker_support", "enableDockerSupport", False),
            ("enable_pypi_support", "enablePypiSupport", False),
            ("debian_trivial_layout", "debianTrivialLayout", False),
            ("enable_debian_support", "enableDebianSupport", False),
            ("enable_bower_support", "enableBowerSupport", False),
            ("enable_npm_support", "enableNpmSupport", False),
            ("enable_gems_support", "enableGemsSupport", False),
            ("enable_nuget_support", "enableNuGetSupport", False),
            ("enable_token_authentication", "enableTokenAuthentication", False),
            ]

    def __init__(self, api):
        super(Remote, self).__init__(api)
