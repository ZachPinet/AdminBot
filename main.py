import discord
from discord.ext import commands
import re

import settings
from database import Database
from help import HelpCog
from welcome import WelcomeCog
from miscellaneous import MiscCog
logger = settings.logging.getLogger("bot")
            
# This has the core functionalities of the bot.
def main():
    db = Database(settings.URI) # This initializes a db instance.
    db.ping_db()

    # This gets the server's prefix. It is called for every command.
    async def get_prefix(bot, message):
        if message:
            prefix = db.get_prefix(message.guild)
            return commands.when_mentioned_or(prefix)(bot, message)
        else:
            return commands.when_mentioned_or("a!")(bot, message)

    intents = discord.Intents.all()
    prefix = get_prefix
    bot = commands.Bot(command_prefix=prefix, intents=intents)
    bot.remove_command('help')
    bot.add_cog(HelpCog(bot, db))
    bot.add_cog(MiscCog(bot, db))
    bot.add_cog(WelcomeCog(bot, db))

    # This brings the bot online when the main function is run.
    @bot.event
    async def on_ready():
        print("Bot is online")
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    # This is called when the bot is added to a new server.
    @bot.event
    async def on_guild_join(guild):
        db.add_server(guild)

    # This is called when the bot leaves a server.
    @bot.event
    async def on_guild_remove(guild):
        db.remove_server(guild)

    # This sends a welcome message when a new user joins the server. 
    @bot.event
    async def on_member_join(member):
        if db.get_welcome(member.guild) == True:

            # This gets the proper welc_channel.
            def welcome_channel(channel_id, guild):
                # If the channel_id is a valid ID, it will be used.
                if isinstance(channel_id, int) == True:
                    welc_channel = bot.get_channel(channel_id)
                    if welc_channel is not None:
                        return welc_channel
            
                # Otherwise, the first valid channel is used instead.
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).send_messages == True:
                        if channel is not None:
                            return channel

            welc_msg = db.get_welc_msg(member.guild)
            channel_id = db.get_welc_channel(member.guild)
            welc_channel = welcome_channel(channel_id, member.guild)

            # This checks if each [channel ID] needs to be replaced.
            def replace_channels(welc_msg):
                pattern = r'\[(\d{10,})\]'
            
                def replace_match(match):
                    channel_id = int(match.group(1))
                    channel = bot.get_channel(channel_id)
                    if channel is None:
                        return match.group(0)
                    return bot.get_channel(channel_id).mention

                return re.sub(pattern, replace_match, welc_msg)

            # These replace substrings in the welcome message as needed.
            welc_msg = welc_msg.replace('[mention]', member.mention)
            welc_msg = welc_msg.replace('[server]', db.get_name(member.guild))
            welc_msg = replace_channels(welc_msg)

            await welc_channel.send(welc_msg)

    bot.run(settings.TOKEN)

if __name__ == "__main__":
    main()
