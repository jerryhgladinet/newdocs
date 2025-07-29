Getting Started
===============

This section provides an introduction to CentreStack administration, including setup
and initial configuration tasks.

Introduction
------------

Welcome to the CentreStack Administration Guide. CentreStack is a mobile access
and secure file‑sharing solution that focuses on local file server
cloud‑enablement. It runs on Microsoft Windows Server and includes client
agents for Windows, Mac OS X, web browsers and mobile devices (Android and iOS).

.. important::

   CentreStack includes a client application for Windows File Server called
   **Server Agent**. This document covers CentreStack itself and does not cover
   the *Server Agent* component.

.. attention::

   This admin guide is written for CentreStack version 16.6.10352.56511. Future
   releases may introduce new features and changes.

Overview
--------

CentreStack bridges the gap between traditional file servers and modern cloud
workflows. It allows organisations to provide secure remote access to existing
Windows file servers without the cost, complexity or risk of migrating all
data to a public cloud. By combining *on‑demand access*, *drive mapping*,
*file locking* and *real‑time synchronisation*, CentreStack gives remote and
mobile users a native file‑sharing experience while IT retains control over
data residency, permissions and compliance.

Key capabilities include:

* **Hybrid file server mobilisation** – Publish existing Windows file server
  shares as team folders without moving the data; users connect through a
  mapped drive or web portal and see the same folder structure and
  permissions that already exist on the server.
* **Active Directory & NTFS integration** – User accounts and groups are
  synchronised from Active Directory or Azure AD, and NTFS permissions are
  preserved. You can also create native accounts for external collaborators.
* **On‑demand access & caching** – Files are not fully synchronised to the
  client; instead they are fetched on demand. Administrators can enable
  offline caching for selected folders or user devices to allow work without
  an internet connection.
* **Secure collaboration** – Built‑in features include two‑factor
  authentication, SAML single sign‑on, distributed file locking, ransomware
  detection, data leak protection and detailed audit logs.
* **Extensible storage** – Besides file servers, you can attach other
  storage backends such as Azure Blob, Amazon S3 or Wasabi to expand
  capacity or tier data while maintaining a single namespace.

Deployment Scenarios
--------------------

CentreStack is flexible in how it can be deployed. Two common patterns are:

1. **On‑premises server** – Install the CentreStack server in the same local
   network as your file servers and domain controllers. This configuration
   provides the best performance and security because file operations never
   leave the local network. Remote users connect to the server over HTTPS to
   access data.

2. **Cloud or data‑centre server** – Deploy CentreStack in a public cloud
   (such as AWS EC2 or Microsoft Azure) or an MSP’s datacentre. The server
   can connect back to your on‑premises file servers over a secure VPN, or
   you can run the optional *Server Agent* on the file server to bridge the
   connection. This deployment can simplify remote access for distributed
   teams and reduce on‑site hardware.

Whichever deployment you choose, CentreStack offers the same management
interface and feature set. Installation typically takes 15–30 minutes, and
there is a 30‑day trial period before licences must be activated via the
partner portal.

Interface Overview
------------------

After signing in, administrators land on the **Cluster Dashboard**, which
shows the cluster status and provides quick access to common tasks. The
screenshot below highlights the major components.

.. image:: cluster_dashboard.png
   :alt: Cluster Dashboard overview
   :width: 600px

Installation and Setup
----------------------

This guide assumes that you have access to a Windows Server environment. To
install the CentreStack server software:

1. Ensure prerequisites are met: a supported Windows Server edition, IIS,
   .NET Framework 4.8 or later, and a SQL database (either SQL Server or
   MySQL).
2. Download the CentreStack installer and run it on the server.
3. Follow the setup wizard to install the server components.
4. When prompted, configure the database connection (SQL Server or MySQL) and
   create or connect to an existing database.
5. Specify the hostname and port for the web portal.
6. Create the cluster administrator account with a strong password.
7. Complete the installation and sign in to the web portal using the cluster
   admin credentials.

Initial Configuration
---------------------

After installation, perform the following tasks to set up your first tenant
and users:

1. Navigate to **Tenant Manager** and click **New Tenant**.
2. Enter a name, administrator email, plan and storage settings, then
   proceed to create the tenant.
3. In the newly created tenant, go to **Team Folders** and attach existing
   file server folders or cloud storage as team folders.
4. Invite users and groups to the tenant. You can create native users or
   import users and groups from Active Directory.
5. Test end‑user access using the web portal and native clients to ensure
   the configuration works as expected.
