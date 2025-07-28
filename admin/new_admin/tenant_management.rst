Tenant Management
=================

Tenant Manager is where administrators manage tenants, users, groups, team folders and Active Directory integration. This section explains how to navigate the Tenant Manager and configure each component.

Tenants
-------

A tenant is an isolated workspace for a customer or department. Administrators can create new tenants, assign storage quotas, plan size, and configure policies. The Tenant Dashboard displays metrics such as number of users, team folders and storage usage, and alerts for ransomware protection and data leak protection【647716952080395†screenshot】.

To create a tenant, click **Create Tenant** in the Tenant Manager. Provide a tenant name, specify the tenant administrator’s email, choose a plan (number of users and storage quota), and optionally enable a trial period. You can later edit the tenant to adjust quotas, enable features such as remote wipe, and assign branding and policies.

Users
-----

Users represent individual accounts within a tenant. You can add **native users** (created locally), import users in bulk via CSV, or synchronize users and groups from Active Directory【479535212585225†screenshot】. When adding a native user, specify the user’s email, password, full name and optional display name. Users can be assigned to groups and team folders. You can also set storage quota, two‑factor authentication requirement and password policies per user.

There are three user types:

* **Regular users** – internal members of the organization who consume a license.
* **Guest users** – external collaborators who can access shared files/folders but do not count against license quotas.
* **Tenant administrators** – users with elevated permissions to manage the tenant’s configuration.

Groups
------

Groups are collections of users that simplify permission management. You can create a group and assign multiple users; then grant the group access to Team Folders. Groups imported from Active Directory maintain their original membership and can be mapped to roles within CentreStack.

Team Folders / Shared Workspaces
--------------------------------

Team Folders are shared workspaces that users collaborate on. Administrators can create a Team Folder backed by an existing file server share, a new attached folder on local storage, or cloud storage connectors (e.g. Amazon S3, Azure Blob). When creating a team folder, you define the path to the backend storage, choose whether to inherit NTFS permissions or assign permissions manually, and specify who can access the folder. Team folders appear in users’ mapped drives and web portal for collaboration.

Active Directory Integration
----------------------------

CentreStack integrates with Active Directory to synchronize users and groups. Under **Active Directory** settings you configure:

* **Local Active Directory** – specify the domain controller hostname/IP, port and service account credentials. Define base DN and authentication method (LDAP or LDAPS).
* **AD Server** – optional remote Active Directory server; used when the CentreStack server cannot join the domain directly.
* **User/Group provisioning** – select which OUs or groups to import, enable automatic user provisioning upon first login and map AD security groups to CentreStack roles.

Once connected, you can import users and groups and manage them like native accounts, while authentication happens against your AD.

Licenses and Quotas
-------------------

The Tenant Manager provides information about license usage and storage quotas. Each tenant is allocated a number of user licenses and storage capacity based on the selected plan. Administrators can increase or decrease quotas, allocate additional storage, and see current usage. You can set per‑user quotas and enforce retention policies to control storage consumption. Guest users do not consume licenses but you can limit the number of guest users per tenant.
