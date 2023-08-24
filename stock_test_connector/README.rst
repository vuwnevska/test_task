=================
Stock Connector
=================



This module adds a possibility to connect to external service to read product data and make proper adjustments in odoo inventory.
The addon requires OCA addon queue, can be loaded from https://github.com/OCA/queue


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
