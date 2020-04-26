import discord
import discord.ext import commands
import os

bot = commands.Bot(command_prefix= "!")


token = os.environ.get('BOT_TOKEN')
bot.run(token)
