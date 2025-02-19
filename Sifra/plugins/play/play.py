import random
import string
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from pytgcalls.exceptions import NoActiveGroupCall
import config
from Sifra.core.call import Ayano
from Sifra.utils import seconds_to_min, time_to_seconds
from Sifra.utils.decorators.language import languageCB
from Sifra.utils.formatters import formats
from Sifra.utils.inline import (
livestream_markup,
slider_markup,
)
from Sifra.utils.stream.stream import stream
from config import BANNED_USERS, lyrical
@app.on_message(
filters.command(
[
]
)
& filters.group
& ~BANNED_USERS
)
client,
message: Message,
_,
chat_id,
video,
channel,
url,
):
mystic = await message.reply_text(
)
plist_id = None
slider = None
plist_type = None
user_id = message.from_user.id
user_name = message.from_user.first_name
audio_telegram = (
(message.reply_to_message.audio or message.reply_to_message.voice)
if message.reply_to_message
else None
)
video_telegram = (
(message.reply_to_message.video or message.reply_to_message.document)
if message.reply_to_message
else None
)
if audio_telegram:
if audio_telegram.file_size > 104857600:
duration_min = seconds_to_min(audio_telegram.duration)
if (audio_telegram.duration) > config.DURATION_LIMIT:
return await mystic.edit_text(
)
file_path = await Telegram.get_filepath(audio=audio_telegram)
if await Telegram.download(_, message, mystic, file_path):
message_link = await Telegram.get_link(message)
file_name = await Telegram.get_filename(audio_telegram, audio=True)
dur = await Telegram.get_duration(audio_telegram, file_path)
details = {
"title": file_name,
"link": message_link,
"path": file_path,
"dur": dur,
}
try:
await stream(
_,
mystic,
user_id,
details,
chat_id,
user_name,
message.chat.id,
streamtype="telegram",
)
except Exception as e:
ex_type = type(e).__name__
err = e if ex_type == "AssistantErr" else _["general_2"].format(ex_type)
return await mystic.edit_text(err)
return await mystic.delete()
return
elif video_telegram:
if message.reply_to_message.document:
try:
ext = video_telegram.file_name.split(".")[-1]
if ext.lower() not in formats:
return await mystic.edit_text(
)
except:
return await mystic.edit_text(
)
if video_telegram.file_size > config.TG_VIDEO_FILESIZE_LIMIT:
file_path = await Telegram.get_filepath(video=video_telegram)
if await Telegram.download(_, message, mystic, file_path):
message_link = await Telegram.get_link(message)
file_name = await Telegram.get_filename(video_telegram)
dur = await Telegram.get_duration(video_telegram, file_path)
details = {
"title": file_name,
"link": message_link,
"path": file_path,
"dur": dur,
}
try:
await stream(
_,
mystic,
user_id,
details,
chat_id,
user_name,
message.chat.id,
video=True,
streamtype="telegram",
)
except Exception as e:
ex_type = type(e).__name__
err = e if ex_type == "AssistantErr" else _["general_2"].format(ex_type)
return await mystic.edit_text(err)
return await mystic.delete()
return
elif url:
if await YouTube.exists(url):
try:
url,
message.from_user.id,
)
except:
plist_type = "yt"
if "&" in url:
plist_id = (url.split("=")[1]).split("&")[0]
else:
plist_id = url.split("=")[1]
elif "https://youtu.be" in url:
videoid = url.split("/")[-1].split("?")[0]
streamtype = "youtube"
img = details["thumb"]
details["title"],
details["duration_min"],
)    
else:
try:
except:
streamtype = "youtube"
img = details["thumb"]
details["title"],
details["duration_min"],
)
return await mystic.edit_text(
"» sᴘᴏᴛɪғʏ ɪs ɴᴏᴛ sᴜᴘᴘᴏʀᴛᴇᴅ ʏᴇᴛ.\n\nᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ."
)
try:
except:
streamtype = "youtube"
img = details["thumb"]
try:
except Exception:
elif "album" in url:
try:
except:
plist_type = "spalbum"
elif "artist" in url:
try:
except:
plist_type = "spartist"
else:
elif await Apple.valid(url):
if "album" in url:
try:
except:
streamtype = "youtube"
img = details["thumb"]
try:
except:
plist_type = "apple"
img = url
else:
elif await Resso.valid(url):
try:
except:
streamtype = "youtube"
img = details["thumb"]
try:
except:
duration_sec = details["duration_sec"]
if duration_sec > config.DURATION_LIMIT:
return await mystic.edit_text(
config.DURATION_LIMIT_MIN,
app.mention,
)
)
try:
await stream(
_,
mystic,
user_id,
details,
chat_id,
user_name,
message.chat.id,
)
except Exception as e:
ex_type = type(e).__name__
err = e if ex_type == "AssistantErr" else _["general_2"].format(ex_type)
return await mystic.edit_text(err)
return await mystic.delete()
else:
try:
await Ayano.stream_call(url)
except NoActiveGroupCall:
await mystic.edit_text(_["black_9"])
return await app.send_message(
chat_id=config.LOGGER_ID,
)
except Exception as e:
return await mystic.edit_text(_["general_2"].format(type(e).__name__))
await mystic.edit_text(_["str_2"])
try:
await stream(
_,
mystic,
message.from_user.id,
url,
chat_id,
message.from_user.first_name,
message.chat.id,
video=video,
streamtype="index",
)
except Exception as e:
ex_type = type(e).__name__
err = e if ex_type == "AssistantErr" else _["general_2"].format(ex_type)
return await mystic.edit_text(err)
else:
if len(message.command) < 2:
return await mystic.edit_text(
reply_markup=InlineKeyboardMarkup(buttons),
)
slider = True
query = message.text.split(None, 1)[1]
if "-v" in query:
query = query.replace("-v", "")
try:
except:
streamtype = "youtube"
if not plist_type:
if details["duration_min"]:
duration_sec = time_to_seconds(details["duration_min"])
if duration_sec > config.DURATION_LIMIT:
return await mystic.edit_text(
)
else:
buttons = livestream_markup(
_,
user_id,
"v" if video else "a",
"c" if channel else "g",
)
return await mystic.edit_text(
reply_markup=InlineKeyboardMarkup(buttons),
)
try:
await stream(
_,
mystic,
user_id,
details,
chat_id,
user_name,
message.chat.id,
video=video,
streamtype=streamtype,
)
except Exception as e:
ex_type = type(e).__name__
err = e if ex_type == "AssistantErr" else _["general_2"].format(ex_type)
return await mystic.edit_text(err)
await mystic.delete()
else:
if plist_type:
ran_hash = "".join(
random.choices(string.ascii_uppercase + string.digits, k=10)
)
lyrical[ran_hash] = plist_id
_,
ran_hash,
message.from_user.id,
plist_type,
"c" if channel else "g",
)
await mystic.delete()
await message.reply_photo(
photo=img,
caption=cap,
reply_markup=InlineKeyboardMarkup(buttons),
)
else:
if slider:
buttons = slider_markup(
_,
message.from_user.id,
query,
0,
"c" if channel else "g",
)
await mystic.delete()
await message.reply_photo(
photo=details["thumb"],
details["title"].title(),
details["duration_min"],
),
reply_markup=InlineKeyboardMarkup(buttons),
)
else:
_,
message.from_user.id,
"c" if channel else "g",
)
await mystic.delete()
await message.reply_photo(
photo=img,
caption=cap,
reply_markup=InlineKeyboardMarkup(buttons),
)
@languageCB
callback_data = CallbackQuery.data.strip()
callback_request = callback_data.split(None, 1)[1]
if CallbackQuery.from_user.id != int(user_id):
try:
except:
return
try:
except:
return
user_name = CallbackQuery.from_user.first_name
try:
await CallbackQuery.message.delete()
await CallbackQuery.answer()
except:
pass
mystic = await CallbackQuery.message.reply_text(
)
try:
except:
if details["duration_min"]:
duration_sec = time_to_seconds(details["duration_min"])
if duration_sec > config.DURATION_LIMIT:
return await mystic.edit_text(
)
else:
buttons = livestream_markup(
_,
CallbackQuery.from_user.id,
mode,
)
return await mystic.edit_text(
reply_markup=InlineKeyboardMarkup(buttons),
)
video = True if mode == "v" else None
try:
await stream(
_,
mystic,
CallbackQuery.from_user.id,
details,
chat_id,
user_name,
CallbackQuery.message.chat.id,
video,
streamtype="youtube",
)
except Exception as e:
ex_type = type(e).__name__
err = e if ex_type == "AssistantErr" else _["general_2"].format(ex_type)
return await mystic.edit_text(err)
return await mystic.delete()
@app.on_callback_query(filters.regex("AnonymousAdmin") & ~BANNED_USERS)
async def anonymous_check(client, CallbackQuery):
try:
await CallbackQuery.answer(
"» ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ :\n\nᴏᴘᴇɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs.\n-> ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs\n-> ᴄʟɪᴄᴋ ᴏɴ ʏᴏᴜʀ ɴᴀᴍᴇ\n-> ᴜɴᴄʜᴇᴄᴋ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴs.",
show_alert=True,
)
except:
pass
@languageCB
callback_data = CallbackQuery.data.strip()
callback_request = callback_data.split(None, 1)[1]
(
videoid,
user_id,
ptype,
mode,
) = callback_request.split("|")
if CallbackQuery.from_user.id != int(user_id):
try:
except:
return
try:
except:
return
user_name = CallbackQuery.from_user.first_name
await CallbackQuery.message.delete()
try:
await CallbackQuery.answer()
except:
pass
mystic = await CallbackQuery.message.reply_text(
)
videoid = lyrical.get(videoid)
video = True if mode == "v" else None
if ptype == "yt":
try:
videoid,
CallbackQuery.from_user.id,
True,
)
except:
try:
except:
if ptype == "spalbum":
try:
except:
if ptype == "spartist":
try:
except:
if ptype == "apple":
try:
except:
try:
await stream(
_,
mystic,
user_id,
result,
chat_id,
user_name,
CallbackQuery.message.chat.id,
video,
)
except Exception as e:
ex_type = type(e).__name__
err = e if ex_type == "AssistantErr" else _["general_2"].format(ex_type)
return await mystic.edit_text(err)
return await mystic.delete()
@app.on_callback_query(filters.regex("slider") & ~BANNED_USERS)
@languageCB
async def slider_queries(client, CallbackQuery, _):
callback_data = CallbackQuery.data.strip()
callback_request = callback_data.split(None, 1)[1]
(
what,
rtype,
query,
user_id,
) = callback_request.split("|")
if CallbackQuery.from_user.id != int(user_id):
try:
except:
return
what = str(what)
rtype = int(rtype)
if what == "F":
if rtype == 9:
query_type = 0
else:
query_type = int(rtype + 1)
try:
except:
pass
title, duration_min, thumbnail, vidid = await YouTube.slider(query, query_type)
med = InputMediaPhoto(
media=thumbnail,
title.title(),
duration_min,
),
)
return await CallbackQuery.edit_message_media(
media=med, reply_markup=InlineKeyboardMarkup(buttons)
)
if what == "B":
if rtype == 0:
query_type = 9
else:
query_type = int(rtype - 1)
try:
except:
pass
title, duration_min, thumbnail, vidid = await YouTube.slider(query, query_type)
med = InputMediaPhoto(
media=thumbnail,
title.title(),
duration_min,
),
)
return await CallbackQuery.edit_message_media(
media=med, reply_markup=InlineKeyboardMarkup(buttons)
)
