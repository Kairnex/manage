from pyrogram import filters
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus, ChatType
from pyrogram.types import Message
from Sifra import app
from Sifra.utils.database import set_cmode
from Sifra.utils.decorators.admins import AdminActual
from config import BANNED_USERS
@AdminActual
if len(message.command) < 2:
query = message.text.split(None, 2)[1].lower().strip()
if (str(query)).lower() == "disable":
await set_cmode(message.chat.id, None)
elif str(query) == "linked":
chat = await app.get_chat(message.chat.id)
if chat.linked_chat:
chat_id = chat.linked_chat.id
await set_cmode(message.chat.id, chat_id)
return await message.reply_text(
)
else:
else:
try:
chat = await app.get_chat(query)
except:
if chat.type != ChatType.CHANNEL:
try:
async for user in app.get_chat_members(
chat.id, filter=ChatMembersFilter.ADMINISTRATORS
):
if user.status == ChatMemberStatus.OWNER:
cusn = user.user.username
crid = user.user.id
except:
if crid != message.from_user.id:
await set_cmode(message.chat.id, chat.id)
