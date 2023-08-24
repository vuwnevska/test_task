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
        # user to encapsulate external calls
        api_user = self.env.ref(
            "stock_api.user_stock_service", raise_if_not_found=False
        )
        if not api_user:
            return {"response": "PUT method failed missing user."}
        env = self.env(user=api_user)
        product = env["product.product"].search(
            [("barcode", "=", params["sku"])], limit=1
        )
        if product.type == "product":
            stock_location = env.ref("stock.stock_location_stock")
            env["stock.quant"]._update_available_quantity(
                product, stock_location, params["qty"]
            )
            return {"response": "PUT called update {} ".format(product.name)}
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
