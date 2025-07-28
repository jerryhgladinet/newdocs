Appendix & Troubleshooting
==========================

This section provides troubleshooting advice, answers to frequently asked questions,
and links to support resources.

Common Issues
-------------

* **Cannot connect to server** – verify network connectivity and ensure DNS resolves to the CentreStack
  server. Check that the CentreStack services (WebPortal, Worker, Database) are running and that
  firewalls allow traffic on HTTP/HTTPS ports. If connecting via a custom domain, confirm the SSL
  certificate is valid.

* **Authentication errors** – ensure the user’s credentials are correct and that the account is not locked.
  For Active Directory integration, check that the server can communicate with the domain controller and
  the base DN and service account credentials are correct. For SAML SSO, verify the IdP metadata
  configuration and certificate. If using 2‑step verification, ensure the user has access to the
  verification email or code.

* **File synchronization problems** – if files are not syncing, confirm that client applications are up
  to date and that the CentreStack server and backend storage are reachable. Check if there are pending
  uploads in the client’s task window and ensure there is sufficient storage quota. In case of network
  disconnects, the client will retry automatically once connectivity is restored.

* **File locking or conflict** – if users cannot edit a document, the file may be locked by another user.
  Use the web portal or client tray menu to view and unlock files if appropriate. Make sure that file
  locking is enabled for the relevant file types and that users are using the latest client. Disable
  conflicting third‑party sync tools that may interfere with locks.

* **Ransomware protection false positives** – review the events in the Ransomware Protection page to see
  which process triggered the alert. Adjust the allowed/blocked process lists or the file change threshold
  as needed, and exclude temporary file patterns to reduce false positives.

* **Client installation issues** – if desktop client installation fails, run the installer as
  administrator and temporarily disable antivirus software. Ensure prerequisites such as Microsoft
  .NET Framework are installed.

FAQs
----

**Q: What is the difference between a cluster administrator and a tenant administrator?**

A cluster administrator manages the entire CentreStack cluster, including creating and deleting tenants,
configuring cluster‑wide settings and licensing. A tenant administrator manages a single tenant’s users,
team folders, quotas and settings but cannot modify other tenants.

**Q: How do I reset a user’s password?**

Cluster or tenant administrators can reset passwords from the **User Account & Security** section. Select
the user, choose **Reset Password**, and a reset link will be emailed to the user. For Active Directory
users, reset the password via AD.

**Q: How do I enable offline access for a team folder?**

Enable offline mode in the Team Folder’s settings. Users can then mark folders as offline in the desktop
client, which caches files locally for access without network connectivity.

**Q: Can I migrate data from an existing file server?**

Yes. Use the Server Agent to connect your on‑prem file server to CentreStack, publish the shares as team
folders and allow users to access them without migration. Alternatively, use a storage connector to
directly connect to cloud storage.

Support Resources
-----------------

Additional resources are available if you need further assistance:

* **Knowledge Base & Documentation** – visit the CentreStack documentation site for guides and best practices.
* **Support portal** – submit support tickets, chat with support engineers and track ticket status.
* **Community forum** – discuss issues and share solutions with other CentreStack administrators.
* **Contact information** – for critical issues, contact Gladinet support via phone or email as listed on the support site.
