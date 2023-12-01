from telebot.async_telebot import AsyncTeleBot, ExceptionHandler
from telebot import asyncio_helper
from aioqb import Client

from agent.config import config
from agent.downloader import ImageDownloader, send_torrent, send_magent
import logging


logger = logging.getLogger(__name__)
image = ImageDownloader()


bot = AsyncTeleBot(
    token=config.bot_token,
    # exception_handler=ExceptionHandler(),
    # colorful_logs=True
)
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
    await bot.send_message(message.chat.id, "Start downloading")
    await send_torrent(message.text)


# Keywords Listener
@bot.message_handler(func=lambda message: True)
async def echo(message):
    if message.chat.id != config.user_id:
        return
    # await bot.send_message(message.chat.id, message.text)
    # URL encoding with UTF-8
    entities = message.json["entities"]
    for entitie in entities:
        if entitie["type"] == "text_link":
            url = entitie["url"]
            break
    if "https://telegra.ph" in url:
        reply = await bot.reply_to(message, "Start downloading images")
        logger.info(f"Start downloading images in {url}")
        await image.download(url)
        await bot.edit_message_text("Download finished", chat_id=message.chat.id, message_id=reply.message_id)
        logger.info(f"Finish downloading")

