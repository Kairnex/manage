from typing import Union
from config import OWNER_ID, SUPPORT_CHAT
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
_,
DURATION,
videoid,
dur: Union[bool, int] = None,
):
not_dur = [
[
InlineKeyboardButton(
text=_["QU_B_1"],
),
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data="close",
),
],
[
InlineKeyboardButton(
text="🎧 𝐎𝐖𝐍𝐄𝐑 🎧", url=f"tg://openmessage?user_id={OWNER_ID}",
),
InlineKeyboardButton(
text="🏯 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🏯", url=SUPPORT_CHAT,
),
],
]
dur = [
[
InlineKeyboardButton(
callback_data="GetTimer",
)
],
[
InlineKeyboardButton(
text=_["QU_B_1"],
),
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data="close",
),
],
[
InlineKeyboardButton(
text="🎧 𝐎𝐖𝐍𝐄𝐑 🎧", url=f"tg://openmessage?user_id={OWNER_ID}",
),
InlineKeyboardButton(
text="🏯 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🏯", url=SUPPORT_CHAT,
),
],
]
upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
return upl
upl = InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text=_["BACK_BUTTON"],
),
InlineKeyboardButton(
text=_["CLOSE_BUTTON"],
callback_data="close",
),
],
[
InlineKeyboardButton(
text="🎧 𝐎𝐖𝐍𝐄𝐑 🎧", url=f"tg://openmessage?user_id={OWNER_ID}",
),
InlineKeyboardButton(
text="🏯 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🏯", url=SUPPORT_CHAT,
),
],
]
)
return upl
def aq_markup(_, chat_id):
buttons = [
#[
#InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
#InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
#InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
#],
[
InlineKeyboardButton(
text="🎧 𝐎𝐖𝐍𝐄𝐑 🎧", url=f"tg://openmessage?user_id={OWNER_ID}",
),
InlineKeyboardButton(
text="🏯 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🏯", url=SUPPORT_CHAT,
),
],
]
return buttons
