from aiohttp import ClientSession
from agent.config import config


class RequestContent:
    def __init__(self):
        self.session = None
        self.proxy = config.proxy

    async def get(self, url):
        async with self.session.get(
                url,
                proxy=self.proxy,
        ) as response:
            return await response.read()

    async def __aenter__(self):
        self.session = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()
        self.session = None
        return False
