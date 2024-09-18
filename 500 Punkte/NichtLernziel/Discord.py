import os

import discord

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run('MTI4NTg2OTAxMzY1MzUyMDQwNg.GfIxJ2.Yh7OK0-WajFZdRC3PN7LIAxVRiZFrhK3NFomw0')




