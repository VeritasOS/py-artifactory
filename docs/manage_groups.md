#### Manage Groups


- Create artifactory client

        from artifactory import Artifactory
        artifactory = Artifactory(
                url="http://127.0.0.1:8081",
                username="admin",
                password="password",
                )


- List groups

        group_list = artifactory.security.groups.list()


- Fetch groups

        group = artifactory.security.groups.fetch("readers")


- Create group

        group = artifactory.security.groups.new()
        group.name = "test_group"
        group.description = "group for testing"
        response = group.create()


- Update group

        group = artifactory.security.groups.fetch("test_group")
        group.auto_join = True
        response = group.update()


- Remove group

        group = artifactory.security.groups.fetch("test_group")
        response = group.remove()


- [Required/optional fields](https://www.jfrog.com/confluence/display/RTF/Security+Configuration+JSON)

        print group.required
        print group.optional
