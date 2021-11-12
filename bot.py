import discord
import threading
import asyncio

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

def start(token):
    loop = asyncio.get_event_loop()
    t = threading.Thread(target=loop.run_until_complete, args=[client.start(token)])
    t.start()

@client.event
async def on_ready():
   print('Successful connection. Token is valid!\nWe have logged in as: {0.user}\n'.format(client))

async def get_guilds():
    print('''\n============ GUILDS ============
(Name : Guild id : Member count)
''')
    guilds = '\n'.join([guild.name + " : " + str(guild.id) + " : " + str(guild.member_count) for guild in list(client.guilds)])
    print(guilds + "\n")
    await shutdown()

async def get_channels(guild_id):
    guild = client.get_guild(guild_id)
    channels = '\n'.join([channel.name + " : " + str(channel.id) + " : " + str(channel.type) for channel in guild.channels])
    print('''\n========= GUILD CHANNELS =========
(Name : Channel id : Channel type)
    ''')
    print(channels + "\n")
    await shutdown()

async def get_members(guild_id):
    guild = client.get_guild(guild_id)
    members = '\n'.join([member.name + " : " + str(member.id) + " : " + str(member.bot) for member in guild.members])
    print('''\n========= GUILD MEMBERS =========
(Name : Member id : is_bot)
    ''')
    print(members + "\n")
    await shutdown()

async def get_messages(guild_id, channel_id, limit=100):
    channel = client.get_guild(guild_id).get_channel(channel_id)
    message_hist = await channel.history(limit=limit).flatten()
    print(f'''\n=========== MESSAGES ===========
Message history from channel: {channel.name}
Latest message is at the top. Timestamps are in UTC
    ''')
    for i in message_hist:
        msg = await channel.fetch_message(i.id)
        print(str(msg.created_at) + "  " + i.author.name + " : " + msg.content)
    print("\n")
    await shutdown()

async def shutdown():
    await client.close()