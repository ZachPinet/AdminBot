from discord.ext import commands
import discord
import re

# This creates the Misc cog to group together welcome commands.
class MiscCog(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    # This is the ping command. It returns the bot latency.
    @discord.app_commands.command(name="ping", description="Check the bot's latency")
    async def ping(self, interaction: discord.Interaction):
        latency = int((self.bot.latency * 1000) + 0.5)
        await interaction.response.send_message(f"pong! ({latency}ms)")
    
    # This checks if the server is in the DB, and adds it if it's not.
    @commands.command(aliases=['check', 'cs'])
    async def checkserver(self, ctx):
        try:
            curr_server = self.db.ab_servers.find_one({"_id": ctx.guild.id})
        except:
            await ctx.send("Server not found in database! Adding it now...")
            self.db.add_server(ctx)
            curr_server = self.db.ab_servers.find_one({"_id": ctx.guild.id})
        
        # This sends a message with all the saved info about the server.
        cs_msg = ""
        for key, value in curr_server.items():
            cs_msg += f"**{key}**: {value}\n"
        await ctx.send(cs_msg[:-2])

    # This command changes the prefix for the server.
    @commands.command(aliases=["sp", "prefixset", "ps"])
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx):
        prefix = ctx.message.content
        prefix = re.split('setprefix |sp |prefixset |ps ', prefix)[1]

        # This ends the command if the new prefix is the current one.
        if prefix == self.db.get_prefix(ctx.guild):
            await ctx.send(f"The prefix is already '{prefix}'.")
            return
        
        # These make sure the prefix is valid.
        valid_prefix = True
        valid_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_',
                       '=', '+', ',', '<', '.', '>', '/', '?', '`', '~']

        if len(prefix) > 5:
            valid_prefix = False
            await ctx.send("New prefix too long! Must have 5 or fewer characters.")

        for x in prefix:
            if x.isalnum() == False and x not in valid_chars:
                valid_prefix = False
                await ctx.send("New prefix not valid! Unknown symbol used.")
                return
        
        # This updates the prefix if it is valid.
        if valid_prefix  == True:
            self.db.set_prefix(ctx, prefix)
            await ctx.send(f"Server prefix updated! Prefix is now '{prefix}'.")

    # This is the panini command. It returns panini.
    @commands.command()
    async def panini(self, ctx):
        await ctx.send("Hell yeah baby it's panini time!")
