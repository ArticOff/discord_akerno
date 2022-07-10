
from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _purge(bot, message: discord_akerno.ext.Message):
    await message.channel.purge(limit=None, check=None)
    await message.channel.send(f'{message.author.mention} has purged the channel!')

if __name__ == '__main__':
    purge = discord_akerno.Command
    purge.constructor(purge, "purge", "moderation", "efface tout les messages", ['nuke'], "manage_messages", "manage_messages")
    purge.execute(purge, _purge)
    purge.Push(purge)
