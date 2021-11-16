# Discord Bot Enumerator 

Discord Bot Enumerator is a simple Python tool that allows users with a valid Discord bot token to enumerate data from the guilds that the bot is in.

In general, users can manually extract data from Discord guilds and channels if they manage to obtain an active bot token. This tool is just a wrapper around the discord.py library, which aims to automate the extraction process. 

**With a valid bot token, users can:**

* Enumerate guilds that the bot is in
* Enumerate channels within a specific guild
* Enumerate guild members **(NOT WORKING FOR NOW)**
* Read Messages sent in channels
* Create invite links to channels



# Bot Requirements

In order to enumerate data using a bot token, the bot itself needs to fulfill certain requirements:

* The token needs to be currently active

* The bot needs to have Administrator Permissions in the guild that it has joined
* To enumerate members, the bot needs to have the 'SERVER MEMBERS INTENT' Privileged Gateway Intent enabled



# Installation

* Discord Bot Enumerator works with Python 3.7+ (It was developed with Python 3.8.10)
* Some Python modules are required which are contained in `requirements.txt` and will be installed below

**Open your terminal and execute the following commands:**

```
# clone repo
git clone https://github.com/nisforrnicholas/Discord-Bot-Enumerator.git

# change working directory to discord-bot-enumerator 
cd Discord-Bot-Enumerator

# install requirements
pip3 install -r requirements.txt
```



# Usage

To enumerate guilds that the bot is in:

```
python3 dbe.py guilds BOT_TOKEN
```

To enumerate channels within a guild:

``````
python3 dbe.py channels GUILD_ID BOT_TOKEN
``````

To enumerate members within a guild:

``````
python3 dbe.py members GUILD_ID BOT_TOKEN
``````

To enumerate message history of a channel:

``````
# prints out latest 200 (default) messages in channel
python3 dbe.py messages GUILD_ID CHANNEL_ID BOT_TOKEN

# specify number of messages to print (eg: 50 messages)
python3 dbe.py messages -l 50 GUILD_ID CHANNEL_ID BOT_TOKEN
``````

To create invite link to a channel:

```
python3 dbe.py invites GUILD_ID CHANNEL_ID BOT_TOKEN
```
