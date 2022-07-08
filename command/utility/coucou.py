from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _coucou(bot, message: discord_akerno.ext.Message):
    # écrit ton code ici !
    await message.reply('Coucou ! :wave:')

if __name__ == '__main__':
    cc = discord_akerno.Command
    cc.constructor(cc, "coucou", "fun", "Coucou!", ['salut'])
    cc.execute(cc, _coucou)
    cc.Push(cc)
