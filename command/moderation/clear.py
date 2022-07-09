
from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _clear(bot, message: discord_akerno.ext.Message):
    await message.delete()
    if len(str(message.content).split()) > 1:
        try:
            await message.channel.purge(limit=int(str(message.content).split()[1]))
            await message.channel.send(f'`{str(message.content).split()[1]}` messages supprimés !')
        except ValueError:
            await message.channel.send('Veuillez entrer un nombre!')
    else:
        await message.channel.send('Veuillez entrer un nombre!')

if __name__ == '__main__':
    clear = discord_akerno.Command
    clear.constructor(clear, "clear", "moderation", "efface des messages", ['clear'], discord_akerno.ext.Permission.gerer_les_messages, discord_akerno.ext.Permission.gerer_les_messages)
    clear.execute(clear, _clear)
    clear.Push(clear)
