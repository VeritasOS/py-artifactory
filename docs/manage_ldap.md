#### Configure LDAP with artifactory

- Create artifactory client

        from artifactory import Artifactory
        artifactory = Artifactory(
                url="http://127.0.0.1:8081",
                username="admin",
                password="password",
                )


- Configure ldap with artifactory

        ldap = artifactory.system.configuration.ldap()

        # ldap settings
        ldap.name="Company"
        ldap.url="ldap://ldap-prod.community.company.com:389/DC=community,DC=company,DC=com"
        ldap.search_filter="(&(objectClass=Person)(sAMAccountName={0}))"
        ldap.manager_dn="username"
        ldap.manager_password="password"
        ldap.email_attribute="mail"

        # ldap group settings
        ldap.group_name="CompanyGroups"
        ldap.group_search_base="OU=Groups"
        ldap.group_name_attribute="cn"
        ldap.group_member_attribute="member:1.2.850.113566.1.4.1931:"
        ldap.group_filter="(objectClass=group)"
        ldap.description_attribute="name"

        ldap.update()


- Import distribution list as artifactory groups

        ldap_groups = artifactory.ldap_groups.new()
        ldap_groups.group_name = "CompanyGroups"
        ldap_groups.group_list = ["dl-project1", "dl-project2"]
        response = ldap_groups.import_group()
