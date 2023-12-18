from telebot.async_telebot import AsyncTeleBot, ExceptionHandler
from telebot import asyncio_helper

from agent.config import config
from agent.downloader import ImageDownloader, send_torrent, send_magent, dl_tw_media, download_url, dl_yt_video
import logging


logger = logging.getLogger(__name__)
image = ImageDownloader()


bot = AsyncTeleBot(
    token=config.bot_token,
    # exception_handler=ExceptionHandler(),
    # colorful_logs=True
)
if config.proxy:
    asyncio_helper.proxy = config.proxy


@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, 'start')


@bot.message_handler(regexp="magnet")
async def magnet(message):
    if message.chat.id != config.user_id:
        return
    await bot.send_message(message.chat.id, "Start downloading torrent")
    await send_magent(message.text)


@bot.message_handler(regexp=".torrent")
async def torrent(message):
    if message.chat.id != config.user_id:
        return
    await bot.send_message(message.chat.id, "Start downloading...")
    await send_torrent(message.text)


@bot.message_handler(regexp="https://x.com")
@bot.message_handler(regexp="https://twitter.com")
async def twitter(message):
    if message.chat.id != config.user_id:
        return
    reply = await bot.reply_to(message, "Start downloading...")
    await dl_tw_media(message.text)
    await bot.edit_message_text("Download completed.", chat_id=message.chat.id, message_id=reply.message_id)


@bot.message_handler(regexp="https://www.youtube.com")
async def youtube(message):
    if message.chat.id != config.user_id:
        return
    reply = await bot.reply_to(message, "Start downloading...")
    await dl_yt_video(message.text)
    await bot.edit_message_text("Download completed.", chat_id=message.chat.id, message_id=reply.message_id)


@bot.message_handler(regexp="https://telegra.ph")
async def telegraph(message):
    if message.chat.id != config.user_id:
        return
    reply = await bot.reply_to(message, "Start downloading images...")
    logger.info(f"Start downloading images in {message.text}")
    await image.download(message.text)
    await bot.edit_message_text("Download completed.", chat_id=message.chat.id, message_id=reply.message_id)
    logger.info(f"Download completed.")


# Photo Listener
@bot.message_handler(content_types=['video'])
@bot.message_handler(content_types=['photo'])
async def photo(message):
    # Download all photo and video
    if message.chat.id != config.user_id:
        return
    # Download photos
    photos = message.json.get("photo", None)
    videos = message.json.get("video", None)
    source = photos[-1] if photos else videos[-1]
    file_id = source["file_id"]
    url = await bot.get_file_url(file_id)
    logger.info(f"Start downloading media in {url}")
    reply = await bot.reply_to(message, "Start downloading media...")
    await download_url(url)
    await bot.edit_message_text("Download completed", chat_id=message.chat.id, message_id=reply.message_id)
    logger.info(f"Download completed.")


# Keywords Listener
@bot.message_handler(func=lambda message: True)
async def download_forward(message):
    if message.chat.id != config.user_id:
        return
    entities = message.json["entities"]
    url = None
    for entitie in entities:
        if entitie["type"] == "text_link":
            url = entitie["url"]
            break
    if "https://telegra.ph" in url:
        reply = await bot.reply_to(message, "Start downloading images...")
        logger.info(f"Start downloading images in {url}")
        await image.download(url)
        await bot.edit_message_text("Download completed.", chat_id=message.chat.id, message_id=reply.message_id)
        logger.info(f"Download completed.")

