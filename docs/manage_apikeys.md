#### Manage User Api Keys


- Create artifactory client

        from artifactory import Artifactory
        artifactory = Artifactory(
                url="http://127.0.0.1:8081",
                username="admin",
                password="password",
                )


- Fetch api key for logged in user

        apikey = artifactory.security.apikeys.fetch()


- Create api key for logged in user

        apikey = artifactory.security.apikeys.new()
        apikey.api_key = "my-key"
        apikey = apikey.create()


- Revoke api key for logged in user

        response = artifactory.security.apikeys.revoke()


- Revoke api key for other users (admin only)

        response = artifactory.security.apikeys.revoke("first.last")


- [Required/optional fields](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetAPIKey)

        print apikey.required
        print apikey.optional
