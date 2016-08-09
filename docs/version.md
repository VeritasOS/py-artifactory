#### Artifactory version


- Create artifactory client

        from artifactory import Artifactory
        artifactory = Artifactory(
                url="http://127.0.0.1:8081",
                username="admin",
                password="password",
                )


- Get version details

        version = artifactory.version()

        # version.version
        # version.revision
        # version.addons
        # version.license


- [Required/optional fields](https://www.jfrog.com/confluence/display/RTF/System+Settings+JSON#SystemSettingsJSON-application/vnd.org.jfrog.artifactory.system.Version+json)

        print version.required
        print version.optional
