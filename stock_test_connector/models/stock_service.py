# License

import logging

from odoo import api, fields, models
from odoo.exceptions import UserError

from ..components.api import ConnectorService

_logger = logging.getLogger(__name__)


class StockService(models.Model):
    _name = "stock.service"
    _description = "Service configuration"

    name = fields.Char(required=True)
    url = fields.Char()
    username = fields.Char()
    password = fields.Char()
    test_service = fields.Boolean(string="Testing")
    active = fields.Boolean(default=True)

    def _get_connection(self):
        return ConnectorService(self.url, self.use_test_service)

    def get_product_list(self):
        """Get a list of the products."""
        self.ensure_one()
        # TODO connect authorization etc .
        return True

    def ping_service(self):
        """Ping the service."""
        # TODO

    def load_product_data(self):
        """Check for products on the service and create jobs to handle them."""
        self.ensure_one()
        res = self.get_product_list()

        for product in res:
            description = "Handle product info {}".format(product)
            self.with_delay(description=description, channel="").process_product(
                product
            )
        return "{} products updated for ".format("")

    @api.model
    def process_product(self, product_data):
        """Handle product data"""
        msg = ""

        prod_obj = self.env["product.product"]
        code = product_data["sku"]
        vals = {"name": product_data["product_name"], "default_code": code}
        # we need unique identifier for products FTM use code in case of duplicate update first
        product = prod_obj.search([("default_code", "=", code)], limit=1)
        if product:
            product.update(vals)
        if not product:
            vals.update({"type": "product"})
            product = prod_obj.create(vals)

        # simplification consider 1 stock location
        stock_location = self.env.ref("stock.stock_location_stock")
        # skip products with tracking
        if product.type == "product":
            # weak place as job asynchronous delay of job can mess up inventory
            self.env["stock.quant"]._update_available_quantity(
                product, stock_location, product_data["qty"]
            )
            msg = "Product {} - id: {} quantity is updated to {}".format(
                product.name, product.id, product_data["qty"]
            )
        else:
            msg = "Product {} - id: {} quantity is not updated".format(
                product.name, product.id
            )
        return msg

    def test_ping(self):
        """Test connection from the UI."""
        self.ensure_one()
        msg = ["Test connection to service : {}".format(self.url)]
        res = self.ping_service()
        if res:
            msg.append(" - Success pinging service")
        else:
            msg.append(" - Failed pinging service")
        raise UserError("\n".join(msg))

    @api.model
    def cron_pull_products(self):
        """Cron job to pull for products on all active services."""
        services = self.search([])
        for service in services:
            service.load_product_data()
