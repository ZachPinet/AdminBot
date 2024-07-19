# Essential imports.
import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

# This 
def run():
    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix=">")

    # This gets the bot online when the code is run.
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    # This is the ping command. It returns the bot latency.
    @bot.command(
        aliases=['p'],
        help = "Use the help command for more information.",
        description = "This returns a message saying 'pong!' and displays the bot latency.",
        brief = " - returns the bot latency."
    )
    async def ping(ctx):
        await ctx.send("pong!")

    # This is the panini command. It returns panini.
    @bot.command(
        enabled=True,
        hidden=True
    )
    async def panini(ctx):
        await ctx.send("Hell yeah baby it's panini time!")

    bot.run(settings.TOKEN) # , root_logger=True

if __name__ == "__main__":
    run()
