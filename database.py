import discord
from discord.ext import commands
from pymongo import MongoClient

# This defines the database class.
class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client.AdminBotDB
        self.ab_servers = self.db.servers

    # This pings the database.
    def ping_db(self):
        try:
            self.client.admin.command('ping')
            print("MongoDB has been successfully pinged!")
        except Exception as e:
            print(e)

    # This gets the ID for a given server.
    def get_id(self, guild):
        curr_server = self.ab_servers.find_one({'_id': guild.id})
        return curr_server['_id']
    
    # This gets the name for a given server.
    def get_name(self, guild):
        curr_server = self.ab_servers.find_one({'_id': guild.id})
        return curr_server['name']
    
    # This gets the prefix for a given server.
    def get_prefix(self, guild):
        curr_server = self.ab_servers.find_one({'_id': guild.id})
        return curr_server['prefix']

    # This sets the prefix for a given server.
    def set_prefix(self, ctx, prefix):
        curr_server = self.ab_servers.find_one({'_id': ctx.guild.id})
        self.ab_servers.update_one(curr_server, {'$set': {'prefix': prefix}})
    
    # This gets the welcome setting for a given server.
    def get_welcome(self, guild):
        curr_server = self.ab_servers.find_one({'_id': guild.id})
        return curr_server['welcome']
    
    # This sets the welcome setting for a given server.
    def set_welcome(self, ctx, welcome):
        curr_server = self.ab_servers.find_one({'_id': ctx.guild.id})
        self.ab_servers.update_one(curr_server, {'$set': {'welcome': welcome}})
    
    # This gets the welcome channel for a given server.
    def get_welc_channel(self, guild):
        curr_server = self.ab_servers.find_one({'_id': guild.id})
        return curr_server['welc_channel']

    # This sets the welcome channel for a given server.
    def set_welc_channel(self, ctx, channel_id):
        curr_server = self.ab_servers.find_one({'_id': ctx.guild.id})
        self.ab_servers.update_one(curr_server, {'$set': {'welc_channel':  channel_id}})

    # This gets the welcome message for a given server.
    def get_welc_msg(self, guild):
        curr_server = self.ab_servers.find_one({'_id': guild.id})
        return curr_server['welc_msg']
    
    # This sets the welcome message for a given server.
    def set_welc_msg(self, ctx, welc_msg):
        curr_server = self.ab_servers.find_one({'_id': ctx.guild.id})
        self.ab_servers.update_one(curr_server, {'$set': {'welc_msg':  welc_msg}})
    
    # This function adds a new Discord server to the DB.
    def add_server(self, guild):
        new_server = {}
        new_server["_id"] = guild.id
        new_server["name"] = guild.name
        new_server["prefix"] = "a!"
        new_server["welcome"] = False
        new_server["welc_channel"] = "default"
        new_server["welc_msg"] = "Welcome [mention] to [server]! We hope you enjoy your stay!"
        self.ab_servers.insert_one(new_server)

    # This function removes a Discord server from the DB.
    def remove_server(self, guild):
        self.ab_servers.delete_one({"_id": guild.id})
