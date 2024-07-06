import requests
import discord
from os.path import join, dirname
from dotenv import load_dotenv
import time
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client=client)

