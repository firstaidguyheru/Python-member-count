import discord
from discord.ext import commands
from asyncio import sleep
import os
from dotenv import load_dotenv


load_dotenv()



intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', help_command=None, intents=intents)


@client.event
async def on_member_join(member):
	await sleep(60*10)
	for channel in member.guild.channels:
		if channel.name.startswith('Member'):
			await channel.edit(name=f'Members: {member.guild.member_count}')
			break






client.run(os.getenv("TOKEN"))