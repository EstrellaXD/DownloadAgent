from agent.network import RequestContent
import hashlib
from urllib3.util import parse_url
from agent.config import IMAGE_DL_PATH
import datetime


async def download_url(url):
    async with RequestContent() as request:
        content = await request.get(url)

    url = parse_url(url)
    filename = (hashlib.md5(content).hexdigest()[0:8] + "." + url.path.split(".")[-1])
    dir_path = IMAGE_DL_PATH / datetime.datetime.now().strftime("%Y-%m-%d")
    dir_path.mkdir(parents=True, exist_ok=True)
    filepath = dir_path / filename
    with open(filepath, "wb") as f:
        f.write(content)
