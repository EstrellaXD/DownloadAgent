from agent.network import RequestContent
import re
from agent.config import TW_DL_PATH
from urllib3.util import parse_url
import asyncio


async def save_tw_media(url: str, session: RequestContent):
    content = await session.get(url)
    TW_DL_PATH.mkdir(parents=True, exist_ok=True)
    path = TW_DL_PATH.joinpath(parse_url(url).path.split('/')[-1])
    with open(path, 'wb') as f:
        f.write(content)


async def dl_tw_media(url: str):
    twid = re.search(r"\d{15,}", url).group(0)
    async with RequestContent() as request:
        contents = await request.get_json(
            f"https://did5b1o5kj.execute-api.us-east-1.amazonaws.com/default/TwitterLinkParse?id={twid}")
        # Create tasks
        tasks = [save_tw_media(url, request) for url in contents]
        # Run tasks
        await asyncio.gather(*tasks)

