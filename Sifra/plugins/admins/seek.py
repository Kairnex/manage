    from pyrogram import filters
    from pyrogram.types import Message
    from Sifra import YouTube, app
    from Sifra.core.call import Ayano
    from Sifra.misc import db
    from Sifra.utils import AdminRightsCheck, seconds_to_min
    from Sifra.utils.inline import close_markup
    from config import BANNED_USERS
    @app.on_message(
    filters.command(["seek", "cseek", "seekback", "cseekback"])
    & filters.group
    & ~BANNED_USERS
    )
    @AdminRightsCheck
    async def seek_comm(cli, message: Message, _, chat_id):
    if len(message.command) == 1:
    return await message.reply_text(_["admin_20"])
    query = message.text.split(None, 1)[1].strip()
    if not query.isnumeric():
    return await message.reply_text(_["admin_21"])
    if duration_seconds == 0:
    return await message.reply_text(_["admin_22"])
    duration_to_skip = int(query)
    if message.command[0][-2] == "c":
    return await message.reply_text(
    reply_markup=close_markup(_),
    )
    else:
    return await message.reply_text(
    reply_markup=close_markup(_),
    )
    mystic = await message.reply_text(_["admin_24"])
    if "vid_" in file_path:
    if n == 0:
    return await message.reply_text(_["admin_22"])
    if check:
    file_path = check
    if "index_" in file_path:
    try:
    await Ayano.seek_stream(
    chat_id,
    file_path,
    seconds_to_min(to_seek),
    duration,
    )
    except:
    return await mystic.edit_text(_["admin_26"], reply_markup=close_markup(_))
    if message.command[0][-2] == "c":
    else:
    await mystic.edit_text(
    text=_["admin_25"].format(seconds_to_min(to_seek), message.from_user.mention),
    reply_markup=close_markup(_),
    )
