# MIT License
# Copyright (c) 2022 Muhammed
import os, re
search = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Creator
CREATOR_NAME = os.environ.get("CREATOR_NAME", "")
CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "")

# Account
API_HASH = os.environ.get("API_HASH", "d0faa85d88a5307ce9aef4fe996ad739")
API_ID = os.environ.get("API_ID", "8118043")
# About Bot
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7588854401:AAEdCQD3-HHmz-sRI-v7jhlUoc352-7mYf4")
PICS = os.environ.get("PICS", "https://telegra.ph/file/89c0411ecab4dbe6cd507.jpg")
# Database
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://JD2021:JD2021@cluster0.zweu4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME ", "Telegram_files")

# Chats & Users
ADMINS = os.environ.get("ADMINS", "846646879")
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "")
AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1002525990761  -1002554856643" )
CHANNELS = [int(ch) if search.search(ch) else ch for ch in os.environ.get("CHANNELS", "-1002634731434"]
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002299074293")
GET_FILECHANNEL = os.environ.get("GET_FILECHANNEL", "")
FILTER_DEL_SECOND = int(os.environ.get("FILTER_DEL_SECOND", "3600"))
IMDB = is_enabled((os.environ.get('IMDB', "True")), True)
CUSTOM_FILE_CAPTION = os.environ.get("CUSTOM_FILE_CAPTION", "")
# AutoFilter
AUTH_GROUPS = os.environ.get("AUTH_GROUPS", "")
AUTH_USERS = [int(user) if search.search(user) else user for user in os.environ.get('AUTH_USERS', '739667270').split()]
FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "5")
PROTECT_FILES = is_enabled((os.environ.get('PROTECT_FILES', "True")), True) 

## EXTRA FEATURES ##
    
# URL Shortener

URL_SHORTENR_WEBSITE = os.environ.get('URL_SHORTENR_WEBSITE', '')
URL_SHORTNER_WEBSITE_API = os.environ.get('URL_SHORTNER_WEBSITE_API', '')
