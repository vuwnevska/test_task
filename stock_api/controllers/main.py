# # License

from odoo.addons.base_rest.controllers import main


class StockPublicApiController(main.RestController):
    _root_path = "/stock_api/"
    _collection_name = "rest.stock.public.service"
    _default_auth = "public"
