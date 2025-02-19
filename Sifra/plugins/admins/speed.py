from pyrogram import filters
from pyrogram.types import Message

from Sifra import app
from Sifra.core.call import Ayano
from Sifra.misc import SUDOERS, db
from Sifra.utils import AdminRightsCheck
from Sifra.utils.database import is_active_chat, is_nonadmin_chat
from Sifra.utils.decorators.language import languageCB
from Sifra.utils.inline import close_markup, speed_markup
from config import BANNED_USERS, adminlist

checker = []


@app.on_message(
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
    if duration_seconds == 0:
        return await message.reply_text(_["admin_27"])
    if "downloads" not in file_path:
        return await message.reply_text(_["admin_27"])
    upl = speed_markup(_, chat_id)
    return await message.reply_text(
        text=_["admin_28"].format(app.mention),
        reply_markup=upl,
    )


@app.on_callback_query(filters.regex("SpeedUP") & ~BANNED_USERS)
@languageCB
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat, speed = callback_request.split("|")
    chat_id = int(chat)
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_5"], show_alert=True)
    is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
    if not is_non_admin:
        if CallbackQuery.from_user.id not in SUDOERS:
            admins = adminlist.get(CallbackQuery.message.chat.id)
            if not admins:
                return await CallbackQuery.answer(_["admin_13"], show_alert=True)
            else:
                if CallbackQuery.from_user.id not in admins:
                    return await CallbackQuery.answer(_["admin_14"], show_alert=True)
    if duration_seconds == 0:
        return await CallbackQuery.answer(_["admin_27"], show_alert=True)
    if "downloads" not in file_path:
        return await CallbackQuery.answer(_["admin_27"], show_alert=True)
    if checkspeed:
        if str(checkspeed) == str(speed):
            if str(speed) == str("1.0"):
                return await CallbackQuery.answer(
                    _["admin_29"],
                    show_alert=True,
                )
    else:
        if str(speed) == str("1.0"):
            return await CallbackQuery.answer(
                _["admin_29"],
                show_alert=True,
            )
    if chat_id in checker:
        return await CallbackQuery.answer(
            _["admin_30"],
            show_alert=True,
        )
    else:
        checker.append(chat_id)
    try:
        await CallbackQuery.answer(
            _["admin_31"],
        )
    except:
        pass
    mystic = await CallbackQuery.edit_message_text(
        text=_["admin_32"].format(CallbackQuery.from_user.mention),
    )
    try:
        await Ayano.speedup_stream(
            chat_id,
            file_path,
            speed,
        )
    except:
        if chat_id in checker:
            checker.remove(chat_id)
        return await mystic.edit_text(_["admin_33"], reply_markup=close_markup(_))
    if chat_id in checker:
        checker.remove(chat_id)
    await mystic.edit_text(
        text=_["admin_34"].format(speed, CallbackQuery.from_user.mention),
        reply_markup=close_markup(_),
    )
