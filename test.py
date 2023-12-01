from agent.downloader.web_img import ImageDownloader
import time


async def main(url):
    downloader = ImageDownloader()
    await downloader.download(url)


if __name__ == '__main__':
    import asyncio
    url = "https://telegra.ph/森罗财团-细雪-01E4K-103P-1V-375G-11-28"
    start = time.time()
    asyncio.run(main(url))
    end = time.time()
    print(end - start)
