import discord

from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _on_ready(bot, ):
    print('Ready !')
    await bot.change_presence(activity=discord.Game(name="!help"))

if __name__ == '__main__':
    on_ready = discord_akerno.Event
    on_ready.constructor(on_ready, "client", "on_ready", "ready")
    on_ready.execute(on_ready, _on_ready)
    on_ready.Push(on_ready)
