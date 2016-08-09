#### Local, Remote, Virtual Repositories

- Create artifactory client

        from artifactory import Artifactory
        artifactory = Artifactory(
                url="http://127.0.0.1:8081",
                username="admin",
                password="password",
                )


- List of repositories

        repo_list = artifactory.repository.list()

        # list of repositories by type
        repo_list = artifactory.repository.list(type="virtual")


- Fetch a repository

        repo = artifactory.repository.fetch("libs-release")


- Create local repository

        local_repo = artifactory.repository.local()
        local_repo.key = "test-local-repo"
        local_repo.package_type = "docker"
        local_repo.create()


- Create remote repository

        remote_repo = artifactory.repository.remote()
        remote_repo.key = "test-remote-repo"
        remote_repo.package_type = "docker"
        remote_repo.url = "http://hub.docker.com"
        remote_repo.create()


- Create virtual repository

        virtual_repo = artifactory.repository.virtual()
        virtual_repo.key = "virtual-repo1"
        virtual_repo.package_type = "maven"
        virtual_repo.repositories = ["test-repo"]
        virtual_repo.create()


- Update local/remote/virtual repositories

        repo = artifactory.repository.fetch("virtual-repo1")
        repo.description = "Virtual test repo"
        response = repo.update()


- Delete local/remote/virtual repositories

        repo = artifactory.repository.fetch("libs-release")
        response = repo.remove()


- [Required/optional fields](https://www.jfrog.com/confluence/display/RTF/Repository+Configuration+JSON)

        print repo.required
        print repo.optional
