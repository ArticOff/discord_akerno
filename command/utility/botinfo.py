import discord
from discord.ext import commands

from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _botinfo(bot: commands.Bot, message: discord_akerno.ext.Message):
    await message.delete()
    embed = discord.Embed(title="Bot Info", description="Le bot open source", color=discord.Color.green())
    embed.add_field(name="Tag", value=f'`{bot.user.name}#{bot.user.discriminator}`', inline=True)
    embed.add_field(name="ID", value=f'`{bot.user.id}`', inline=True)
    embed.add_field(name="Version", value="`1.0.0`", inline=True)
    embed.add_field(name="Auteur", value="[`The Discord Server`](https://discord.gg/kNNa8P3Ajy)", inline=False)
    embed.add_field(name="Préfix", value=f'`{bot.command_prefix}`', inline=True)
    embed.add_field(name="Serveurs", value=f'`{len(bot.guilds)}`', inline=True)
    embed.add_field(name="Nombre d'utilisateurs", value=f'`{len(set(bot.get_all_members()))}`', inline=True)
    embed.add_field(name="Extention", value=f"`discord_akerno {discord_akerno.__version__}`", inline=False)
    return await message.channel.send(embed=embed)
    
if __name__ == '__main__':
    botinfo = discord_akerno.Command
    botinfo.constructor(botinfo, "botinfo", "utility", "Les informations du bot", ['botinfo', 'bot.info'], None, None)
    botinfo.execute(botinfo, _botinfo)
    botinfo.Push(botinfo)
