import os
from os import getenv

API_ID = int(os.environ.get("22865155", ""))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("e430e3f61712616b926be959f1612c46", "")
BOT_TOKEN = os.environ.get("8705907823:AAHoOY-XXIctxTffXDPjTnLH7vYmnypEmxM", "")

OWNER_ID = int(os.environ.get("8453406690", ""))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("8453406690", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("mongodb+srv://adarshppandey937:uIoPcln9vXQBF0vP@cluster0.o9mn6hb.mongodb.net/?", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("-1003570183030", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("8453406690", "")  # Optional here you'll get all logs
