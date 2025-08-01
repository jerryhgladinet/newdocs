Settings
========

The Settings area provides tenant level controls for authentication, security policies,
integrations, notifications and other administrative features. Each setting can be
toggled or configured by administrators. The following subsections describe how to
configure these options in CentreStack.

Active Directory settings
-------------------------

CentreStack can integrate with on‑premises Active Directory or Azure AD to
synchronize users and groups and authenticate against your domain. Under **Active Directory**
settings you can configure a connection to:

* **Local Active Directory** – specify the domain controller’s host name or IP address, port and service
  account credentials. Provide the Base DN for users and groups and choose the authentication method (LDAP or LDAPS).
* **Remote AD Server** – configure a remote domain controller if the CentreStack server is not joined
  to the domain. You can import users and groups from this server on demand.
* **User/Group provisioning** – select which organizational units (OUs) or security groups to import
  and choose whether users are automatically provisioned the first time they log in. Imported groups
  can be mapped to roles within CentreStack.

After the connection is configured, you can import users and groups into Tenant Manager and they will
authenticate against your AD.

Single Sign‑On (SAML Integration)
---------------------------------

CentreStack supports SAML‑based Single Sign‑On with identity providers such as ADFS, Okta and Azure AD.
In the **Single Sign‑On** settings you enter the SAML metadata including the **Identity Provider
SSO URL**, **Entity ID** and **X.509 certificate**. You can also configure attribute mappings to
match the identity provider’s user attributes (e.g. email, displayName) to CentreStack fields.
When enabled, users are redirected to the identity provider for authentication and then returned to
CentreStack.

2‑Step Verification (MFA)
-------------------------

Two‑Step Verification (also known as multi‑factor authentication) adds an extra layer of security
by requiring users to enter a verification code in addition to their password. The MFA settings page
includes options to:

* **Enforce 2‑step verification** on all users, or allow exceptions for Windows/Mac desktop clients or
  mobile clients.
* **Disable 2‑step verification** entirely or exclude guest users from the requirement.
* **Email only** – send verification codes by email instead of SMS.
* **Backup email** – allow users to configure a backup email address for receiving codes.
* **Login control** – set an account lockout threshold and enable progressively longer wait times
  after consecutive invalid logon attempts.
* **Notification** – send an email alert when a user logs in from a new device.
* **Token timeout** – define how long a verification token is valid for native clients, mobile clients and web sessions.
* **Max concurrent devices** – limit the number of devices each user can connect from concurrently.

Ransomware Protection
---------------------

CentreStack includes built‑in ransomware protection that monitors file operations for suspicious
behaviour. Administrators can enable protection and configure thresholds for automatic actions. In the
**Ransomware Protection** settings you can:

* Specify the number of file changes within a time window that triggers the system to disable a device.
* Define **allowed processes** that are permitted to modify files without triggering protection, and
  **blocked processes** that are known ransomware threats.
* Ignore certain file patterns or file name extensions (e.g. `~$` temporary files or `.ldb` locking files)
  to avoid false positives.
* Disable uploading files containing specific strings in their names (e.g. `.encr`).
* Schedule background sync for specific file extensions so these files are uploaded only periodically.

Events captured by ransomware protection can be viewed under the **Ransomware Protection Events** page.

File Locking
------------

Distributed file locking prevents conflicts when multiple users access the same document from different
clients. The **File Locking** settings include:

* **Enable distributed locking** – turn on file locking across Windows, Mac and web clients.
* **Lock file exclusively** – when enabled, users must obtain a lock before editing; others open the file
  in read‑only mode.
* **Read‑only on lock** – automatically open the file in read‑only mode if it is already locked by another user.
* **Delay sync until unlock** – delay synchronization of changes until the file is unlocked to avoid conflict.
* **Auto‑unlock after upload** – automatically release the lock once the edited file is uploaded.
* **Native locking** – enable native file locking for files stored in attached folders to honour NTFS
  locking semantics.
* **Office Web Apps integration** – automatically lock the file when it is opened in Office Web Apps.
* **Hide lock lost messages** – suppress lock lost notifications on the client.
* **Scheduled sync** – define a list of file extensions (e.g. `.mdb`, `.qbw`) that should be synchronized at
  scheduled intervals rather than instantly.
* **Process filters** – specify the list of desktop processes that support native locking (e.g. `winword.exe`,
  `excel.exe`) and processes to exclude.

Data Leak Protection
--------------------

Data Leak Protection (DLP) enforces policies to prevent unauthorised sharing or exfiltration of data.
In the DLP settings you can manage:

* **Client Access Policy** – control whether users can download, print or sync files; restrict access to
  specific networks or devices; and enforce remote wipe on lost devices.
* **Sharing policies** – define rules for external sharing (e.g. require passwords for share links or
  disallow public links).
* **Watermark** – apply watermarks to documents viewed via the web portal to deter screenshots.
* **Shared Objects** – view and manage all externally shared files and folders.
* **DLP Events** – review events that triggered DLP policies and take action.

Notifications
-------------

CentreStack can send email notifications to administrators and users about system events. You can
configure:

* **Daily summary** – receive a daily email summarizing file changes, audit traces and guest user counts.
* **Quota warnings** – notify tenant administrators when storage usage approaches a specified threshold.
* **Sync task failures** – alert administrators when scheduled sync tasks fail.
* **Share notifications** – notify administrators when a member shares a folder or sends a public link.
* **Account lockouts** – email an administrator when a user account is locked due to failed logins.
* **Hide desktop notifications** – suppress file change notifications on Windows and Mac clients.
* **Additional recipients** – specify additional email addresses to receive copies of notifications.

Email Service
-------------

By default CentreStack uses its own mail service to send verification codes and notifications. You can
configure an external SMTP server under **Email Service**. Provide the SMTP server address and port,
choose whether to use SSL/TLS, specify the “from” address and supply authentication credentials (username
and password). CentreStack will then relay all outgoing emails through your SMTP service.

SharePoint Online Integration
-----------------------------

To integrate SharePoint Online as a backend storage provider, enable **SharePoint Online** and supply the
following parameters obtained from your Azure AD application registration:

* **Client ID** – the application (client) ID assigned in Azure AD.
* **Client Secret** – the client secret generated for the application.
* **Tenant ID or name** – your Azure AD tenant identifier.
* **Callback URL** – the URL in CentreStack that Microsoft will call back after authentication. This must match
  the redirect URL configured in Azure AD.

Once configured, SharePoint document libraries can be added as Team Folders.

Clients & Applications
-----------------------

The **Clients & Applications** settings control integrations with external applications and client behaviour.

* **Office 365 Integration** – allow users to open Office documents with Microsoft Office 365 from the web portal.
  You can optionally force documents opened from the Windows desktop client to use Office 365 as well.
* **Default Document Viewer** – choose whether the built‑in document viewer is used for previews or rely on
  native applications.
* **Client settings** – configure options such as offline caching, bandwidth throttling and automatic update policy
  for desktop clients.
* **Web portal** – customise the web portal behaviour, e.g. default landing page, file listing view and session timeout.
* **Native client** – define default drive letter mappings, cache locations and user experience options for the
  Windows and Mac clients.

User Account & Security
-----------------------

Within **User Account & Security** administrators manage user accounts and security policies:

* **Tenant administrators & user management** – create and manage tenant administrators and regular users, reset
  passwords, set storage quotas and disable accounts.
* **Password policy** – define the minimum password length, expiration interval and complexity requirements
  (uppercase, lowercase, digits and special characters).
* **Access control** – restrict sign‑ins to certain IP addresses, networks or time windows; enforce session timeouts.
* **Security options** – enable device approval workflows and control how many devices a user may register.
* **Home directory** – specify a default home directory for new users and optionally allow custom home directories.
* **Azure AD integration** – connect to Azure Active Directory to import users and groups similarly to on‑prem AD.

Folder & Storage
----------------

Folder & Storage settings define how data is stored and retained:

* **Backend storage** – configure file server shares, NAS devices, cloud storage (Amazon S3, Azure Blob, Wasabi, etc.)
  or SharePoint Online as the backend for Team Folders.
* **Retention policy** – set retention periods for deleted items and version history, and configure automatic cleanup.
* **Filters** – define file type filters to exclude temporary files (e.g. `*.tmp`, `*.bak`) or restrict uploads to
  certain extensions.
* **Attached folder** – connect local directories on the server as Team Folders and control whether they inherit
  NTFS permissions.
* **Background tasks** – manage scheduled tasks such as virus scanning, quota enforcement, and scheduled syncs.


Timeouts & Limits
-----------------
The Cluster Settings page provides timeouts and limit settings that apply across the cluster. Administrators can configure:

* **Web session timeout, token expiration and distributed lock idle timeout** – specify in minutes to control how long browser sessions, mobile/desktop tokens and distributed locks remain active.
* **Notification frequency** – how often the server notifies the desktop client of file changes (in seconds).
* **Device limits** – maximum concurrent devices per user and number of days before inactive devices are purged from the system.
* **Search results limit** – maximum number of file search results returned per query.

The figure below shows the **Timeouts & Limits** settings page.

.. image:: settings_timeouts.png
   :alt: Timeouts and limits settings page
   :width: 600px

Languages
---------
Administrators can enable or disable specific language packs and choose a cluster default. Supported languages include Chinese, German, French, Italian and Dutch. The cluster default is used for new tenants; tenants may still set their own language preferences.

Below is the **Languages** settings page.

.. image:: settings_languages.png
   :alt: Languages settings page
   :width: 600px

Branding Options
----------------
This tab provides simple options to hide tutorial videos and enable tenant‑level branding. For full branding customisation see :doc:`branding`.

The screenshot below illustrates the **Branding Options** page.

.. image:: settings_branding.png
   :alt: Branding options settings page
   :width: 600px

Change Log
----------
Configure how many days to retain file change logs and specify an email address and database connection string for cloud monitoring and logging.

.. image:: settings_change_log.png
   :alt: Change log settings page
   :width: 600px

License String
--------------
Enter a license key to unlock user counts and features. After applying a valid key, the page displays the registered user count, licensee and expiration date.

.. image:: settings_license.png
   :alt: License string settings page
   :width: 600px

Anti‑Virus
----------
Select an anti‑virus engine to scan uploaded files. When set to **None** no scanning is performed.

.. image:: settings_antivirus.png
   :alt: Anti‑Virus settings page
   :width: 600px

Application Integrations
------------------------
Enable **Office Web App** or **Zoho Web App** for online editing. Provide the Office Online Server endpoint or Zoho API key, choose whether to allow editing or view‑only access and set the default viewer.

.. image:: settings_app_integrations.png
   :alt: Application Integrations settings page
   :width: 600px

Default Group Policy
--------------------
For details on default security, sharing and retention policies see :doc:`group_policy`.

.. image:: settings_group_policy.png
   :alt: Default group policy settings page
   :width: 600px
