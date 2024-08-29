import os

from dotenv import load_dotenv


load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
DELAY = float(os.getenv("DELAY")) or 60
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
SESSION_NAME = "TgAlwaysOnline"
