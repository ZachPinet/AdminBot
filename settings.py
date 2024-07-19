import os
from dotenv import load_dotenv

# Loads the dotenv file.
load_dotenv()

# Gets the bot token stored in the dotenv file.
TOKEN = os.getenv('token')