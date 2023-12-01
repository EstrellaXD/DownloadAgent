from aioqb import Client
from agent.config import config
from agent.network import RequestContent


async def send_magent(torrent_link: str):
    async with Client(url=config.qb_host, username=config.qb_username, password=config.qb_password) as client:
        await client.torrents_add(
            urls=[torrent_link],
            savepath="/downloads/Movie",
        )


async def send_torrent(torrent_link: str):
    async with RequestContent() as request:
        content = await request.get(torrent_link)
    async with Client(url=config.qb_host, username=config.qb_username, password=config.qb_password) as client:
        await client.torrents_add(
            torrents=content,
            savepath="/downloads/Movie",
        )