    from pyrogram import filters
    from pyrogram.types import Message
    from Sifra import app
    from Sifra.core.call import Ayano
    from Sifra.utils.decorators import AdminRightsCheck
    from Sifra.utils.inline import close_markup
    from config import BANNED_USERS
    @app.on_message(filters.command(["resume", "cresume"]) & filters.group & ~BANNED_USERS)
    @AdminRightsCheck
    async def resume_com(cli, message: Message, _, chat_id):
    return await message.reply_text(_["admin_3"])
    await Ayano.resume_stream(chat_id)
    await message.reply_text(
    _["admin_4"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
