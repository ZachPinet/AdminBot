import os
from dotenv import load_dotenv

# Loads the dotenv file.
load_dotenv()

# Gets the private information stored in the dotenv file.
TOKEN = os.getenv('TOKEN')
TESTTOKEN = os.getenv('TESTTOKEN')
DBUSER =  os.getenv('DBUSER')
DBPASSWORD = os.getenv('DBPASSWORD')
CLUSTERSTRING = os.getenv('CLUSTERSTRING')
URI = f"mongodb+srv://{DBUSER}:{DBPASSWORD}@{CLUSTERSTRING}.mongodb.net/?retryWrites=true&w=majority"
