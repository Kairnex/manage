import os
from random import randint
from typing import Union
from pyrogram.types import InlineKeyboardMarkup
import config
from Sifra import Carbon, YouTube, app
from Sifra.core.call import Ayano
from Sifra.misc import db
from Sifra.utils.database import add_active_video_chat, is_active_chat
from Sifra.utils.exceptions import AssistantErr
from Sifra.utils.inline import aq_markup, close_markup, stream_markup
from Sifra.utils.pastebin import AyanoBin
from Sifra.utils.thumbnails import get_thumb
async def stream(
_,
mystic,
user_id,
result,
chat_id,
user_name,
original_chat_id,
video: Union[bool, str] = None,
streamtype: Union[bool, str] = None,
):
if not result:
return
await Ayano.force_stop_stream(chat_id)
count = 0
for search in result:
continue
try:
(
title,
duration_min,
duration_sec,
thumbnail,
vidid,
except:
continue
if str(duration_min) == "None":
continue
if duration_sec > config.DURATION_LIMIT:
continue
if await is_active_chat(chat_id):
chat_id,
original_chat_id,
f"vid_{vidid}",
title,
duration_min,
user_name,
vidid,
user_id,
"video" if video else "audio",
)
position = len(db.get(chat_id)) - 1
count += 1
msg += f"{count}. {title[:70]}\n"
else:
db[chat_id] = []
status = True if video else None
try:
file_path, direct = await YouTube.download(
vidid, mystic, video=status, videoid=True
)
except:
await Ayano.join_call(
chat_id,
original_chat_id,
file_path,
video=status,
image=thumbnail,
)
chat_id,
original_chat_id,
file_path if direct else f"vid_{vidid}",
title,
duration_min,
user_name,
vidid,
user_id,
"video" if video else "audio",
)
img = await get_thumb(vidid)
button = stream_markup(_, chat_id)
run = await app.send_photo(
original_chat_id,
photo=img,
caption=_["stream_1"].format(
f"https://t.me/{app.username}?start=info_{vidid}",
title[:23],
duration_min,
user_name,
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"] = run
db[chat_id][0]["markup"] = "stream"
if count == 0:
return
else:
link = await AyanoBin(msg)
lines = msg.count("\n")
if lines >= 17:
car = os.linesep.join(msg.split(os.linesep)[:17])
else:
car = msg
carbon = await Carbon.generate(car, randint(100, 10000000))
upl = close_markup(_)
return await app.send_photo(
original_chat_id,
photo=carbon,
reply_markup=upl,
)
elif streamtype == "youtube":
link = result["link"]
vidid = result["vidid"]
title = (result["title"]).title()
duration_min = result["duration_min"]
thumbnail = result["thumb"]
status = True if video else None
try:
file_path, direct = await YouTube.download(
vidid, mystic, videoid=True, video=status
)
except:
if await is_active_chat(chat_id):
chat_id,
original_chat_id,
file_path if direct else f"vid_{vidid}",
title,
duration_min,
user_name,
vidid,
user_id,
"video" if video else "audio",
)
position = len(db.get(chat_id)) - 1
button = aq_markup(_, chat_id)
await app.send_message(
chat_id=original_chat_id,
reply_markup=InlineKeyboardMarkup(button),
)
else:
db[chat_id] = []
await Ayano.join_call(
chat_id,
original_chat_id,
file_path,
video=status,
image=thumbnail,
)
chat_id,
original_chat_id,
file_path if direct else f"vid_{vidid}",
title,
duration_min,
user_name,
vidid,
user_id,
"video" if video else "audio",
)
img = await get_thumb(vidid)
button = stream_markup(_, chat_id)
run = await app.send_photo(
original_chat_id,
photo=img,
caption=_["stream_1"].format(
f"https://t.me/{app.username}?start=info_{vidid}",
title[:23],
duration_min,
user_name,
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"] = run
db[chat_id][0]["markup"] = "stream"
file_path = result["filepath"]
title = result["title"]
duration_min = result["duration_min"]
if await is_active_chat(chat_id):
chat_id,
original_chat_id,
file_path,
title,
duration_min,
user_name,
streamtype,
user_id,
"audio",
)
position = len(db.get(chat_id)) - 1
button = aq_markup(_, chat_id)
await app.send_message(
chat_id=original_chat_id,
reply_markup=InlineKeyboardMarkup(button),
)
else:
db[chat_id] = []
await Ayano.join_call(chat_id, original_chat_id, file_path, video=None)
chat_id,
original_chat_id,
file_path,
title,
duration_min,
user_name,
streamtype,
user_id,
"audio",
)
button = stream_markup(_, chat_id)
run = await app.send_photo(
original_chat_id,
photo=config.SOUNCLOUD_IMG_URL,
caption=_["stream_1"].format(
config.SUPPORT_CHAT, title[:23], duration_min, user_name
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"] = run
db[chat_id][0]["markup"] = "tg"
elif streamtype == "telegram":
file_path = result["path"]
link = result["link"]
title = (result["title"]).title()
duration_min = result["dur"]
status = True if video else None
if await is_active_chat(chat_id):
chat_id,
original_chat_id,
file_path,
title,
duration_min,
user_name,
streamtype,
user_id,
"video" if video else "audio",
)
position = len(db.get(chat_id)) - 1
button = aq_markup(_, chat_id)
await app.send_message(
chat_id=original_chat_id,
reply_markup=InlineKeyboardMarkup(button),
)
else:
db[chat_id] = []
await Ayano.join_call(chat_id, original_chat_id, file_path, video=status)
chat_id,
original_chat_id,
file_path,
title,
duration_min,
user_name,
streamtype,
user_id,
"video" if video else "audio",
)
if video:
await add_active_video_chat(chat_id)
button = stream_markup(_, chat_id)
run = await app.send_photo(
original_chat_id,
photo=config.TELEGRAM_VIDEO_URL if video else config.TELEGRAM_AUDIO_URL,
caption=_["stream_1"].format(link, title[:23], duration_min, user_name),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"] = run
db[chat_id][0]["markup"] = "tg"
elif streamtype == "live":
link = result["link"]
vidid = result["vidid"]
title = (result["title"]).title()
thumbnail = result["thumb"]
status = True if video else None
if await is_active_chat(chat_id):
chat_id,
original_chat_id,
f"live_{vidid}",
title,
duration_min,
user_name,
vidid,
user_id,
"video" if video else "audio",
)
position = len(db.get(chat_id)) - 1
button = aq_markup(_, chat_id)
await app.send_message(
chat_id=original_chat_id,
reply_markup=InlineKeyboardMarkup(button),
)
else:
db[chat_id] = []
n, file_path = await YouTube.video(link)
if n == 0:
raise AssistantErr(_["str_3"])
await Ayano.join_call(
chat_id,
original_chat_id,
file_path,
video=status,
image=thumbnail if thumbnail else None,
)
chat_id,
original_chat_id,
f"live_{vidid}",
title,
duration_min,
user_name,
vidid,
user_id,
"video" if video else "audio",
)
img = await get_thumb(vidid)
button = stream_markup(_, chat_id)
run = await app.send_photo(
original_chat_id,
photo=img,
caption=_["stream_1"].format(
f"https://t.me/{app.username}?start=info_{vidid}",
title[:23],
duration_min,
user_name,
),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"] = run
db[chat_id][0]["markup"] = "tg"
elif streamtype == "index":
link = result
title = "ɪɴᴅᴇx ᴏʀ ᴍ3ᴜ8 ʟɪɴᴋ"
duration_min = "00:00"
if await is_active_chat(chat_id):
chat_id,
original_chat_id,
"index_url",
title,
duration_min,
user_name,
link,
"video" if video else "audio",
)
position = len(db.get(chat_id)) - 1
button = aq_markup(_, chat_id)
await mystic.edit_text(
reply_markup=InlineKeyboardMarkup(button),
)
else:
db[chat_id] = []
await Ayano.join_call(
chat_id,
original_chat_id,
link,
video=True if video else None,
)
chat_id,
original_chat_id,
"index_url",
title,
duration_min,
user_name,
link,
"video" if video else "audio",
)
button = stream_markup(_, chat_id)
run = await app.send_photo(
original_chat_id,
photo=config.STREAM_IMG_URL,
caption=_["stream_2"].format(user_name),
reply_markup=InlineKeyboardMarkup(button),
)
db[chat_id][0]["mystic"] = run
db[chat_id][0]["markup"] = "tg"
await mystic.delete()
