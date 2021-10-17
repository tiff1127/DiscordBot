#todo : add in inserter to insert command

import discord
import os
import io
import aiohttp
import secrets
from datetime import datetime
from dotenv import load_dotenv
from discord.utils import get

#List of images
imageLink = ['https://i.imgur.com/NAMy3Da.jpg','https://i.imgur.com/PckEk9m.jpg','https://i.imgur.com/nO9aKVP.jpg','https://i.imgur.com/8b1uL7J.jpg','https://i.imgur.com/Woheash.jpg']
nightImageLink = ['https://i.imgur.com/78NwZNe.jpg','https://i.imgur.com/kCcFtdn.jpg','https://i.imgur.com/7Kq9v6j.png','https://i.imgur.com/sahjAnc.jpg']
simpImage = ['untitled.png','image0.png']

#get client from discord
client = discord.Client()

#event decerator
#registering an event
@client.event
async def on_ready():
	#getting username '0' replaces with 'client'
	print('Started hehe {0.user}'.format(client))

#if a message sends in server(from anyone)
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.lower().startswith('I love you'.lower()):
		emoji = client.get_emoji(725164098979102760)
		await message.add_reaction(emoji)
		await message.channel.send('I love you too <3')

	if message.content.startswith('nsimp'):
		await message.channel.send(file=discord.File(secrets.choice(simpImage)))

	if message.content.startswith('nshuaige'):
		await message.channel.send(file=discord.File('pepeeyes.png'))

	if message.content.startswith('ndrunk'):
		file = discord.File('pepeeyes.png')
		await message.channel.send('???????????? IM ALCOHOL FREE BUT IM DRUNK',file = file)

	if message.content.startswith('nskem'):
		await message.channel.send(file=discord.File('images.jpg'))

	if message.content.startswith('nreact'):
		emoji = client.get_emoji(725164098979102760)
		await message.add_reaction(emoji)
		emoji = '\N{SLIGHTLY SMILING FACE}'
		await message.add_reaction(emoji)
		emoji = '\N{PILE OF POO}'
		await message.add_reaction(emoji)
		emoji = client.get_emoji(819934714664190002)
		await message.add_reaction(emoji)


	if message.content.startswith('Hi'):
		await message.channel.send('Hi MATE')

	if message.content == 'nmorning':
		async with aiohttp.ClientSession() as session:
			async with session.get(secrets.choice(imageLink)) as resp:
				if resp.status != 200:
					print('Could not download file... [image error]')
					return await channel.send('Error :\'<')
				data = io.BytesIO(await resp.read())
				await message.channel.send(file=discord.File(data, 'morning.jpg'))

	if message.content == 'nnight':
		async with aiohttp.ClientSession() as session:
			async with session.get(secrets.choice(nightImageLink)) as resp:
				if resp.status != 200:
					print('Could not download file... [image error]')
					return await channel.send('Error :\'<')
				data = io.BytesIO(await resp.read())
				await message.channel.send(file=discord.File(data, 'morning.jpg'))

	if message.content == 'nmorninggif':
		async with aiohttp.ClientSession() as session:
			async with session.get('https://i.postimg.cc/cH4HD2LX/15330893807631864.gif') as resp:
				if resp.status != 200:
					print('Could not download file... [image error]')
					return await channel.send('Error :\'<')
				data = io.BytesIO(await resp.read())
				#picture = discord.File(data)
				await message.channel.send(file=discord.File(data, 'smth.gif'))

	#if message.content.startswith('nmorning1'):
	#	async with aiohttp.ClientSession() as session:
	#		async with session.get('https://i.imgur.com/PckEk9m.jpg') as resp:
	#			if resp.status != 200:
	#				return await channel.send('Could not download file...')
	#			data = io.BytesIO(await resp.read())
	#			await message.channel.send(file=discord.File(data, 'cool_image.jpg'))

	#if message.content.startswith('nmorning2'):
	#	async with aiohttp.ClientSession() as session:
	#		async with session.get('https://i.imgur.com/nO9aKVP.jpg') as resp:
	#			if resp.status != 200:
	#				return await channel.send('Could not download file...')
	#			data = io.BytesIO(await resp.read())
	#			await message.channel.send(file=discord.File(data, 'cool_image.jpg'))

	#if message.content.startswith('nmorning3'):
	#	async with aiohttp.ClientSession() as session:
	#		async with session.get('https://i.imgur.com/8b1uL7J.jpg') as resp:
	#			if resp.status != 200:
	#				return await channel.send('Could not download file...')
	#			data = io.BytesIO(await resp.read())
	#			await message.channel.send(file=discord.File(data, 'cool_image.jpg'))

	#if message.content.startswith('nmorning4'):
	#	async with aiohttp.ClientSession() as session:
	#		async with session.get('https://i.imgur.com/Woheash.jpg') as resp:
	#			if resp.status != 200:
	#				return await channel.send('Could not download file...')
	#			data = io.BytesIO(await resp.read())
	#			await message.channel.send(file=discord.File(data, 'cool_image.jpg'))

	if message.content.startswith('nniubi'):
		async with aiohttp.ClientSession() as session:
			async with session.get('https://i.imgur.com/lIQieq1.jpg') as resp:
				if resp.status != 200:
					return await channel.send('Could not download file...')
				data = io.BytesIO(await resp.read())
				await message.channel.send(file=discord.File(data, 'cool_image.jpg'))

	if message.content.startswith('nhehe'):
		async with aiohttp.ClientSession() as session:
			async with session.get('https://i.postimg.cc/Lsh4LfCb/he-hehe.gif') as resp:
				if resp.status != 200:
					return await channel.send('Could not download file...')
				data = io.BytesIO(await resp.read())
				await message.channel.send(file=discord.File(data, 'cool_image.gif'))

	if message.content.startswith('nroneno'):
		await message.channel.send(file=discord.File('roneno.jpg'))

	if message.content.startswith('nnoods'):
		await message.channel.send(file=discord.File('noods.jpg'))

@client.event
async def on_reaction_add(reaction,user):
	if user == client.user:
		return

	#can get reaction.message.author to get the user sent
	mention = user.mention
	if reaction.message == "I love you too <3":
		await message.channel.send('{mention} Lub U')

#@client.event
#async def on_message_delete(message):
#	if message.author == client.user:
#		return

#	deletedmsg = message.content
#	await message.channel.send(deletedmsg)


load_dotenv('.env')
client.run(os.environ.get('TOKEN'))