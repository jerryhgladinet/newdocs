Tenant Administration
=====================

This section describes administration tasks performed at the tenant level.  A tenant typically represents an organisation or department.  Tenant administrators have full control over their own users, storage and policies but cannot affect other tenants.

Introduction
------------

You can access the tenant administration interface either by signing in as the tenant administrator or by clicking **Manage Tenant** from the cluster administrator’s Tenant Manager.  The tenant dashboard summarises usage and provides links to different sections.

``(Screenshot placeholder: tenant‑dashboard‑overview.png – show the tenant dashboard with summary cards for users, storage, licences and quick links.)``

Tenant Plan
-----------

Under **Tenant Plan** you can view and adjust the user licence count, storage quota and bandwidth limits assigned to this tenant.

``(Screenshot placeholder: tenant‑plan‑settings.png – show the tenant plan page with licence and storage sliders.)``

Team Folders
------------

Team folders are shared workspaces similar to network shares.  From the **Team Folders** page you can:

* **Create a new team folder** by clicking **Add New Team Folder** (+).  A wizard allows you to choose the underlying storage: existing tenant storage, local file server shares via server agent, remote file servers or cloud storage (S3, Azure Blob, Wasabi, etc.).
* **Manage an existing team folder** by clicking the **Edit** icon.  Here you can adjust folder information, collaborators, external sharing, access policies, folder permissions and folder settings.

``(Screenshot placeholder: tenant‑teamfolders‑overview.png – show the Team Folders page with a list of team folders and an add (+) button.)``
``(Screenshot placeholder: tenant‑teamfolder‑create.png – show the new team folder wizard with storage options such as Existing Tenant Storage, File Servers in LAN, Remote File Servers and Cloud Storage.)``
``(Screenshot placeholder: tenant‑teamfolder‑settings.png – show an existing team folder’s information tab.)``
``(Screenshot placeholder: tenant‑teamfolder‑collaborators.png – show the Collaborators tab where users and groups are assigned.)``
``(Screenshot placeholder: tenant‑teamfolder‑external‑sharing.png – show the External Sharing settings for a team folder.)``
``(Screenshot placeholder: tenant‑teamfolder‑permissions.png – show the Folder Permissions matrix for a team folder.)``

Device Manager
--------------

The **Device Manager** lists devices connected by tenant users (desktops, mobiles and other clients).  You can disable, wipe or rename devices from this page.

``(Screenshot placeholder: tenant‑device‑manager.png – show the Device Manager table with devices and available actions.)``

User Management
---------------

Under **Users & Groups** you can manage users, groups and roles:

* **Users** – create regular users or guest accounts, reset passwords and assign roles.
* **Groups** – create groups to simplify assignment of team folder permissions.
* **Roles** – define custom roles with specific rights and assign them to users.

``(Screenshot placeholder: tenant‑user‑management.png – show the Users list with an add user button.)``
``(Screenshot placeholder: tenant‑group‑management.png – show the Groups list.)``
``(Screenshot placeholder: tenant‑role‑management.png – show the Roles list and the create role dialog.)``

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

``(Screenshot placeholder: tenant‑report‑storage‑statistics.png – show the Storage Statistics report for the tenant.)``
``(Screenshot placeholder: tenant‑report‑upload.png – show the Upload Report graphs for the tenant.)``
``(Screenshot placeholder: tenant‑report‑shared‑objects.png – show the Shared Objects report listing shared files.)``

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

``(Screenshot placeholder: tenant‑settings‑active‑directory.png – show the Active Directory settings page.)``
``(Screenshot placeholder: tenant‑settings‑file‑locking.png – show the File Locking settings.)``
``(Screenshot placeholder: tenant‑settings‑notifications.png – show the Notifications settings.)``
``(Screenshot placeholder: tenant‑settings‑user‑account‑security.png – show the User Account & Security page.)``
``(Screenshot placeholder: tenant‑settings‑ransomware‑protection.png – show the Ransomware Protection settings.)``
``(Screenshot placeholder: tenant‑settings‑data‑leak‑protection.png – show the Data Leak Protection page.)``
``(Screenshot placeholder: tenant‑settings‑clients‑applications.png – show the Clients & Applications settings.)``
``(Screenshot placeholder: tenant‑settings‑folder‑storage.png – show the Folder & Storage settings.)``
``(Screenshot placeholder: tenant‑settings‑branding.png – show the Tenant Branding settings page.)``

Summary
-------

Tenant administration focuses on managing a single organisation’s users, storage and policies.  Tenant administrators have many of the same capabilities as cluster administrators, but only within their own tenant.  They can create and manage team folders, integrate with Active Directory and SAML SSO, enforce security and data protection policies, and monitor usage through detailed reports.