from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    bot_token = str(os.getenv("BOT_TOKEN"))
    user_id = int(os.getenv("USER_ID"))
    proxy = str(os.getenv("PROXY"))
    qb_host = str(os.getenv("QB_HOST"))
    qb_username = str(os.getenv("QB_USERNAME"))
    qb_password = str(os.getenv("QB_PASSWORD"))


config = Config()
