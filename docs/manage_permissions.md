#### Manage Permissions

- Permission abbreviation

        r=read
        w=deploy
        n=annotate
        d=delete
        m=admin

- Create artifactory client

        from artifactory import Artifactory
        artifactory = Artifactory(
                url="http://127.0.0.1:8081",
                username="admin",
                password="password",
                )


- List permissions

        permission_list = artifactory.security.permissions.list()


- Fetch permission

        permission = artifactory.security.permissions.fetch("demo-permission-dev")


- Create permission

        permission = artifactory.security.permissions.new()
        permission.name = "test_permissions"
        permission.repositories = ["test-local-repo"]

        permission_matrix = {
                "users" : {
                    "first.last": ["r","w","m"],
                    },
                "groups" : {
                    "readers" : ["r"]
                    }
                }

        permission.principals = permission_matrix
        response = permission.create()


- Update permission

        permission = artifactory.security.permissions.fetch("test_permissions")
        permission.repositories = ["test-local-repo", "ANY"]
        response = permission.update()


- Remove permission

        permission = artifactory.security.permissions.fetch("test_permissions")
        response = permission.remove()


- [Required/optional fields](https://www.jfrog.com/confluence/display/RTF/Security+Configuration+JSON)

        print permission.required
        print permission.optional
