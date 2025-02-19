from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message
from Sifra import app
from Sifra.utils.decorators import language
from config import BANNED_USERS
@language
Direct = True
else:
Direct = None
is_non_admin = await is_nonadmin_chat(message.chat.id)
if not is_non_admin:
Group = True
else:
Group = None
else:
response = await message.reply_text(
reply_markup=InlineKeyboardMarkup(buttons),
)
