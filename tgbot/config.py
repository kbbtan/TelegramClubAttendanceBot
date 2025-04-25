"""
Defines global configuration variables for the bot.
Also loads any environment variables from a local .env file.
"""
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")