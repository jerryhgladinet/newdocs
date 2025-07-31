Cluster Settings
================

The Cluster Settings module provides controls at the cluster level that govern system wide behaviour. These settings differ from tenant‑level settings because they apply to the entire cluster.

Timeouts and Limits
-------------------
- **Web Browser Session Timeout** – number of minutes before a web portal session expires. `0` disables the timeout【368951610685776†screenshot】.
- **Native Client Token Timeout / Mobile Client Token Timeout** – defines how long tokens remain valid for desktop and mobile clients (in days). Use `0` to never expire【368951610685776†screenshot】.
- **Distributed Lock Idle Timeout** – minutes a file lock can remain idle before expiring【368951610685776†screenshot】.
- **Shared file change notification interval** – send change notifications every N minutes; set to `0` to notify immediately【368951610685776†screenshot】.
- **Concurrent device limit** – maximum number of devices per user; `0` means no limit【368951610685776†screenshot】.
- **Device purge** – automatically purge device entries after they have been disconnected for N days【368951610685776†screenshot】.
- **Maximum file search results** – limit the number of results returned by file search【368951610685776†screenshot】.

Languages
---------
Administrators can enable and disable language packs for the web portal and choose a default language for the cluster. Supported languages include simplified and traditional Chinese, German, French, Italian and Dutch【429436530000742†screenshot】.

Branding Options
----------------
Cluster administrators can hide tutorial videos and enable tenant‑level branding at the cluster scope【601177976076060†screenshot】. For details on uploading logos and customizing colours, see :doc:`branding`.

Change Log
----------
- **Keep file change log for N days** – defines the retention period for file change logs【651974268771292†screenshot】.
- **Cloud Monitor email** – specify an address to receive alerts and monitoring messages【651974268771292†screenshot】.
- **Logging DB connection strings** – optionally provide connection strings to write logs to an external database (primary and read‑only replica)【651974268771292†screenshot】.

License String
--------------
Enter a license string obtained from Gladinet to unlock production features. After a valid string is entered, the user count, expiration date and licensee name will appear【181972470491864†screenshot】.

Anti‑Virus
----------
Cluster Settings also allow you to select an anti‑virus engine to scan files uploaded via worker nodes. Set to **None** to disable scanning【175956599893755†screenshot】.

Application Integrations
------------------------
From the “Application Manager” (under the Cluster Dashboard), you can configure server integrations used by all tenants.

- **Microsoft Office Web App** – specify the Office Online Server access point for editing and choose whether documents open in view‑only mode. You can also make Office Web App the default viewer【1156660894236083†screenshot】.
- **Zoho Web App** – supply a Zoho API key and enable it as the default viewer【1156660894236083†screenshot】.

Default Group Policy
--------------------
The “Default Group Policy” defines baseline policies for all tenants. It includes settings for security (e.g., requiring re‑authentication on network change and mandating uploads through worker nodes), sharing (requiring login to access shared links, disabling public links and restricting home directory sharing), file locking, client settings manager, retention policy, ransomware protection and more【744557574147673†screenshot】【201194311463185†screenshot】. See :doc:`group_policy` for full details.
