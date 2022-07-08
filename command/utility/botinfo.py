import discord
from discord.ext import commands

from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _botinfo(bot: commands.Bot ,message: discord_akerno.ext.Message):
    await message.delete()
    embed = discord.Embed(title="Bot Info", description="The open source bot", color=discord.Color.green())
    embed.add_field(name="Name", value=f'`{bot.user.name}`', inline=True)
    embed.add_field(name="ID", value=f'`{bot.user.id}`', inline=True)
    embed.add_field(name="Version", value="`1.0.0`", inline=True)
    embed.add_field(name="Author", value="`The Discord Server`", inline=False)
    embed.add_field(name="Prefix", value=f'`{bot.command_prefix}`', inline=True)
    embed.add_field(name="Guilds", value=f'`{len(bot.guilds)}`', inline=True)
    embed.add_field(name="Users", value=f'`{len(set(bot.get_all_members()))}`', inline=True)
    embed.add_field(name="Extention", value=f"`discord_akerno {discord_akerno.__version__}`", inline=False)
    return await message.channel.send(embed=embed)
    
if __name__ == '__main__':
    botinfo = discord_akerno.Command
    botinfo.constructor(botinfo, "botinfo", "utility", "Les informations du bot", ['botinfo', 'bot.info'])
    botinfo.execute(botinfo, _botinfo)
    botinfo.Push(botinfo)
