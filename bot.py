import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
import os

bot = commands.Bot(command_prefix="ch.")


bot.run(os.getenv("MAIN"))