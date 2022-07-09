
from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _coucou(bot, message: discord_akerno.ext.Message):
    await message.reply('Coucou ! :wave:')

if __name__ == '__main__':
    coucou = discord_akerno.Command
    coucou.constructor(coucou, "coucou", "fun", "hey", ['salut', 'hey'], None, None)
    coucou.execute(coucou, _coucou)
    coucou.Push(coucou)
