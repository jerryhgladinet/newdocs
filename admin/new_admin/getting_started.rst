Getting Started
================

This section introduces CentreStack administration and explains how to 
access the management portal. It also outlines additional resources you 
should review before proceeding.

Introduction
------------

Welcome to the CentreStack Administration Guide. CentreStack is a mobile
access and secure file‑sharing solution that focuses on local file server
cloud‑enablement. It runs on Microsoft Windows Server and includes client
agents for Windows, **macOS**, web browsers and mobile devices (Android and iOS).

.. important::

   CentreStack includes a client application for Windows File Server called 
   **Server Agent**. This document covers CentreStack itself and does not cover the
   *Server Agent* component.

.. attention::

   This admin guide is written for CentreStack version 16.6.10352.56511.
   Future releases may introduce new features and changes.

Overview
--------

CentreStack bridges the gap between traditional file servers and modern 
cloud workflows. It allows organisations to provide secure remote access to 
existing Windows file servers without the cost, complexity or risk of migrating 
all data to a public cloud. By combining *on‑demand access*, *drive mapping*,
*file locking* and *real‑time synchronisation*, CentreStack gives remote and 
mobile users a native file‑sharing experience while IT retains control over data
residency, permissions and compliance.

Key capabilities include:

* **Hybrid file server mobilisation** – Publish existing Windows file server
  shares as team folders without moving the data; users connect through a mapped 
  drive or web portal and see the same folder structure and permissions that 
  already exist on the server.  **Because CentreStack uses HTTPS tunnelling, these
  mapped drives work without a VPN.**
* **Active Directory & NTFS integration** – User accounts and groups are 
  synchronised from Active Directory or Azure AD, and NTFS permissions are 
  preserved. You can also create native accounts for external collaborators.
* **On‑demand access & caching** – Files are not fully synchronised to the 
  client; instead they are fetched on demand. Administrators can enable offline 
  caching for selected folders or user devices to allow work without an internet 
  connection.
* **Secure collaboration** – Built‑in features include two‑factor 
  authentication, SAML single sign‑on, distributed file locking, ransomware 
  detection, data leak protection and detailed audit logs.
* **Extensible storage** – Besides file servers, you can attach other 
  storage backends such as Azure Blob, Amazon S3 or Wasabi to expand capacity or 
  tier data while maintaining a single namespace.
* **VPN‑less remote access** – CentreStack leverages secure HTTPS to provide
  remote access and drive mapping without requiring a VPN. This simplifies 
  administration and improves performance for remote users.

Before You Begin
----------------

CentreStack administration builds on three other guides that address 
installation, deployment and high‑level orientation. Read or skim these guides 
first:

* **`Quick Start Guide <https://cdn.centrestack.com/mobi5/web/library/quick-
start/index.html>`_** – Provides a high‑level overview of CentreStack and the 
  problems it solves. The guide explains the three deployment models – 
  **On‑premises self‑hosted**, **data‑centre MSP‑hosted** and **cloud 
  SaaS‑hosted** – and describes the benefits of each. It also walks you through 
  registering for a partner account, accessing the partner portal and setting up a
  trial environment.
* **`Installation Guide 
<https://cdn.centrestack.com/mobi5/web/library/install/index.html>`_** – Offers 
  step‑by‑step instructions for installing the CentreStack server on Windows 
  Server. It covers prerequisites such as preparing file storage, optional 
  Active Directory integration, configuring a SQL Server or MySQL database, 
  running the installer and completing the initial setup. After following the 
  Installation Guide you will have a working CentreStack server and a cluster 
  administrator account.
* **`Deployment Guide 
<https://cdn.centrestack.com/mobi5/web/library/deploy/index.html>`_** – Focuses 
  on planning and sizing your CentreStack deployment. It discusses terminology, 
  system requirements, hardware sizing, capacity planning, load balancing and 
  deployment scenarios for on‑premises, hosted and cloud environments. It also 
  covers best practices for Active Directory integration, storage, backup and 
  security. Review this guide to ensure your infrastructure is ready before going 
  live.

Accessing the Web Portal
------------------------

Once CentreStack is installed, open a browser to access the web portal. If 
you are on the server console (local keyboard/monitor or via Remote Desktop), 
navigate to ``http://localhost/``. If you configured a fully qualified domain 
name or external URL during installation, use that address instead.

.. note::

   The login page displays the CentreStack build number in the lower right 
   corner and prompts for the cluster administrator credentials you created 
   earlier.

``(Screenshot placeholder: centrestack‑main‑login‑screen.png – shows the default CentreStack login screen with the title **"Sign In"**, input boxes for username and password, a **Sign In** button and the build number in the lower right corner.)``

First page: Tenant Manager
--------------------------

After successful login you land on the **Tenant Manager**. This page lists 
existing tenants and allows you to create new ones, assign administrators, view 
storage usage and check security alerts. If only one tenant exists, the Tenant 
Manager acts as both cluster and tenant administration portal. From the Tenant 
Manager you can navigate to other modules such as Settings, Reports and 
Branding.

``(Screenshot placeholder: cluster‑admin‑main‑interface‑after‑login‑multi‑tenancy.png – shows the Tenant Manager page with a **New Tenant** tile (plus icon) and cards for existing tenants.  The blue banner displays trial days left and navigation icons.)``

Cluster Dashboard Overview
--------------------------

The **Cluster Dashboard** provides a high‑level view of the health and 
status of your CentreStack installation. It summarises licence usage, server 
farm status, worker node health and client versions, and provides quick links to
common administrative tasks such as cluster branding, group policy and reports. 
You can reach the dashboard by clicking the **Dashboard** button in the 
navigation menu.

``(Screenshot placeholder: cluster‑admin‑main‑interface‑after‑login‑multi‑tenancy.png – same as above; shows the Cluster Dashboard.  Labels and graphs highlight licence usage, node health and quick links to Branding, Group Policy and Reports.)``

Next Steps
----------

With an understanding of how to access the portal and where key modules 
live, you can proceed through the rest of this Administration Guide. The 
following chapters describe tenant management, settings, reports, branding, 
client downloads and troubleshooting in detail.