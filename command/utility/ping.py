from discord.ext import commands

from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _ping(bot: commands.Bot ,message: discord_akerno.ext.Message):
    await message.reply(f'Pong ! :ping_pong:\n`{round(bot.latency * 1000, 3)}`ms')

if __name__ == '__main__':
    ping = discord_akerno.Command
    ping.constructor(ping, "ping", "utility", "Le ping du bot", ['ping', 'ms', 'latency'])
    ping.execute(ping, _ping)
    ping.Push(ping)