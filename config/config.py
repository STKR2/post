import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff  -----------------------

API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
BOT_TOKEN = getenv("BOT_TOKEN", "5204315005:AAGPX3ySLQZkvVcLHc7n1N_u0NFJUOHN0lw")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgBp-a0RLvxLtoGMo-lobfwZyjqGKYzTqPWU3_Wn29Rg-dH8wNftfw3VXfrVeM7tdBriw6-xpJLqLOynF-7TyY8gkls2Vi6ILsKtTq2bKkg_iqrNfw51l_kDp6LmK4-cjRF2mm-wEzN-o05_paVXhd1Z7UIAUZZFodEnjZQ8hHrXS77x-NSQE06TuoBRrQXao5xZG2bw8lEbDjetLWIptr7jUDJaxoikSBQjpN0ypXBloy_71kTlNvy2TwIN8-6bqsJti6q4iKgGWm0TRtith_BuF_IS5uBiBhidt89IxOofnqC4tnZpbEtxX6kfqKKnzarHJQvDu_1dn1pvQTR-vn61AAAAAUM3evYA")
BOT_USERNAME = getenv("BOT_USERNAME", "Saiadjabot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "1854384004").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001847569598")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates 🍃 & Music bot name________________
NETWORK = getenv("NETWORK", "xl444")
GROUP = getenv("GROUP", "xl444")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff ****************************

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg")

aiohttpsession = aiohttp.ClientSession()


