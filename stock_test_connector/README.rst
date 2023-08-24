=================
Stock Connector
=================



This module allows connecting to an external service to read product data and make proper adjustments in odoo inventory.
The addon requires OCA addon queue, which can be loaded from https://github.com/OCA/queue


Configuration
=============

To use this module, you need to :

Go to Inventory > Configuration > Stock Service > add proper external service records > test connection with UI interface
Go to Settings > Scheduled actions > (Select cron 'Service - get product info') > Set active, configure time if needed

Usage
=====

After service configuration, the addon will generate jobs to update product list and state which can be found in the Job Queue

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/vuwnevska/test_task/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed

Known issues / Roadmap
======================

* check for TODO's in the code to complete the implementation
* make multi-company safe
* make multi-stock safe