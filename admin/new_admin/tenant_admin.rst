Tenant Administration
=====================

This section describes administration tasks performed at the tenant level.  A tenant typically represents an organisation or department.  Tenant administrators have full control over their own users, storage and policies but cannot affect other tenants.

Introduction
------------

You can access the tenant administration interface either by signing in as the tenant administrator or by clicking **Manage Tenant** from the cluster administrator’s Tenant Manager.  The tenant dashboard summarises usage and provides links to different sections.

.. image:: _static/tenant-scope-per-tenant-dashboard-main-view.png
   :alt: **Tenant Dashboard** page with summary cards for Users, Storage, Licences and Bandwidth and quick links to Team Folders, Users, Groups, Reports and Settings

Tenant Plan
-----------

Under **Tenant Plan** you can view and adjust the user licence count, storage quota and bandwidth limits assigned to this tenant.

.. image:: _static/tenant-admin-main-interface.png
   :alt: **Tenant Plan** page where sliders allow you to adjust user licences, storage quota and bandwidth allocation for the tenant with current values displayed

Team Folders
------------

Team folders are shared workspaces similar to network shares.  From the **Team Folders** page you can:

* **Create a new team folder** by clicking **Add New Team Folder** (+).  A wizard allows you to choose the underlying storage: existing tenant storage, local file server shares via server agent, remote file servers or cloud storage (S3, Azure Blob, Wasabi, etc.).
* **Manage an existing team folder** by clicking the **Edit** icon.  Here you can adjust folder information, collaborators, external sharing, access policies, folder permissions and folder settings.

.. image:: _static/tenant-scope-per-tenant-team-folder-view.png
   :alt: **Team Folders** overview listing existing team folders with their names and storage paths and a blue **Add New Team Folder** (+) button
.. image:: _static/tenant-scope-per-tenant-teamfolder-clicked-add-teamfolder-screen1.png
   :alt: **Add New Team Folder** wizard step where you choose the underlying storage from Existing Tenant Storage, File Servers in LAN, Remote File Servers or Cloud Storage (S3/Azure/Wasabi)
.. image:: _static/tenant-scope-per-tenant-team-folder-permissions-view.png
   :alt: **Information** tab of a team folder’s settings showing the folder name, description, storage location and options to enable versioning and attachments
.. image:: _static/tenant-scope-per-tenant-team-folder-collaborators-view.png
   :alt: **Collaborators** tab of a team folder listing users and groups with their permission levels and an **Add Collaborator** button
.. image:: _static/tenant-scope-per-tenant-team-folder-sharing-view.png
   :alt: **External Sharing** tab of a team folder with toggles to enable or disable external sharing, require login for shared items, allow public links and set expiration policies
.. image:: _static/tenant-scope-per-tenant-team-folder-permissions-view.png
   :alt: **Permissions** tab for a team folder with a matrix listing users and groups and their assigned permission levels (Read, Write, Full Control)

Device Manager
--------------

The **Device Manager** lists devices connected by tenant users (desktops, mobiles and other clients).  You can disable, wipe or rename devices from this page.

.. image:: _static/tenant-scope-per-tenant-device-view.png
   :alt: **Device Manager** page listing devices connected by tenant users with columns for Device Name, User, OS/Client type and Last Access, plus actions to disable, wipe or rename devices

User Management
---------------

Under **Users & Groups** you can manage users, groups and roles:

* **Users** – create regular users or guest accounts, reset passwords and assign roles.
* **Groups** – create groups to simplify assignment of team folder permissions.
* **Roles** – define custom roles with specific rights and assign them to users.

.. image:: _static/tenant-scope-per-tenant-user-view.png
   :alt: **Users** tab under Users & Groups where a table lists existing users with columns for Username, Email and Role and an **Add User** (+) button to create new users or guests
.. image:: _static/tenant-scope-per-tenant-user-view.png
   :alt: **Groups** tab displaying groups with their names and member counts and an **Add Group** button to create new groups
.. image:: _static/tenant-scope-per-tenant-user-view.png
   :alt: **Roles** tab listing existing roles with their names and descriptions and a **Create Role** button to define a new role and assign permissions

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

.. image:: _static/tenant-scope-per-tenant-report-view.png
   :alt: tenant‑level **Storage Statistics** report summarising files, folders and storage usage with pie charts and tables ranking team folders or users by usage
.. image:: _static/tenant-scope-per-tenant-report-view.png
   :alt: tenant‑level **Upload Report** with graphs depicting file uploads over the last month, week, day and hour for this tenant
.. image:: _static/tenant-scope-per-tenant-report-view.png
   :alt: **Shared Objects** report listing files and folders shared by users in the tenant with details such as path, share type and expiry date

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

.. image:: _static/tenant-scope-per-tenant-active-directory-after-enabled-active-directory.png
   :alt: **Active Directory** settings page with fields for server address, bind account, base DN and attribute mappings and buttons to synchronise users and groups
.. image:: _static/tenant-scope-per-tenant-settings-view.png
   :alt: **File Locking** settings page with options to enable distributed file locking, set conflict resolution rules and define lock expiration periods
.. image:: _static/tenant-scope-per-tenant-settings-view.png
   :alt: **Notifications** settings page where you can enable email notifications for folder changes, sync task failures, upload/download completion and other events
.. image:: _static/tenant-scope-per-tenant-settings-view.png
   :alt: **User Account & Security** page for managing tenant administrators, configuring password policies, setting session timeouts, enabling two‑factor authentication and controlling whether the cluster admin can manage your tenant
.. image:: _static/tenant-scope-per-tenant-settings-view.png
   :alt: **Ransomware Protection** settings with toggles to enable detection of suspicious activity, quarantine affected files and specify exclusion patterns
.. image:: _static/tenant-scope-per-tenant-settings-view.png
   :alt: **Data Leak Protection** page where you can require login for shared items, disable public links, control guest user permissions and enable watermarking on shared documents
.. image:: _static/tenant-scope-per-tenant-client-download-view.png
   :alt: **Clients & Applications** settings page with controls to enable or disable client features such as map network drive and sync indicator, set offline access parameters and configure web portal options
.. image:: _static/tenant-scope-per-tenant-settings-view.png
   :alt: **Folder & Storage** settings page where you can connect new storage sources, set retention policies and manage versioning
.. image:: _static/tenant-scope-per-tenant-branding-view.png
   :alt: **Tenant Branding** settings page with options to upload a custom tenant logo, choose a colour theme and specify a login page background image distinct from the cluster branding

Summary
-------

Tenant administration focuses on managing a single organisation’s users, storage and policies.  Tenant administrators have many of the same capabilities as cluster administrators, but only within their own tenant.  They can create and manage team folders, integrate with Active Directory and SAML SSO, enforce security and data protection policies, and monitor usage through detailed reports.