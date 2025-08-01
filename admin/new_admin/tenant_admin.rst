Tenant Administration
=====================

This section describes administration tasks performed at the tenant level.  A tenant typically represents an organisation or department.  Tenant administrators have full control over their own users, storage and policies but cannot affect other tenants.

Introduction
------------

You can access the tenant administration interface either by signing in as the tenant administrator or by clicking **Manage Tenant** from the cluster administrator’s Tenant Manager.  The tenant dashboard summarises usage and provides links to different sections.

``(Screenshot placeholder: tenant‑dashboard‑overview.png – shows the **Tenant Dashboard** page.  At the top of the page you’ll see summary cards labelled **Users**, **Storage**, **Licences** and **Bandwidth** with usage bars and numbers.  Quick links down the side lead to Team Folders, Users, Groups, Reports and Settings.)``

Tenant Plan
-----------

Under **Tenant Plan** you can view and adjust the user licence count, storage quota and bandwidth limits assigned to this tenant.

``(Screenshot placeholder: tenant‑plan‑settings.png – shows the **Tenant Plan** page.  Sliders allow you to adjust the number of user licences, storage quota and bandwidth allocation for the tenant.  Current values are displayed above each slider.)``

Team Folders
------------

Team folders are shared workspaces similar to network shares.  From the **Team Folders** page you can:

* **Create a new team folder** by clicking **Add New Team Folder** (+).  A wizard allows you to choose the underlying storage: existing tenant storage, local file server shares via server agent, remote file servers or cloud storage (S3, Azure Blob, Wasabi, etc.).
* **Manage an existing team folder** by clicking the **Edit** icon.  Here you can adjust folder information, collaborators, external sharing, access policies, folder permissions and folder settings.

``(Screenshot placeholder: tenant‑teamfolders‑overview.png – shows the **Team Folders** overview.  Existing team folders are listed with their names and storage paths.  A blue **Add New Team Folder** (+) button is located at the top or bottom of the list.)``
``(Screenshot placeholder: tenant‑teamfolder‑create.png – shows the **Add New Team Folder** wizard.  On the first step you choose the underlying storage from options like **Existing Tenant Storage**, **File Servers in LAN**, **Remote File Servers** and **Cloud Storage (S3/Azure/Wasabi)**.)``
``(Screenshot placeholder: tenant‑teamfolder‑settings.png – shows the **Information** tab of a team folder’s settings.  It displays the folder name, description, storage location and options to enable versioning and attachments.)``
``(Screenshot placeholder: tenant‑teamfolder‑collaborators.png – shows the **Collaborators** tab for a team folder.  A table lists users and groups assigned to the folder with their permission levels, and an **Add Collaborator** button allows you to invite new users or groups.)``
``(Screenshot placeholder: tenant‑teamfolder‑external‑sharing.png – shows the **External Sharing** tab of a team folder.  Toggles let you enable or disable external sharing, require login for shared items, allow public links and set expiration policies.)``
``(Screenshot placeholder: tenant‑teamfolder‑permissions.png – shows the **Permissions** tab for a team folder.  A matrix lists users and groups down the rows and permission levels (Read, Write, Full Control) across the columns, with check boxes indicating each assignment.)``

Device Manager
--------------

The **Device Manager** lists devices connected by tenant users (desktops, mobiles and other clients).  You can disable, wipe or rename devices from this page.

``(Screenshot placeholder: tenant‑device‑manager.png – shows the **Device Manager** page.  The table lists devices connected by tenant users with columns for Device Name, User, OS/Client type and Last Access.  Action buttons let you disable, wipe or rename a device.)``

User Management
---------------

Under **Users & Groups** you can manage users, groups and roles:

* **Users** – create regular users or guest accounts, reset passwords and assign roles.
* **Groups** – create groups to simplify assignment of team folder permissions.
* **Roles** – define custom roles with specific rights and assign them to users.

``(Screenshot placeholder: tenant‑user‑management.png – shows the **Users** tab under Users & Groups.  A table lists existing users with columns for Username, Email and Role.  An **Add User** (+) button allows you to create a new user or guest.)``
``(Screenshot placeholder: tenant‑group‑management.png – shows the **Groups** tab.  Groups are listed with their names and member counts, and an **Add Group** button lets you create a new group.)``
``(Screenshot placeholder: tenant‑role‑management.png – shows the **Roles** tab.  Existing roles are listed with their names and descriptions.  A **Create Role** button opens a dialog where you define a new role and assign permissions.)``

Reports
-------

Tenant administrators can run reports scoped to their tenant:

* **Upload Report** – track file uploads over time.
* **Storage Statistics** – view total files, folders and storage by type.
* **Bandwidth Usage** – see upload/download bandwidth and top users.
* **Team Folders** – statistics per team folder.
* **Shared Objects** – list shared files and folders.
* **Audit Trace** – search audit logs for actions within the tenant.
* **File Change Log** – view historical changes to files.
* **Folder Permissions** – report on permissions for each folder.
* **Distributed Locks** – monitor locked files.
* **Pending Purged Folder** – view items scheduled for purge.

``(Screenshot placeholder: tenant‑report‑storage‑statistics.png – shows the tenant‑level **Storage Statistics** report.  It summarises files, folders and storage usage for the tenant and includes pie charts and tables ranking team folders or users by usage.)``
``(Screenshot placeholder: tenant‑report‑upload.png – shows the tenant‑level **Upload Report**.  Graphs depict file uploads over the last month, week, day and hour for this tenant.)``
``(Screenshot placeholder: tenant‑report‑shared‑objects.png – shows the **Shared Objects** report.  A table lists files and folders shared by users in the tenant, including the path, share type and expiry date.)``

Settings
--------

The **Settings** section includes many sub‑pages where you configure integrations, policies and client behaviours:

* **Active Directory** – integrate with local or external Active Directory; configure AD server settings, user provisioning and attribute mapping.
* **Single Sign‑On (SAML Integration)** – configure SAML SSO with your identity provider by supplying IdP metadata and certificates.
* **File Locking** – enable distributed file locking and set conflict resolution policies.
* **Notifications** – configure email notifications for events such as folder changes, sync task failures and upload/download completion.
* **User Account & Security** – manage tenant administrators, user accounts, password policies, access controls, security settings (e.g., allow cluster admin to manage my tenant) and the default home directory.
* **Ransomware Protection** – enable ransomware detection and quarantine settings.
* **Data Leak Protection** – set sharing policies (require login for shared items, disable public links), configure guest user restrictions and enable watermarking.
* **Clients & Applications** – configure client settings (UI features, offline access), web portal settings and native client settings.
* **Folder & Storage** – manage backend storage (connect to file servers, remote file servers or cloud storage), configure retention policies and attach additional storage.
* **Tenant Branding** – customise tenant‑level branding separate from cluster branding (logo, colours, login page image).
* **Background Tasks & Filters** – view background tasks (e.g., indexing) and configure file type filters.

``(Screenshot placeholder: tenant‑settings‑active‑directory.png – shows the **Active Directory** settings page.  Fields let you specify the AD server address, bind account, base DN and attribute mappings, with buttons to synchronise users and groups.)``
``(Screenshot placeholder: tenant‑settings‑file‑locking.png – shows the **File Locking** settings page.  Options enable distributed file locking, set conflict resolution rules and define lock expiration periods.)``
``(Screenshot placeholder: tenant‑settings‑notifications.png – shows the **Notifications** settings page.  You can enable email notifications for folder changes, sync task failures, upload/download completion and other events.)``
``(Screenshot placeholder: tenant‑settings‑user‑account‑security.png – shows the **User Account & Security** page.  Here you manage tenant administrators, configure password policies, set session timeouts, enable two‑factor authentication and control whether the cluster admin can manage your tenant.)``
``(Screenshot placeholder: tenant‑settings‑ransomware‑protection.png – shows the **Ransomware Protection** settings.  Toggles let you enable detection of suspicious activity and quarantine affected files, and you can specify exclusion patterns.)``
``(Screenshot placeholder: tenant‑settings‑data‑leak‑protection.png – shows the **Data Leak Protection** page.  You can require login for shared items, disable public links, control guest user permissions and enable watermarking on shared documents.)``
``(Screenshot placeholder: tenant‑settings‑clients‑applications.png – shows the **Clients & Applications** settings page.  Controls include enabling or disabling client features (e.g., map network drive, sync indicator), setting offline access parameters and configuring web portal options.)``
``(Screenshot placeholder: tenant‑settings‑folder‑storage.png – shows the **Folder & Storage** settings page.  You can connect new storage sources (file server agent, remote file server, cloud storage), set retention policies and manage versioning.)``
``(Screenshot placeholder: tenant‑settings‑branding.png – shows the **Tenant Branding** settings page.  You can upload a custom tenant logo, choose a colour theme and specify a login page background image distinct from the cluster branding.)``

Summary
-------

Tenant administration focuses on managing a single organisation’s users, storage and policies.  Tenant administrators have many of the same capabilities as cluster administrators, but only within their own tenant.  They can create and manage team folders, integrate with Active Directory and SAML SSO, enforce security and data protection policies, and monitor usage through detailed reports.