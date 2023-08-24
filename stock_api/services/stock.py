# License

from odoo.addons.component.core import Component


class StockService(Component):
    _inherit = "base.rest.service"
    _name = "stock.inventory.rest"
    _usage = "inventory"
    _collection = "rest.stock.public.service"
    _description = "Access to the product"

    def update_inventory(self, **params):
        """
        Update inventory leftovers for product
        """

        env = self.env(user=self.env.ref("base.user_admin"))
        product = env["product.product"].search(
            [("barcode", "=", params["sku"])], limit=1
        )
        if product.type == "product":
            stock_location = env.ref("stock.stock_location_stock")
            env["stock.quant"]._update_available_quantity(
                product, stock_location, params["qty"]
            )
            return {"response": "PUT called update {} ".format(product.id)}
        return {
            "response": "PUT inventory update failed for sku {} ".format(params["sku"])
        }

    # Validator

    def _validator_update_inventory(self):
        return {
            "sku": {"type": "string"},
            "qty": {
                "type": "float",
                "required": True,
                "nullable": True,
            },
        }

    def _validator_return_update_inventory(self):
        return {"response": {"type": "string"}}
