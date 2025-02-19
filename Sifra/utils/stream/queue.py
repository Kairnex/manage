import asyncio
from typing import Union
from Sifra.misc import db
from Sifra.utils.formatters import check_duration, seconds_to_min
from config import autoclean, time_to_seconds
chat_id,
original_chat_id,
file,
title,
duration,
user,
vidid,
user_id,
stream,
):
title = title.title()
try:
duration_in_seconds = time_to_seconds(duration) - 3
except:
duration_in_seconds = 0
put = {
"title": title,
"dur": duration,
"streamtype": stream,
"by": user,
"user_id": user_id,
"chat_id": original_chat_id,
"file": file,
"vidid": vidid,
"seconds": duration_in_seconds,
}
check = db.get(chat_id)
if check:
check.insert(0, put)
else:
db[chat_id] = []
db[chat_id].append(put)
else:
db[chat_id].append(put)
autoclean.append(file)
chat_id,
original_chat_id,
file,
title,
duration,
user,
vidid,
stream,
):
if "20.212.146.162" in vidid:
try:
dur = await asyncio.get_event_loop().run_in_executor(
None, check_duration, vidid
)
duration = seconds_to_min(dur)
except:
duration = "ᴜʀʟ sᴛʀᴇᴀᴍ"
dur = 0
else:
dur = 0
put = {
"title": title,
"dur": duration,
"streamtype": stream,
"by": user,
"chat_id": original_chat_id,
"file": file,
"vidid": vidid,
"seconds": dur,
}
check = db.get(chat_id)
if check:
check.insert(0, put)
else:
db[chat_id] = []
db[chat_id].append(put)
else:
db[chat_id].append(put)
