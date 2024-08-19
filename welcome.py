from discord.ext import commands
import re

# This creates the Welcome cog to group together welcome commands.
class WelcomeCog(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    # This enables welcome messages on the server.
    @commands.command(aliases=['welcon', 'won'])
    @commands.has_permissions(administrator=True)
    async def welcomeon(self, ctx):
        if self.db.get_welcome(ctx.guild) == False:
            self.db.set_welcome(ctx, True)
            await ctx.send("Welcome messages have been enabled.")
        else:
            await ctx.send("Welcome messages are still enabled.")

    # This disables welcome messages on the server.
    @commands.command(aliases=['welcoff', 'woff'])
    @commands.has_permissions(administrator=True)
    async def welcomeoff(self, ctx):
        if self.db.get_welcome(ctx.guild) == True:
            self.db.set_welcome(ctx, False)
            await ctx.send("Welcome messages have been disabled.")
        else:
            await ctx.send("Welcome messages are still disabled.")

    # This changes the welcome message for the server.
    @commands.command(aliases=['setwelc', 'sw'])
    @commands.has_permissions(administrator=True)
    async def setwelcome(self, ctx):
        welc_msg = ctx.message.content
        welc_msg = re.split('setwelcome |setwelc |sw ', welc_msg)[1]
        self.db.set_welc_msg(ctx, welc_msg)
        await ctx.send("The server's welcome message has been updated.")

    # This sends the server's current welcome message .
    @commands.command(aliases=['viewwelc', 'vw'])
    @commands.has_permissions(administrator=True)
    async def viewwelcome(self, ctx):
        welc_msg = self.db.get_welc_msg(ctx.guild)

        # This checks each channel ID for validity before replacing it.
        def replace_channels(welc_msg):
            pattern = r'\[(\d{10,})\]'
            
            def replace_match(match):
                channel_id = int(match.group(1))
                channel = self.bot.get_channel(channel_id)
                if channel is None:
                    return match.group(0)
                return self.bot.get_channel(channel_id).mention

            return re.sub(pattern, replace_match, welc_msg)

        # These replace substrings in the welcome message as needed.
        welc_msg = welc_msg.replace('[mention]', ctx.message.author.mention)
        welc_msg = welc_msg.replace('[server]', self.db.get_name(ctx.guild))
        welc_msg = replace_channels(welc_msg)
        await ctx.send(welc_msg)

    # This sets the server's welcome channel if a valid ID is given.
    @commands.command(aliases=['swc'])
    @commands.has_permissions(administrator=True)
    async def setwelcomechannel(self, ctx):
        channel_id = ctx.message.content
        channel_id = int(re.split('setwelcomechannel |swc ', channel_id)[1])
        welc_channel = self.bot.get_channel(channel_id)
        
        if welc_channel is None:
            await ctx.send(f"Sorry, it seems like something is wrong with channel ID {channel_id}. Are you sure this is a valid ID?")
        else:
            self.db.set_welc_channel(ctx, channel_id)
            await ctx.send("The server's welcome channel has been updated.")
