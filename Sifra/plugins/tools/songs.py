
import os
import re

import yt_dlp
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaAudio,
                            InputMediaVideo, Message)

from Sifra import YouTube, app
from Sifra.utils.decorators.language import language, languageCB
from Sifra.utils.formatters import convert_bytes



@app.on_message(
    & filters.group
    & ~BANNED_USERS
)
@language
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["SG_B_1"],
                ),
            ]
        ]
    )




@app.on_message(
    & filters.private
    & ~BANNED_USERS
)
@language
    await message.delete()
    url = await YouTube.url(message)
    if url:
        if not await YouTube.exists(url):
        (
            title,
            duration_min,
            duration_sec,
            thumbnail,
            vidid,
        ) = await YouTube.details(url)
        if str(duration_min) == "None":
            return await mystic.edit_text(
                )
            )
        await mystic.delete()
        return await message.reply_photo(
            thumbnail,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        if len(message.command) < 2:
    query = message.text.split(None, 1)[1]
    try:
        (
            title,
            duration_min,
            duration_sec,
            thumbnail,
            vidid,
        ) = await YouTube.details(query)
    except:
    if str(duration_min) == "None":
        return await mystic.edit_text(
        )
    await mystic.delete()
    return await message.reply_photo(
        thumbnail,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(
)
@languageCB
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    stype, vidid = callback_request.split("|")
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(
)
@languageCB
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    stype, vidid = callback_request.split("|")
    try:
    except:
        pass
    if stype == "audio":
        try:
            formats_available, link = await YouTube.formats(
                vidid, True
            )
        except:
        keyboard = InlineKeyboard()
        done = []
        for x in formats_available:
            check = x["format"]
            if "audio" in check:
                if x["filesize"] is None:
                    continue
                form = x["format_note"].title()
                if form not in done:
                    done.append(form)
                else:
                    continue
                sz = convert_bytes(x["filesize"])
                fom = x["format_id"]
                keyboard.row(
                    InlineKeyboardButton(
                        text=f"{form} Quality Audio = {sz}",
                    ),
                )
        keyboard.row(
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"close"
            ),
        )
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=keyboard
        )
    else:
        try:
            formats_available, link = await YouTube.formats(
                vidid, True
            )
        except Exception as e:
            print(e)
        keyboard = InlineKeyboard()
        done = [160, 133, 134, 135, 136, 137, 298, 299, 264, 304, 266]
        for x in formats_available:
            check = x["format"]
            if x["filesize"] is None:
                continue
            if int(x["format_id"]) not in done:
                continue
            sz = convert_bytes(x["filesize"])
            ap = check.split("-")[1]
            to = f"{ap} = {sz}"
            keyboard.row(
                InlineKeyboardButton(
                    text=to,
                )
            )
        keyboard.row(
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"close"
            ),
        )
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=keyboard
        )




@app.on_callback_query(
)
@languageCB
    try:
        await CallbackQuery.answer("Downloading")
    except:
        pass
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    stype, format_id, vidid = callback_request.split("|")
    yturl = f"https://www.youtube.com/watch?v={vidid}"
    with yt_dlp.YoutubeDL({"quiet": True}) as ytdl:
        x = ytdl.extract_info(yturl, download=False)
    title = (x["title"]).title()
    title = re.sub("\W+", " ", title)
    thumb_image_path = await CallbackQuery.message.download()
    duration = x["duration"]
    if stype == "video":
        thumb_image_path = await CallbackQuery.message.download()
        width = CallbackQuery.message.photo.width
        height = CallbackQuery.message.photo.height
        try:
            file_path = await YouTube.download(
                yturl,
                mystic,
                format_id=format_id,
                title=title,
            )
        except Exception as e:
        med = InputMediaVideo(
            media=file_path,
            duration=duration,
            width=width,
            height=height,
            thumb=thumb_image_path,
            caption=title,
            supports_streaming=True,
        )
        await app.send_chat_action(
            chat_id=CallbackQuery.message.chat.id,
            action=ChatAction.UPLOAD_VIDEO,
        )
        try:
            await CallbackQuery.edit_message_media(media=med)
        except Exception as e:
            print(e)
        os.remove(file_path)
    elif stype == "audio":
        try:
            filename = await YouTube.download(
                yturl,
                mystic,
                format_id=format_id,
                title=title,
            )
        except Exception as e:
        med = InputMediaAudio(
            media=filename,
            caption=title,
            thumb=thumb_image_path,
            title=title,
            performer=x["uploader"],
        )
        await app.send_chat_action(
            chat_id=CallbackQuery.message.chat.id,
            action=ChatAction.UPLOAD_AUDIO,
        )
        try:
            await CallbackQuery.edit_message_media(media=med)
        except Exception as e:
            print(e)
        os.remove(filename)
