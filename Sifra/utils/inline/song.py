from pyrogram.types import InlineKeyboardButton
import config
buttons = [
[
InlineKeyboardButton(
text=_["SG_B_2"],
),
InlineKeyboardButton(
text=_["SG_B_3"],
),
],
[
InlineKeyboardButton(
text="🥀 sᴜᴩᴩᴏʀᴛ 🥀", url=f"{config.SUPPORT_CHAT}",
),
InlineKeyboardButton(
text=_["CLOSE_BUTTON"], callback_data="close"
),
],
]
return buttons
