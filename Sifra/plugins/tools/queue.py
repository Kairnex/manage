import asyncio
import os

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message

import config
from Sifra import app
from Sifra.misc import db
from Sifra.utils.decorators.language import language, languageCB
from config import BANNED_USERS

basic = {}


def get_image(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"
    else:
        return config.YOUTUBE_IMG_URL


    if "index_" in file_path or "live_" in file_path:
        return "Unknown"
    if duration_seconds == 0:
        return "Unknown"
    else:
        return "Inline"


@app.on_message(
    & filters.group
    & ~BANNED_USERS
)
@language
    if message.command[0][0] == "c":
        chat_id = await get_cmode(message.chat.id)
        if chat_id is None:
            return await message.reply_text(_["setting_7"])
        try:
            await app.get_chat(chat_id)
        except:
    else:
        chat_id = message.chat.id
    if not await is_active_chat(chat_id):
        return await message.reply_text(_["general_5"])
    got = db.get(chat_id)
    if not got:
    file = got[0]["file"]
    videoid = got[0]["vidid"]
    user = got[0]["by"]
    title = (got[0]["title"]).title()
    typo = (got[0]["streamtype"]).title()
    DUR = get_duration(got)
    if "live_" in file:
        IMAGE = get_image(videoid)
    elif "vid_" in file:
        IMAGE = get_image(videoid)
    elif "index_" in file:
        IMAGE = config.STREAM_IMG_URL
    else:
        if videoid == "telegram":
            IMAGE = (
                config.TELEGRAM_AUDIO_URL
                if typo == "Audio"
                else config.TELEGRAM_VIDEO_URL
            )
            IMAGE = config.SOUNCLOUD_IMG_URL
        else:
            IMAGE = get_image(videoid)
    upl = (
        if DUR == "Unknown"
            _,
            DUR,
            videoid,
            got[0]["dur"],
        )
    )
    basic[videoid] = True
    mystic = await message.reply_photo(IMAGE, caption=cap, reply_markup=upl)
    if DUR != "Unknown":
        try:
            while db[chat_id][0]["vidid"] == videoid:
                await asyncio.sleep(5)
                if await is_active_chat(chat_id):
                    if basic[videoid]:
                            try:
                                    _,
                                    DUR,
                                    videoid,
                                    db[chat_id][0]["dur"],
                                )
                                await mystic.edit_reply_markup(reply_markup=buttons)
                            except FloodWait:
                                pass
                        else:
                            pass
                    else:
                        break
                else:
                    break
        except:
            return


@app.on_callback_query(filters.regex("GetTimer") & ~BANNED_USERS)
async def quite_timer(client, CallbackQuery: CallbackQuery):
    try:
        await CallbackQuery.answer()
    except:
        pass


@languageCB
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    what, videoid = callback_request.split("|")
    try:
    except:
        return
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_5"], show_alert=True)
    got = db.get(chat_id)
    if not got:
    if len(got) == 1:
    await CallbackQuery.answer()
    basic[videoid] = False
    med = InputMediaPhoto(
        media="https://telegra.ph//file/6f7d35131f69951c74ee5.jpg",
    )
    await CallbackQuery.edit_message_media(media=med)
    j = 0
    msg = ""
    for x in got:
        j += 1
        if j == 1:
            msg += f'Streaming :\n\n✨ Title : {x["title"]}\nDuration : {x["dur"]}\nBy : {x["by"]}\n\n'
        elif j == 2:
        else:
            msg += f'✨ Title : {x["title"]}\nDuration : {x["dur"]}\nBy : {x["by"]}\n\n'
        if len(msg) < 700:
            await asyncio.sleep(1)
            return await CallbackQuery.edit_message_text(msg, reply_markup=buttons)
        if "✨" in msg:
            msg = msg.replace("✨", "")
        link = await AyanoBin(msg)
        await CallbackQuery.edit_message_media(media=med, reply_markup=buttons)
    else:
        await asyncio.sleep(1)
        return await CallbackQuery.edit_message_text(msg, reply_markup=buttons)


@languageCB
    callback_data = CallbackQuery.data.strip()
    try:
    except:
        return
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_5"], show_alert=True)
    got = db.get(chat_id)
    if not got:
    await CallbackQuery.answer(_["set_cb_5"], show_alert=True)
    file = got[0]["file"]
    videoid = got[0]["vidid"]
    user = got[0]["by"]
    title = (got[0]["title"]).title()
    typo = (got[0]["streamtype"]).title()
    DUR = get_duration(got)
    if "live_" in file:
        IMAGE = get_image(videoid)
    elif "vid_" in file:
        IMAGE = get_image(videoid)
    elif "index_" in file:
        IMAGE = config.STREAM_IMG_URL
    else:
        if videoid == "telegram":
            IMAGE = (
                config.TELEGRAM_AUDIO_URL
                if typo == "Audio"
                else config.TELEGRAM_VIDEO_URL
            )
            IMAGE = config.SOUNCLOUD_IMG_URL
        else:
            IMAGE = get_image(videoid)
    upl = (
        if DUR == "Unknown"
            _,
            DUR,
            videoid,
            got[0]["dur"],
        )
    )
    basic[videoid] = True

    med = InputMediaPhoto(media=IMAGE, caption=cap)
    mystic = await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
    if DUR != "Unknown":
        try:
            while db[chat_id][0]["vidid"] == videoid:
                await asyncio.sleep(5)
                if await is_active_chat(chat_id):
                    if basic[videoid]:
                            try:
                                    _,
                                    DUR,
                                    videoid,
                                    db[chat_id][0]["dur"],
                                )
                                await mystic.edit_reply_markup(reply_markup=buttons)
                            except FloodWait:
                                pass
                        else:
                            pass
                    else:
                        break
                else:
                    break
        except:
            return
