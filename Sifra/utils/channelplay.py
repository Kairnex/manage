    from Sifra import app
    from Sifra.utils.database import get_cmode
    if command == "c":
    chat_id = await get_cmode(CallbackQuery.message.chat.id)
    if chat_id is None:
    try:
    return await CallbackQuery.answer(_["setting_7"], show_alert=True)
    except:
    return
    try:
    channel = (await app.get_chat(chat_id)).title
    except:
    try:
    except:
    return
    else:
    chat_id = CallbackQuery.message.chat.id
    channel = None
    return chat_id, channel
