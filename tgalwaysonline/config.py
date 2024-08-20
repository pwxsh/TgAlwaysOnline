import os
from dotenv import load_dotenv

load_dotenv()


API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME")
DELAY = os.getenv("DELAY")
