from pyrogram import filters
from Sifra import YouTube, app
from Sifra.utils.decorators.language import languageCB
from Sifra.utils.stream.stream import stream
from config import BANNED_USERS
@app.on_callback_query(filters.regex("LiveStream") & ~BANNED_USERS)
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
video = True if mode == "v" else None
user_name = CallbackQuery.from_user.first_name
await CallbackQuery.message.delete()
try:
await CallbackQuery.answer()
except:
pass
mystic = await CallbackQuery.message.reply_text(
)
try:
except:
if not details["duration_min"]:
try:
await stream(
_,
mystic,
user_id,
details,
chat_id,
user_name,
CallbackQuery.message.chat.id,
video,
streamtype="live",
)
except Exception as e:
ex_type = type(e).__name__
err = e if ex_type == "AssistantErr" else _["general_2"].format(ex_type)
return await mystic.edit_text(err)
else:
return await mystic.edit_text("» ɴᴏᴛ ᴀ ʟɪᴠᴇ sᴛʀᴇᴀᴍ.")
await mystic.delete()
