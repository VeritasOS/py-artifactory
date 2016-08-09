#### Manage Users


- Create artifactory client

        from artifactory import Artifactory
        artifactory = Artifactory(
                url="http://127.0.0.1:8081",
                username="admin",
                password="password",
                )


- List users

        user_list = artifactory.security.users.list()


- Fetch user

        user = artifactory.security.users.fetch("first.last")


- Create user

        user = artifactory.security.users.new()
        user.name = "first.last"
        user.password = "test"
        user.email = "first.last@testartifactory.com"
        user.groups = ["readers"]
        response = user.create()


- Update user

        user = artifactory.security.users.fetch("first.last")
        user.password = "test"  # password is required to update account details
        user.admin = False
        response = user.update()


- Remove user

        user = artifactory.security.users.fetch("first.name")
        response = user.remove()


- [Required/optional fields](https://www.jfrog.com/confluence/display/RTF/Security+Configuration+JSON)

        print user.required
        print user.optional
