from discord.ext import commands

# This creates the Welcome cog to group together welcome commands.
class HelpCog(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    # This is the help command. It shows detailed info about the bot.
    @commands.command(aliases=['h'])
    async def help(self, ctx):
        p = self.db.get_prefix(ctx.guild)
        help1 = ("## Here is a list of commands:\n"
        "### Misc Commands:\n"
        f"**{p}help [h]**: Displays this help message.\n"
        f"**{p}ping [p]**: Returns the bot latency.\n"
        f"**{p}checkserver [cs]**: Gets all stored info about the server.\n"
        f"**{p}setprefix [sp]**: Sets a new command prefix for the server.\n"
        "### Welcome Commands:\n"
        f"**{p}welcomeon [won]**: Enables welcome messages on the server.\n"
        f"**{p}welcomeoff [woff]**: Disables welcome messages on the server.\n"
        f"**{p}setwelcome [sw]**: Sets a new welcome message for the server.\n"
        f"**{p}viewwelcome [vw]**: Sends a preview of the welcome message.\n"
        f"**{p}setwelcomechannel [swc]**: Sets the channel using its ID.")
        await ctx.send(help1)
        