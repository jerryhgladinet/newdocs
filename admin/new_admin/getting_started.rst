Getting Started
===============

.. contents:: Table of Contents
   :local:
   :depth: 2

This section provides an introduction to CentreStack administration, including setup and essential configuration tasks.

Introduction
------------

Welcome to the CentreStack Administration Guide. CentreStack is a mobile access and secure file sharing solution that focuses on local file server cloud‑enablement. It runs on Microsoft Windows Server and includes client agents for Windows, Mac OS X, web browsers and mobile devices (Android and iOS).

Important: there is also a client application for Windows File Server called the *Server Agent*. That component is outside the scope of this guide.

Overview
--------

CentreStack differentiates itself from other file sync and share solutions by focusing on data security, permission controls and hybrid file server mobilization. Key capabilities include:

* **Maintaining NTFS and Active Directory permissions** – user permissions and security inherit from your existing file servers.
* **Live sync and versioning** – files are synchronized in real time with version control and revision history.
* **On‑demand access** – users access files directly from the server in real time; read‑only and write permissions are honoured on demand.
* **Mirroring network shares** – existing network shares can be published as Team Folders for collaboration without migration.
* **Drive mapping & file locking** – the Windows client provides a mapped drive with file locking, version control and offline caching.

Installation and Setup
-----------------------

CentreStack Server can be deployed on‑premises or in a private cloud. Basic requirements include Windows Server 2016 or later, IIS, .NET Framework, and a database (SQL Server or MySQL). The installer bundles required components, but you may deploy the database separately.

1. **Download and run the installer**. Obtain the CentreStack Server package from the official site and run it on a supported Windows Server. The setup wizard installs the web components and prompts for a database connection.
2. **Configure the database**. You can choose to install a local SQL Express instance or point to an existing SQL Server/MySQL database. The database stores metadata, configuration and audit logs.
3. **Create the cluster administrator account**. During installation, specify an email address and password for the cluster (master) administrator. This account will manage tenants, storage and system settings.
4. **Complete installation and sign in**. After installation finishes, open a browser to `https://your-server-address/portal`. Log in with the cluster administrator credentials.

Initial Configuration
---------------------

After signing in, perform the following initial configuration tasks:

* **Create your first tenant**. In the Tenant Manager, click **Create Tenant**, provide a tenant name, assign a tenant administrator email and choose a plan. A tenant represents a customer or business unit and has its own users, policies and storage.
* **Add storage connectors or Team Folders**. Connect file server shares or cloud storage as Team Folders. When creating a Team Folder, specify the underlying storage path (e.g., a network share or NAS) and choose how permissions will be inherited from NTFS or assigned manually.
* **Invite users and groups**. Add native users manually or import existing users and groups from Active Directory. Assign users to Team Folders and groups, and configure quotas and policies.
* **Test end‑user access**. Log in as a tenant administrator or regular user via the web portal, Windows client or mobile client. Verify that files are accessible, changes synchronize correctly, and security settings (e.g., read‑only) behave as expected.

Completing these steps provides a working CentreStack deployment ready for further configuration and branding.
