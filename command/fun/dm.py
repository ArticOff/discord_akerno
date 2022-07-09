from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _dm(bot, message: discord_akerno.ext.Message):
    await message.delete()
    await message.channel.send(f'{message.author.mention} has been dm!')
    await message.author.send(str(message.content).removeprefix('!dm '))

if __name__ == '__main__':
    dm = discord_akerno.Command
    dm.constructor(dm, 'dm', 'fun', 'DM', ['mp'], None, None)
    dm.execute(dm, _dm)
    dm.Push(dm)
