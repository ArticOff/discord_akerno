from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _say(bot, message: discord_akerno.ext.Message):
    await message.delete()
    await message.channel.send(str(message.content).removeprefix('!say '))

if __name__ == '__main__':
    say = discord_akerno.Command
    say.constructor(say, 'say', 'utility', 'Say', ['dire'], 'manage_messages', 'None')
    say.execute(say, _say)
    say.Push(say)
