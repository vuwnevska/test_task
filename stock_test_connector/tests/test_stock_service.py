# License
from unittest.mock import patch

from odoo.tests.common import SavepointCase


class CommonCase(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(
            context=dict(
                cls.env.context,
                tracking_disable=True,
                queue_job__no_delay=True,
            )
        )
        cls.quant_obj = cls.env["stock.quant"]
        cls.product_obj = cls.env["product.product"]
        cls.stock_location = cls.env.ref("stock.stock_location_stock")

        cls.product_1 = cls.product_obj.create(
            {
                "name": "Test 1",
                "list_price": 10.00,
                "default_code": "0000000001",
                "type": "product",
            }
        )
        cls.product_2 = cls.product_obj.create(
            {
                "name": "Test 2",
                "list_price": 20.00,
                "default_code": "0000000002",
                "type": "product",
            }
        )
        cls.service = cls.env["stock.service"].create(
            {
                "name": "Test Service",
                "test_service": True,
            }
        )

    def test_service_ping(self):
        pass

    @patch(
        "odoo.addons.stock_test_connector.models.stock_service.StockService.get_product_list"
    )
    def test_product_load(self, patched):
        patched.return_value = [
            {"sku": "0000000001", "product_name": "UPD name", "qty": 1},
            {"sku": "0000000003", "product_name": "Test 3", "qty": 30},
        ]
        self.assertFalse(self.product_obj.search([("default_code", "=", "0000000003")]))

        self.assertEqual(
            self.quant_obj._get_available_quantity(self.product_1, self.stock_location),
            0.0,
        )

        self.service.load_product_data()
        self.assertEqual(self.product_1.default_code, "0000000001")
        self.assertEqual(self.product_1.name, "UPD name")
        self.assertEqual(
            self.quant_obj._get_available_quantity(self.product_1, self.stock_location),
            1.0,
        )
        self.assertEqual(
            self.quant_obj._get_available_quantity(self.product_2, self.stock_location),
            0,
        )

        product_3 = self.product_obj.search([("default_code", "=", "0000000003")])
        self.assertEqual(product_3.name, "Test 3")
        self.assertEqual(
            self.quant_obj._get_available_quantity(product_3, self.stock_location), 30
        )
