import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Sifra import LOGGER, app, userbot
from Sifra.core.call import Ayano
from Sifra.misc import sudo
from Sifra.plugins import ALL_MODULES
from Sifra.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Sifra.plugins" + all_module)
    LOGGER("Sifra.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴀʟʟ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await Ayano.start()
    try:
        await Ayano.stream_call("https://telegra.ph/file/f59799c8d94c4691939a4.mp4")
    except NoActiveGroupCall:
        LOGGER("Sifra").error(
            "ᴠᴄ ᴛᴏ ᴏɴ ᴋʀ ʟᴇ ᴘᴇʜʟᴇ ғɪʀ ᴅᴇᴘʟᴏʏ ᴋʀ..."
        )
        exit()
    except:
        pass
    await Ayano.decorators()
    LOGGER("Sifra").info(
        "ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ, ᴀᴀʙ ᴄʜᴀɴɴᴇʟ Jᴏɪɴ ᴋʀ ʟᴇ @PAHADI_VERSE"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Sifra").info("ᴍᴀᴀ ᴄʜᴜᴅᴀ ᴍᴀɪɴ ʙᴏᴛ ʙᴀɴᴅ ᴋᴀʀ ʀʜᴀ Sifra Mᴜsɪᴄ Bᴏᴛ...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
