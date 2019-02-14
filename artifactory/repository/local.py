# -*- coding: utf-8 -*-
"""
Artifactory local repo
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from .repotype import RepositoryType


class Local(RepositoryType):
    endpoint = "repositories"

    _required = [
            ("key", "key", ""),
            ("rclass", "rclass", "local"),
            ("package_type", "packageType", ""),
            ]

    _optional = [
            ("description", "description", ""),
            ("notes", "notes", ""),
            ("includes_pattern", "includesPattern", "**/*"),
            ("excludes_pattern", "excludesPattern", ""),
            ("repo_layout_ref", "repoLayoutRef", "simple-default"),
            ("debian_trivial_layout", "debianTrivialLayout", False),
            ("checksum_policy_type", "checksumPolicyType", "client-checksums"),
            ("handle_releases", "handleReleases", True),
            ("handle_snapshots", "handleSnapshots", True),
            ("max_unique_snapshots", "maxUniqueSnapshots", 0),
            ("max_unique_tags", "maxUniqueTags", 0),
            ("snapshot_version_behavior", "snapshotVersionBehavior", "non-unique"),
            ("suppress_pom_consistency_checks", "suppressPomConsistencyChecks", False),
            ("blacked_out", "blackedOut", False),
            ("property_sets", "propertySets", []),
            ("archive_browsing_enabled", "archiveBrowsingEnabled", False),
            ("calculate_yum_metadata", "calculateYumMetadata", False),
            ("yum_root_depth", "yumRootDepth", 0),
            ("docker_api_version", "dockerApiVersion", "V2"),
            ("force_docker_authentication", "forceDockerAuthentication", False),
            ("enable_file_lists_indexing", "enableFileListsIndexing", False),
            ("optional_index_compression_formats", "optionalIndexCompressionFormats", ["bz2"]),
            ("downloa_dredirect", "downloadRedirect", False),
            ]

    def __init__(self, api):
        super(Local, self).__init__(api)
