from agent.network import RequestContent
from bs4 import BeautifulSoup
import asyncio
from pathlib import Path
from urllib3.util import parse_url
from urllib.parse import unquote
from agent.config import IMAGE_DL_PATH


class ImageDownloader:
    def __init__(self):
        pass

    @staticmethod
    async def __get_image_urls(url: str):
        root_url = parse_url(url).scheme + '://' + parse_url(url).host
        async with RequestContent() as request:
            content = await request.get(url)
        img_urls = BeautifulSoup(content, 'html.parser').find_all('img')
        return [root_url + img_url['src'] for img_url in img_urls]

    @staticmethod
    async def __download_image(url: str):
        async with RequestContent() as request:
            content = await request.get(url)
        return content

    async def __save_image(self, save_dir: Path, url: str):
        save_dir.mkdir(parents=True, exist_ok=True)
        content = await self.__download_image(url)
        path = save_dir.joinpath(parse_url(url).path.split('/')[-1])
        with open(path, 'wb') as f:
            f.write(content)

    async def download(self, url: str):
        img_urls = await self.__get_image_urls(url)
        folder_name = unquote(parse_url(url).path.replace('/', ''))
        save_dir = IMAGE_DL_PATH.joinpath(folder_name)
        tasks = [self.__save_image(save_dir, img_url) for img_url in img_urls]
        return await asyncio.gather(*tasks)
        # for img_url in img_urls:
        #     await self.__save_image(save_dir, img_url)
