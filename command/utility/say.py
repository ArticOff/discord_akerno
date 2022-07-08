from importlib import machinery
discord_kairo = machinery.SourceFileLoader('discord_kairo','discord_kairo.py').load_module()

async def _say(bot, message: discord_kairo.ext.Message):
    await message.delete()
    await message.channel.send(str(message.content).removeprefix('!say '))

if __name__ == '__main__':
    say = discord_kairo.Command
    say.constructor(say, 'say', 'utility', 'Say', ['dire'])
    say.execute(say, _say)
    say.Push(say)