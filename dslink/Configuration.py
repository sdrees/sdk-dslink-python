from argparse import ArgumentParser
import logging


class Configuration:
    """
    Provides configuration to the DSLink.
    """

    def __init__(self, name, responder=False, requester=False, ping_time=30, keypair_path=".keys",
                 nodes_path="nodes.json", no_save_nodes=False):
        """
        Object that contains configuration for the DSLink.
        :param name: DSLink name.
        :param responder: True if responder, default is False.
        :param requester: True if requester, default is False.
        :param ping_time: Time between pings, default is 30.
        :param keypair_path: Path to save keypair, default is ".keys".
        :param nodes_path: Path to save nodes.json, default is "nodes.json".
        :param no_save_nodes: Don't use nodes.json, default is False.
        """
        if not responder and not requester:
            raise ValueError("DSLink is neither responder nor requester.")
        parser = ArgumentParser()
        parser.add_argument("--broker", default="http://localhost:8080/conn")
        parser.add_argument("--log", default="info")
        parser.add_argument("--token")
        args = parser.parse_args()
        self.name = name
        self.broker = args.broker
        self.log_level = args.log.lower()
        self.token = args.token
        self.responder = responder
        self.requester = requester
        self.ping_time = ping_time
        self.keypair_path = keypair_path
        self.nodes_path = nodes_path
        self.no_save_nodes = no_save_nodes

        if self.log_level == "critical":
            self.log_level = logging.CRITICAL
        elif self.log_level == "error":
            self.log_level = logging.ERROR
        elif self.log_level == "warning":
            self.log_level = logging.WARNING
        elif self.log_level == "info":
            self.log_level = logging.INFO
        elif self.log_level == "debug":
            self.log_level = logging.DEBUG
        elif self.log_level == "none":
            self.log_level = logging.NOTSET

    def using_token(self):
        return self.token is not None
