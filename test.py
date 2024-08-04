# This example requires the 'message_content' intent.

import discord
import random
import asyncio
from os import environ
import dotenv

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$goodbye'):
        await message.channel.send('Goodbye!')

    if message.content.startswith('$help'):
        await message.channel.send(f'Hello {message.author.name}, how can I assist you today?')

    if message.content.startswith('$roll'):
        dice_roll = random.randint(1, 6)
        await message.channel.send(f'You rolled a {dice_roll}!')

    if message.content.startswith('$flip'):
        coin_flip = 'heads' if random.choice([True, False]) else 'tails'
        await message.channel.send(f'The coin landed on {coin_flip}!')

    if message.content.startswith('countdown'):
        try:
            count = int(message.content.split()[1])
            if count > 0:
                for i in range(count, 0, -1):
                    await message.channel.send(i)
                    await asyncio.sleep(1)
                await message.channel.send('Time\'s up!')
            else:
                await message.channel.send('Please provide a positive integer for the countdown.')
        except (IndexError, ValueError):
            await message.channel.send('Please provide a valid number for the countdown.')

client.run(environ["DISCORD_BOT_TOKEN"])
