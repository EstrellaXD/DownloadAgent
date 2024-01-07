import asyncio
from pytube import YouTube
from agent.config import YT_DL_PATH


async def download_video(url):
    # 创建一个事件循环
    loop = asyncio.get_event_loop()

    # 定义一个同步函数，用于下载YouTube视频
    def sync_download(url):
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download(output_path=YT_DL_PATH)

    # 在异步函数中调用同步函数，并确保不会阻塞主事件循环
    await loop.run_in_executor(None, sync_download, url)