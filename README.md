# discord_akerno

### Akairo for Python !

The project is under development

Attention, the framework is only in French 

## discord_akerno makes it easy for your robots to separate commands by file and move them by folder according to their category

## Features

### Dynamic commands.
- Creating commands from the file.
- Creating your own categories.
### Command Handling.
- Command aliases.
- Client and user permission checks.
### Blocking and monitoring messages.
- On a word
- For a user by ID
- For a user by name
- For a guild by ID
- For a guild by name
- For a channel by ID
- For a channel by name

## Quick Examples

### A bot without discord_akerno
```python
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

prefix = "!"
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot is ready !")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Liste des commandes", color=0x00ff00)
    embed.add_field(name="!ban", value="Bannir un utilisateur", inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} a été banni")

bot.run('token')
```

### A bot with discord_akerno
```python
import discord
from discord.ext import commands
from discord_akerno import AkernoClient

prefix = "!"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
AkernoClient(bot)

@bot.event
async def on_ready():
    print("Bot is ready !")
    await bot.change_presence(activity=discord.Game(name="!help"))

bot.run('token')
```

### Your bot will look like this

```
MySuperBot
├── akerno.commands.json
├── akerno.dirs.json
├── akerno.inhibitors.json
├── bot.py
├── discord_akerno.create.py
├── discord_akerno.py
└── command
    ├── fun
    │   ├── coucou.py
    │   └── dm.py
    ├── moderation
    │   ├── ban.py
    │   ├── clear.py
    │   ├── kick.py
    │   └── purge.py
    └── utility
        ├── botinfo.py
        ├── help.py
        ├── ping.py
        └── say.py
```

## How to install it ?

1. [Download Python](https://www.python.org/downloads/) (I recommend a recent version of Python)
2. [Download all files](https://github.com/ArticOff/discord_akerno/archive/refs/heads/main.zip)
3. Put them in a common folder
4. Put your bot
5. Don't forget to import the discord_akerno framework
6. Put the line to connect the bot to the framework `AkernoClient(bot)`
7. You're done !

## How to create a command ?

1. Open the file [discord_akerno.create.py](https://github.com/Help-Python-Group-FR/discord_akerno/blob/main/discord_akerno.create.py)
2. Fill in the options
3. Then run the file

***

- [The official discord server](https://discord.com/invite/h7YFnP45jv)
- [The github issues page](https://github.com/ArticOff/discord_akerno/issues)
- [Click here to download](https://github.com/ArticOff/discord_akerno/archive/refs/heads/main.zip)

Made with ❤️ by [Artic](https://discord.com/users/855783629047988274)
