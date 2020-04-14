### Py-artifactory
Python REST API client for JFrog Artifactory


**Installing stable**

    pip install git+https://github.com/veritasos/py-artifactory.git@<version_number>


**Installing cutting edge**

    pip install git+https://github.com/veritasos/py-artifactory.git


- [**Pre-requisites**](docs/pre_requisites.md)

- [**Usage**](docs/usage.md)
    - [Manage Users](docs/manage_users.md)
    - [Manage Groups](docs/manage_groups.md)
    - [Manage Permissions](docs/manage_permissions.md)
    - [Manage Repositories](docs/manage_repositories.md)
    - [Manage Repository Replication](docs/manage_replication.md)
    - [Manage LDAP](docs/manage_ldap.md)
    - [Manage User Api Keys](docs/manage_apikeys.md)
    - [Get version](docs/version.md)

- [**Development**](docs/development.md)


**Note**

- [Artifactory api](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API) follows camel case but this package follow snake case.
- Example:

        Artifactory rest api field name: handleSnapshots
        Package field name: handle_snapshots

**ToDo**

- Try to cover all [api endpoints provided by artifactory](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API)
- Implement doc strings using [Sphinx](http://www.sphinx-doc.org/en/stable/)
