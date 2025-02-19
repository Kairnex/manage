from Sifra.core.bot import Ayano
from Sifra.core.dir import dirr
from Sifra.core.git import git
from Sifra.core.userbot import Userbot
from Sifra.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Ayano()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
