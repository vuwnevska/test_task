# License

import logging

import requests

_logger = logging.getLogger(__name__)


class ConnectorService:
    def __init__(
        self,
        url,
        test_service,
    ):

        requests.Session()
        # if test_service:
        self.client = ""
        if url:
            self.service = self.client.create_service()
        else:
            self.service = self.client.service

    @staticmethod
    def handle_fault(fault):
        # TODO better message handling
        msg = ("{}\n").format(fault.message)
        _logger.info("Connector fault : {}".format(msg))
        return msg
