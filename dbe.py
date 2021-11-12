import bot
import asyncio
import argparse
import time

def get_banner():
    return '''
██████╗ ██████╗ ███████╗   ██████╗ ██╗   ██╗
██╔══██╗██╔══██╗██╔════╝   ██╔══██╗╚██╗ ██╔╝
██║  ██║██████╔╝█████╗     ██████╔╝ ╚████╔╝ 
██║  ██║██╔══██╗██╔══╝     ██╔═══╝   ╚██╔╝  
██████╔╝██████╔╝███████╗██╗██║        ██║   
╚═════╝ ╚═════╝ ╚══════╝╚═╝╚═╝        ╚═╝   
    '''

if __name__=='__main__':
     # create the top-level parser
    parser = argparse.ArgumentParser(description='Discord Bot Enumerator',  epilog='Example Usages:\ndbe.py guilds <BOT TOKEN>\ndbe.py channels <GUILD ID> <BOT TOKEN>\ndbe.py members <GUILD ID> <BOT TOKEN>\ndbe.py messages <GUILD ID> <CHANNEL ID> <BOT TOKEN>\n ', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser._positionals.title = 'Commands'

    # create subparsers
    subparsers = parser.add_subparsers(dest='command', required=True)

    # create the parser for the "guilds" command
    parser_guilds = subparsers.add_parser('guilds', help='Enumerate guilds that bot is in. Use "guilds -h" for help')
    parser_guilds.add_argument('token', help='Specify valid bot token')

    # create the parser for the "channel" command
    parser_channels = subparsers.add_parser('channels', help='Enumerate channels in guild. Use "channels -h" for help')
    parser_channels.add_argument('guild_id', type=int, help='Specify valid guild ID')
    parser_channels.add_argument('token', help='Specify valid bot token')

    # create the parser for the "channel" command
    parser_members = subparsers.add_parser('members', help='Enumerate members in guild. Use "members -h" for help')
    parser_members.add_argument('guild_id', type=int, help='Specify valid guild ID')
    parser_members.add_argument('token', help='Valid Bot Token')

    # create the parser for the "channel" command
    parser_messages = subparsers.add_parser('messages', help='Enumerate messages in channel. use "messages -h" for help')
    parser_messages.add_argument('guild_id', type=int, help='Valid Guild ID')
    parser_messages.add_argument('channel_id', type=int, help='Valid Channel ID')
    parser_messages.add_argument('token', help='Valid Bot Token')
    parser_messages.add_argument('-l', '--limit', type=int, help='Specify message history limit (Default: 200)')

    # parse arguments
    args = parser.parse_args()
    
    print(get_banner() + "\nConnecting to Discord Servers...\n")
    # connect to discord servers
    bot.start(args.token)
    time.sleep(5)
    
    loop = asyncio.get_event_loop()

    if args.command == 'guilds':
        asyncio.run_coroutine_threadsafe(bot.get_guilds(), loop)

    if args.command == 'channels':
        asyncio.run_coroutine_threadsafe(bot.get_channels(args.guild_id), loop)

    if args.command == 'members':
        asyncio.run_coroutine_threadsafe(bot.get_members(args.guild_id), loop)

    if args.command == 'messages':
        if args.limit:
            asyncio.run_coroutine_threadsafe(bot.get_messages(args.guild_id, args.channel_id, args.limit), loop)
        else:
            asyncio.run_coroutine_threadsafe(bot.get_messages(args.guild_id, args.channel_id), loop)


    