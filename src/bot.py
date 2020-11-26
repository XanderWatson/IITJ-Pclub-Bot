import discord
import datetime
import random

client = discord.Client()

symbol = '$'


@client.event
async def on_message(message):
    global symbol
    message.content = message.content.lower()
    if message.author == client.user:
        return

    if message.content.startswith(symbol + 'time'):
        await message.channel.send(str(datetime.datetime.now()))

    elif message.content.startswith(symbol + 'set'):
        content = message.content.split()
        if len(content) <= 1:
            await message.channel.send('Please enter a symbol. Usage "<current symbol>set <new symbol>"')
        else:
            symbol = content[1]
            await message.channel.send(f'The new symbol has been set to "{symbol}"')

    elif message.content.startswith(symbol):
        await message.channel.send('Hello This bot has been called')

client.run('')
