from importlib import machinery
discord_kairo = machinery.SourceFileLoader('discord_kairo','discord_kairo.py').load_module()

async def _dm(bot, message: discord_kairo.ext.Message):
    await message.delete()
    await message.channel.send(f'{message.author.mention} has been dm!')
    await message.author.send(str(message.content).removeprefix('!dm '))

if __name__ == '__main__':
    dm = discord_kairo.Command
    dm.constructor(dm, 'dm', 'fun', 'DM', ['mp'])
    dm.execute(dm, _dm)
    dm.Push(dm)
    
