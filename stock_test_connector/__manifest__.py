# License
{
    "name": "Stock sync",
    "summary": " bridge to ...",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/queue",
    "depends": [
        "stock",
        "queue_job",
    ],
    "data": [
        "data/ir_cron.xml",
        "security/ir.model.access.csv",
        "views/stock_service.xml",
    ],
    "demo": [],
}
