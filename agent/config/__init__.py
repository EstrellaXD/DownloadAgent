from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()


class Config:
    bot_token = os.getenv("BOT_TOKEN")
    user_id = int(os.getenv("USER_ID"))
    proxy = os.getenv("PROXY") if os.getenv("PROXY") else None
    qb_host = os.getenv("QB_HOST") if os.getenv("QB_HOST") else None
    qb_username = os.getenv("QB_USERNAME") if os.getenv("QB_USERNAME") else None
    qb_password = os.getenv("QB_PASSWORD") if os.getenv("QB_PASSWORD") else None


config = Config()

if os.getenv("CONTAINER"):
    TW_DL_PATH = Path("/downloads/Twitter")
    IMAGE_DL_PATH = Path("/downloads/Image")
    YT_DL_PATH = Path("/downloads/Youtube")
else:
    TW_DL_PATH = Path("downloads/Twitter")
    IMAGE_DL_PATH = Path("downloads/Image")
    YT_DL_PATH = Path("downloads/Youtube")
