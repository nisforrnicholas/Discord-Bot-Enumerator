import discord
import threading
import asyncio
from discord.ext import commands
from colorama import init, Fore, Style

init()

intents = discord.Intents.default()
intents.members = False

client = discord.Client(intents=intents)

def start(token):
    loop = asyncio.get_event_loop()
    t = threading.Thread(target=loop.run_until_complete, args=[client.start(token)])
    t.start()

@client.event
async def on_ready():
   print('Successful connection. Token is valid!\nWe have logged in as: ' + Fore.RED + '{0.user}\n'.format(client) + Style.RESET_ALL)

async def get_guilds():
    print('''\n============ GUILDS ============
(Name : Guild id : Member count)
''')
    guilds = '\n'.join([Fore.GREEN + guild.name + Style.RESET_ALL + " : " + str(guild.id) + " : " + str(guild.member_count) for guild in list(client.guilds)])
    print(guilds + "\n")
    await shutdown()

async def get_channels(guild_id):
    guild = client.get_guild(guild_id)
    if guild.me.guild_permissions.administrator or guild.me.guild_permissions.view_channel:
        channels = '\n'.join([Fore.GREEN + channel.name + Style.RESET_ALL + " : " + str(channel.id) + " : " + str(channel.type) for channel in guild.channels])
        print('''\n========= GUILD CHANNELS =========
(Name : Channel id : Channel type)
        ''')
        print(f"[ Channels in: {guild.name} ]")
        print(channels + "\n")
    else:
        print(f'''\n========= GUILD CHANNELS =========
        
[ Bot does not have 'View Channels' permissions on {guild.name} ]
        ''')
    await shutdown()

async def get_members(guild_id):
    guild = client.get_guild(guild_id)
    members = '\n'.join([Fore.GREEN + member.name + Style.RESET_ALL + " : " + str(member.id) + " : " + str(member.bot) for member in guild.members])
    print('''\n========= GUILD MEMBERS =========
(Name : Member id : is_bot)
    ''')
    print(f"[ Members in: {guild.name} ]")
    print(members + "\n")
    await shutdown()

async def get_messages(guild_id, channel_id, limit=200):
    guild = client.get_guild(guild_id)
    if (guild.me.guild_permissions.administrator or guild.me.guild_permissions.read_message_history) and guild.me.guild_permissions.view_channel:
        channel = guild.get_channel(channel_id)
        message_hist = await channel.history(limit=limit).flatten()
        print(f'''\n=========== MESSAGES ==========
Latest message is at the top. Timestamps are in UTC.

[ Message history from channel: {channel.name} ]
        ''')
        for i in message_hist:
            msg = await channel.fetch_message(i.id)
            print(Fore.CYAN + str(msg.created_at) + Style.RESET_ALL + "  " + Fore.GREEN + i.author.name + Style.RESET_ALL + " : " + msg.content)
        print("\n")
    else:
        print(f'''\n=========== MESSAGES ===========

[ Bot does not have 'Read Message History' permissions on {guild.name} ]
        ''')
    await shutdown()

async def create_invites(guild_id, channel_id):
    guild = client.get_guild(guild_id)
    if guild.me.guild_permissions.administrator or guild.me.guild_permissions.create_instant_invite:
        channel = guild.get_channel(channel_id)
        discord_server_invite = await channel.create_invite()
        print(f'''\n=========== Invites ===========
[ Creating invite for channel: {channel.name} ]
        ''')
        print("Invite Link: " + Fore.GREEN + str(discord_server_invite) + Style.RESET_ALL)
    else:
        print(f'''\n=========== Invites ===========

[ Bot does not have 'Create Instant Invite' permissions on {guild.name} ]
        ''')
    await shutdown()

async def shutdown():
    print("Task done. Closing connection...\n")
    await client.close()