Default Group Policy
====================

The Default Group Policy defines baseline policies that apply to all tenants in the cluster. It contains multiple categories of settings that can be customised by the cluster administrator.

Security
--------
Security settings control authentication and session behaviour for all users. For example, administrators can:
- Notify users when their email address is changed, alerting them to potential account changes【744557574147673†screenshot】.
- Force users to re‑authenticate when their client IP/network changes (e.g., moving from office to home), ensuring sessions aren’t hijacked【744557574147673†screenshot】.
- Allow users to log in with Google Apps (if the tenant is connected to a Google Workspace domain)【744557574147673†screenshot】.
- Impersonate a tenant administrator when a cluster administrator logs in as a delegate admin【744557574147673†screenshot】.
- Require that uploads/downloads be proxied through worker nodes to enforce network security policies【744557574147673†screenshot】.

Sharing
-------
Sharing policies govern how users can share content:
- Require login for recipients to view files shared with them【201194311463185†screenshot】.
- Disable external sharing of home directories or restrict public links【201194311463185†screenshot】.
- Enable internal share URLs (links that only work for users within the cluster) and disable public share links【201194311463185†screenshot】.
- Show or hide the user and guest lists in the share dialogue【201194311463185†screenshot】.
- Allow or prevent guests from creating their own accounts when visiting share links.

File Locking & Collision
------------------------
Policies in this category determine how file locking and version conflict resolution work. Administrators can require users to lock files before editing (to prevent simultaneous changes), automatically lock files opened by Microsoft Office, and configure conflict resolution behaviour when multiple edits occur.

Client Settings Manager
-----------------------
The Client Settings Manager category controls client‑side behaviours such as whether to automatically launch the desktop client at startup, display overlay icons, or enforce bandwidth limits on uploads and downloads.

Retention Policy & Ransomware Protection
----------------------------------------
These settings define how long deleted items and file versions are retained and enable ransomware protection. Administrators can set a number of days to keep deleted items and old versions, automatically quarantine suspicious file activities, and specify whether end‑users can restore data from snapshots.

Accounts & Login
----------------
Options here include disabling new account registration, enabling two‑step verification for all users, forcing password complexity requirements and password expiration, and controlling session lifetimes.

Folder & Storage
----------------
This section governs storage limits and folder behaviours, such as maximum allowed file size, whether to allow direct folder uploads, and whether to store version history.

Client Control
--------------
Client control policies allow administrators to restrict client capabilities, for example disabling offline access, blocking printing or file download, or preventing clipboard copy operations from the desktop or mobile clients.

These baseline policies can be customised per tenant, but the default group policy provides a secure starting point for all tenants. Refer to the cluster’s Group Policy page for the full set of options.
