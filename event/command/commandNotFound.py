from discord.ext import commands

from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _commandNotFound(bot, ctx: commands.Context, error):
    return await ctx.reply('Command not found.')

if __name__ == '__main__':
    commandNotFound = discord_akerno.Event
    commandNotFound.constructor(commandNotFound, "command", "commandNotFound", "commandNotFound")
    commandNotFound.execute(commandNotFound, _commandNotFound)
    commandNotFound.Push(commandNotFound)
