    import math
    from config import SUPPORT_CHAT, OWNER_ID
    from pyrogram.types import InlineKeyboardButton
    from Sifra.utils.formatters import time_to_seconds
    buttons = [
    [
    InlineKeyboardButton(
    text=_["P_B_1"],
    ),
    InlineKeyboardButton(
    text=_["P_B_2"],
    )
    ],
    [
    InlineKeyboardButton(
    text="🎧 𝐎𝐖𝐍𝐄𝐑 🎧", url=f"tg://openmessage?user_id={OWNER_ID}",
    ),
    InlineKeyboardButton(
    text="🏯 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🏯", url=SUPPORT_CHAT,
    )
    ],
    [
    InlineKeyboardButton(
    text=_["CLOSE_BUTTON"],
    callback_data=f"forceclose {videoid}|{user_id}",
    )
    ],
    ]
    return buttons
    duration_sec = time_to_seconds(dur)
    umm = math.floor(percentage)
    if 0 < umm <= 10:
    bar = "⎆╌╌╌╌╌╌╌╌"
    elif 10 < umm < 20:
    bar = "╌⎆╌╌╌╌╌╌╌"
    elif 20 <= umm < 30:
    bar = "╌╌⎆╌╌╌╌╌╌"
    elif 30 <= umm < 40:
    bar = "╌╌╌⎆╌╌╌╌╌"
    elif 40 <= umm < 50:
    bar = "╌╌╌╌⎆╌╌╌╌"
    elif 50 <= umm < 60:
    bar = "╌╌╌╌╌⎆╌╌╌"
    elif 60 <= umm < 70:
    bar = "╌╌╌╌╌╌⎆╌╌"
    elif 70 <= umm < 80:
    bar = "╌╌╌╌╌╌╌⎆╌"
    elif 80 <= umm < 95:
    bar = "╌╌╌╌╌╌╌╌⎆╌"
    else:
    bar = "╌╌╌╌╌╌╌╌╌⎆"
    buttons = [
    [
    InlineKeyboardButton(
    callback_data="GetTimer",
    )
    ],
    [
    InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
    InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
    InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
    ],
    [
    InlineKeyboardButton(
    text="🏯 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🏯", url=SUPPORT_CHAT,
    )
    ],
    [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons
    def stream_markup(_, chat_id):
    buttons = [
    [
    InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
    InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
    InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}")
    ],
    [
    InlineKeyboardButton(
    text="🎧 𝐎𝐖𝐍𝐄𝐑 🎧", url=f"tg://openmessage?user_id={OWNER_ID}",
    ),
    InlineKeyboardButton(
    text="🏯 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🏯", url=SUPPORT_CHAT,
    )
    ],
    [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons
    buttons = [
    [
    InlineKeyboardButton(
    text=_["P_B_1"],
    ),
    InlineKeyboardButton(
    text=_["P_B_2"],
    ),
    ],
    [
    InlineKeyboardButton(
    text=_["CLOSE_BUTTON"],
    callback_data=f"forceclose {videoid}|{user_id}",
    ),
    ],
    ]
    return buttons
    buttons = [
    [
    InlineKeyboardButton(
    text=_["P_B_3"],
    ),
    ],
    [
    InlineKeyboardButton(
    text=_["CLOSE_BUTTON"],
    callback_data=f"forceclose {videoid}|{user_id}",
    ),
    ],
    ]
    return buttons
    query = f"{query[:20]}"
    buttons = [
    [
    InlineKeyboardButton(
    text=_["P_B_1"],
    ),
    InlineKeyboardButton(
    text=_["P_B_2"],
    ),
    ],
    [
    InlineKeyboardButton(
    text="◁",
    ),
    InlineKeyboardButton(
    text=_["CLOSE_BUTTON"],
    callback_data=f"forceclose {query}|{user_id}",
    ),
    InlineKeyboardButton(
    text="▷",
    ),
    ],
    ]
    return buttons
