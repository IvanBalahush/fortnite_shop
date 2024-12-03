import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
FORTNITE_API_KEY=os.getenv("FORTNITE_API_KEY")
FORTNITE_API_URL=os.getenv("FORTNITE_API_URL")

if not TELEGRAM_BOT_TOKEN or not FORTNITE_API_URL or not FORTNITE_API_KEY:
    raise EnvironmentError("Not all environment variables are set")
