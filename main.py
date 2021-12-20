import discord
from discord.ext import commands,tasks
import logging,os,json
from itertools import cycle
from flask import Flask
from threading import Thread

logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename="discord.log",encoding="utf-8",mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s"))
logger.addHandler(handler)

def get_prefix(client,message):
    with open("prefix.json","r") as f:
        prefix = json.load(f)
    return prefix[str(message.guild.id)]

#class Help(commands.HelpCommand):

    #def __init__(self):
        #super().__init__()

    #async def send_bot_help(self,mapping):
        #return await super().send_bot_help(mapping)

    #async def send_cog_help(self,cog):
        #return await super().send_cog_help(cog)

    #async def send_group_help(self,group):
        #return await super().send_group_help(group)

    #async def send_command_help(self,command):
        #return await super().send_command_help(command)

client = commands.Bot(
    command_prefix = get_prefix,
    #help_command = Help(),
    description = "Loop of Hernie, by Hernie\nReport bugs on Git through -git"
)

status = cycle([" with -help!"," with your emotions!"," 0.3.0 Alpha!"," by thine own hand!"," with 99.98% uptime!"," with Wumpus!"])
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(
        status = discord.Status.dnd,
        activity = discord.Game(next(status))
    )

@client.event
async def on_ready():
    change_status.start()

app = Flask("")
@app.route("/")
def home():
    return "Loop"
def run():
    app.run(host="0.0.0.0",port=8080)
def ping():
    Thread(target=run).start()

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

ping()
client.run(os.getenv("key"))