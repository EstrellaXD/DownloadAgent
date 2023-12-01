from agent.bot import bot
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info('Start polling...')
    asyncio.run(bot.polling())

