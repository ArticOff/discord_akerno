from importlib import machinery
discord_kairo = machinery.SourceFileLoader('discord_kairo','discord_kairo.py').load_module()

async def _coucou(bot, message: discord_kairo.ext.Message):
    # écrit ton code ici !
    await message.reply('Coucou ! :wave:')

if __name__ == '__main__':
    cc = discord_kairo.Command
    cc.constructor(cc, "coucou", "fun", "Coucou!", ['salut'])
    cc.execute(cc, _coucou)
    cc.Push(cc)
