import re
from os import getenv
import config
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "21189715"))

API_HASH = getenv("API_HASH", "988a9111105fd2f0c5e21c2c2449edfd")

BOT_TOKEN = getenv("BOT_TOKEN","7258579835:AAFDsRl4zjWMyQJc3PLlA602QdZfG2FHLZ8")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ayanosuvii0925:subhichiku123@cluster0.uw8yxkl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

)

LOGGER_ID = int(getenv("LOGGER_ID", "-1001956979385"))

OWNER_ID = int(getenv("OWNER_ID", "6999372290"))

BOT_USERNAME = getenv("BOT_USERNAME" , "")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ayanokozii/Sifra2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Anya")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/II_AYANO_II")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/pahadichat")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))





CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION",  "BQFPq6kArdA70evSPgUWvXABCn8OYKFfLfwa0vDEgD6cSIcWsh08iTw5Lg0n4sAqefmcbfu9Xz1RADdmjUXEoKOy0e5iLDK3kl-UBjuCe9wA499ySdCOp6EqVpZeIXq5TgqYoHWWSEw8cE1jUhX_ETe2OJ1_lWa5X7W7Vmtd4_LhzMb5CAoLoQOxoCJ_tRWzm7sfqpwNWlU-V7BKmm8oegkdTfS8Xcb2XvBRwnIEJK5v7KPnMNypJRWRJ6BE_xHlmsJ1VWrG4l1KXtWvuF05ZfKLVrtd7Huu80-mxJTn-5UbXsQIFKqmSG1VLtNX3uRS4-76vBM7CHkf9mPhm-FqfxLnI04yCwAAAAGSN1vtAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
)
STATS_IMG_URL = "https://te.legra.ph/file/4a7c28726502e24ea0fe0.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/81df44f3679946babd8c3.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/53f1a295e172d39eaa39d.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/81df44f3679946babd8c3.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
