import discord
import asyncio
import secreto


token = secreto.seu_token()
msg_id = None
msg_user = None

client = discord.Client()

@client.event
async def on_ready():
   await client.change_presence(game=discord.Game(name=" Power Disc | ?help"))
   print('olá Mundo!')
   print(client.user.name)
   print(client.user.id)
   print('-----BIRL-----')

@client.event
async def on_message(message):
  if message.content.lower().startswith('?teste'):
   await client.send_message(message.channel, '```olá Mundo!```')

client.run(token)
