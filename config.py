import os
from dotenv import load_dotenv
import logging

logging.basicConfig(
    format="%(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

load_dotenv()


class Config(object):
    # Get a token from @BotFather
    BOT_TOKEN = "6411516712:AAFk3hqpYt5erpF0ExpAwW54JytLZR3XuQ4"
    # The Telegram API things
    API_ID = "5986296"
    API_HASH = "7e38dc5d2f8302364f8051a68afae05b"
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot

    # File /video download location
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 4194304000

    # Chunk size that should be used with requests : default is 128KB
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # Proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # Set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3700

    OWNER_ID = os.environ.get("1098983599")
    ADL_BOT_RQ = {}
    AUTH_USERS = list({int(x) for x in os.environ.get("AUTH_USERS", "2090127712").split()})
    AUTH_USERS.append(OWNER_ID)
