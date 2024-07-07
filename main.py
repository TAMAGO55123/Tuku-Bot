import requests
import discord
from os.path import join, dirname
from dotenv import load_dotenv
import time
import os
import json

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("API_KEY")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client=client)

username="Houjiy_"

@client.event
async def on_ready():
    print('ログインしました')
    await tree.sync()

@tree.command(name='test', description="テストコマンドです。何もありません。")
async def test_command(interation:discord.Interaction):
    await interation.response.send_message("テストコマンドか実行されました。")

@tree.command(name='tuku', description=''.join(['つく(',username,')の情報を返します。']))
async def tuku(interation:discord.Interaction):
    followers = requests.get(''.join(['https://api.scratch.mit.edu/users/',username,'/followers']))
    followers_data = json.loads(followers.text)
    followers_data3 = len(followers_data)

    userdata = requests.get(''.join(['https://api.scratch.mit.edu/users/',username]))
    userdata_data1 = json.loads(userdata.text)
    #userdata_data2 = userdata_data1['id']
    #userdata_icon = ''.join(['https://cdn2.scratch.mit.edu/get_image/user/',userdata_data2,'_90x90.png?v='])

    embed1=discord.Embed(title="ユーザー詳細", color=0xF8AA36, description=f"ユーザ名:{username}\nフォロワー数:{str(followers_data3)}", url=''.join(['https://scratch.mit.edu/users/',username]))
    #embed1.set_thumbnail(url=userdata_icon)
    await interation.response.send_message(embed=embed1)

try:
    client.run(TOKEN)
except:
    os.system("kill 1")



