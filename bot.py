import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user.name}")

@client.event
async def on_message(message):
    if message.author == client.user: return;
    if message.content.startswith("!내일시간표"):
        await message.channel.send("내가 그걸 어떻게 알아")
    if message.content.startswith("!너누구야"):
        await message.channel.send("글자 못읽어? 개구리다!")

client.run(TOKEN)