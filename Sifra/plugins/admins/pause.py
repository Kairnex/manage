from pyrogram import filters
from pyrogram.types import Message
from Sifra import app
from Sifra.core.call import Ayano
from Sifra.utils.decorators import AdminRightsCheck
from Sifra.utils.inline import close_markup
from config import BANNED_USERS
@AdminRightsCheck
return await message.reply_text(_["admin_1"])
await message.reply_text(
_["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
)
