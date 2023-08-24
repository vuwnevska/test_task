=================
Stock Connector
=================


.. |badge1| image:: https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production/Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Faccount--payment-lightgray.png?logo=github
    :target: https://github.com/OCA/account-payment/tree/14.0/account_due_list
    :alt: OCA/account-payment
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/account-payment-14-0/account-payment-14-0-account_due_list
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.odoo-community.org/runbot/96/14.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

This module adds a possibility to connect to external service to read product data and make proper adjustments in odoo inventory.
The addon requires OCA addon queue, can be loaded from https://github.com/OCA/queue

**Table of contents**

.. contents::
   :local:

Configuration
=============

To use this module, you need to :

Go to Inventory > Configuration > Stock Service > add proper external service records > test connection with UI interface
Go to Settings > Scheduled actions > (Select cron 'Service - get product info') > Set active, configure time if needed

Usage
=====

After service configuration addon will generate job's to update products list and state of which can be found in Job Queue

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/vuwnevska/test_task/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed

Known issues / Roadmap
======================

* check for TODO's in the code to complete implementation
* make multi-company safe
* make multi-stock safe
