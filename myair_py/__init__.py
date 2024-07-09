from aiohttp import ClientSession
from .legacy_client import LegacyClient
from .new_client import RESTClient
from .myair_client import MyAirConfig

class ClientFactory:
    config: MyAirConfig
    session: ClientSession

    def __init__(self, config = None, session = None):
        self.config = config
        self.session = session
    
    def config(self, config: MyAirConfig):
        self.config = config
        return self
    
    def session(self, session: ClientSession):
        self.session = session
        return self

    def get(self):
        assert(self.config and self.session)
        if self.config.region == "NA":
            return RESTClient(self.config, self.session)
        elif self.config.region == "EU":
            return LegacyClient(self.config, self.session)
        assert False, "Region must be NA or EU"
