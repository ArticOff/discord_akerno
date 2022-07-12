# discord_akerno

### Akairo for Python !

The project is under development

## discord_akerno makes it easy for your robots to separate commands by file and move them by folder according to their category

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
    await bot.change_presence(activity=discord.Game(name="!help"))

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong ! {round(bot.latency * 1000)}ms")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Liste des commandes", description="", color=0x00ff00)
    embed.set_author(name="Akerno", icon_url="https://cdn.discordapp.com/avatars/724098984389058688/f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/724098984389058688/f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8.png")
    embed.add_field(name="!help", value="Affiche la liste des commandes", inline=False)
    embed.add_field(name="!ping", value="Affiche le ping du bot", inline=False)
    embed.add_field(name="!purgea", value="Efface tout les messages", inline=False)
    embed.add_field(name="!nuke", value="Efface tout les messages", inline=False)
    embed.add_field(name="!kick", value="Kick un utilisateur", inline=False)
    embed.add_field(name="!ban", value="Bannir un utilisateur", inline=False)
    embed.add_field(name="!unban", value="Unban un utilisateur", inline=False)
    embed.add_field(name="!mute", value="Mute un utilisateur", inline=False)
    embed.add_field(name="!unmute", value="Unmute un utilisateur", inline=False)
    embed.add_field(name="!say", value="Le bot dit quelque chose", inline=False)
    embed.add_field(name="!avatar", value="Affiche l'avatar d'un utilisateur", inline=False)
    embed.add_field(name="!userinfo", value="Affiche les informations d'un utilisateur", inline=False)
    embed.add_field(name="!serverinfo", value="Affiche les informations du serveur", inline=False)
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
5. Don't forget to import the discord_akerno module
6. Put the line to connect the bot to the module `AkernoClient(bot)`
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
