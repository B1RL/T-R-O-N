import discord
import token

token = token.seu_token()
msg_id = None
msg_user = None
client = discord.Client()
players = {}

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=" Power Disc | !help"))
    print(client.user.name)
    print('BOT ONLINE')


@client.event
async def on_message(message):
    if message.content.startswith('?conectar'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, 'Você precisa estar conectado em um canal de voz!')
        except Exception as error:
            await client.send_message(message.channel, "Um Erro foi encontrado: ```{error}```".format(error=error))

    if message.content.startswith('?desconectar'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, 'O bot não está conectado em nenhum canal de voz!')
        except Exception as Hugo:
            await client.send_message(message.channel, "Um Erro foi encontrado: ```{haus}```".format(haus=Hugo))

    if message.content.startswith('?play'):
        try:
            if client.is_voice_connected(message.server):
                link = message.content[6:]
                voice = client.voice_client_in(message.server)
                player = await voice.create_ytdl_player("ytsearch:{}".format(link))
                players[message.server.id] = player
                player.start()
                await client.send_message(message.channel, "🎶 | **A musica pedida está sendo reproduzida**")
        except:
                await client.send_message(message.channel, 'Erro ao reproduzir a música.')


client.run(token)
