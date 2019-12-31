import nest_asyncio; nest_asyncio.apply()
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '++')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    
client.run('NjYxNDI1ODQ0NzUyNzQ0NDQ5.XgrQAA.bITZyFyYkK2WAsruCaBu9167fbU')