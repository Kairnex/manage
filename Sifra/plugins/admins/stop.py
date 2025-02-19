from pyrogram import filters
from pyrogram.types import Message
from Sifra import app
from Sifra.core.call import Ayano
from Sifra.utils.database import set_loop
from Sifra.utils.decorators import AdminRightsCheck
from Sifra.utils.inline import close_markup
from config import BANNED_USERS
@app.on_message(
filters.command(["end", "stop", "cend", "cstop"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
if not len(message.command) == 1:
return
await Ayano.stop_stream(chat_id)
await set_loop(chat_id, 0)
await message.reply_text(
_["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
)
