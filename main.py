# Essential Imports.
import settings

# Discord imports.
import discord
from discord.ext import commands

def run():
    # His settings: DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")
    print(settings.token)
    print("done")

if __name__ == "__main__":
    run()
else:
    print("uhoh")

print('wtffff')