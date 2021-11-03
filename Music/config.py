##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID", "7754894"))
API_HASH = getenv("API_HASH")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "540000"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001525866631"))
ASS_ID = int(getenv("ASS_ID", "2047725868"))
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
