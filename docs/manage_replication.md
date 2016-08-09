#### Manage Single Replication


- Create artifactory client

        from artifactory import Artifactory
        artifactory = Artifactory(
                url="http://127.0.0.1:8081",
                username="admin",
                password="password",
                )


- List replications for a repository

         replication_list = artifactory.replications.list(
                 repo_name="test-repo")


- Fetch replication for a repository

         replication = artifactory.replications.fetch(
                 repo_name="test-repo",
                 remote_repo_url="http://127.0.0.1:8082/artifactory/remote-repo",
                 )


- Create replication for a repository

         replication = artifactory.replications.new()

         # required
         replication.repo_key = "test-repo"  # repository name
         replication.url = "http://127.0.0.1:8082/artifactory/remote-repo"
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


- Update replication for a repository

         replication = artifactory.replications.fetch(
                 repo_name="test-repo",
                 remote_repo_url="http://127.0.0.1:8082/artifactory/remote-repo",
                 )

         replication.sync_deleted_artifacts = True
         response = replication.update()


- Remove replication for a repository

         replication = artifactory.replications.fetch(
                 repo_name="test-repo",
                 remote_repo_url="http://127.0.0.1:8082/artifactory/remote-repo",
                 )

         response = replication.remove()


- [Required/optional fields](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetRepositoryReplicationConfiguration)

        print replication.required
        print replication.optional



#### Manage Multiple Replications


- Create/Update multiple replications for a repository

        # Create new replication
        new_replication = artifactory.replications.new()
        new_replication.repo_key = "test-repo"  # repository name
        new_replication.url = "http://127.0.0.1:8082/artifactory/new-remote-repo"
        new_replication.username = "admin"
        new_replication.password = "password"
        new_replication.cron_expression = "0 0 12 * * ?"

        # Fetch existing replication
        existing_replication = artifactory.replications.fetch(
                repo_name="test-repo",
                remote_repo_url="http://127.0.0.1:8083/artifactory/existing-remote-repo",
                )

        # Create Multiple replications
        multiple_replication = artifactory.replications.multiple()
        multiple_replication.repo_key = "test-repo"
        multiple_replication.cron_expression = "0 0 12 * * ?"
        multiple_replication.enable_event_replication = False

        # assign new replication and an existing replication
        multiple_replication.replications = [new_replication, existing_replication]

        # create multiple replications
        response = multiple_replication.create()

        # update multiple replications
        response = multiple_replication.update()


- Delete multiple replications for a repository

        response = artifactory.replications.purge(
                    repo_name="test-repo")


- [Required/optional fields](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplaceLocalMulti-pushReplication)

        print replication.required
        print replication.optional



#### Scheduled Replication Status


- Get replication status

        status = artifactory.replications.status(
                repo_name="test-repo")

        # print
        >>> status.status
            u'ok'

        >>> status.last_completed
            u'2016-07-28T10:00:00.478Z'

        >>> status.repositories
            {u'remote-repo': {u'status': u'ok', u'lastCompleted': u'2016-07-28T12:00:04.186Z'}}


- [Required/optional fields](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ScheduledReplicationStatus)

        print status.required
        print status.optional
