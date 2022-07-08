from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _ban(bot, message: discord_akerno.ext.Message):
    user = message.mentions[0]
    await message.channel.send(f'{user.mention} has been banned for `{" ".join(str(message.content).split()[2:])}`!')
    await user.ban(reason=" ".join(str(message.content).split()[2:]))

if __name__ == '__main__':
    ban = discord_akerno.Command
    ban.constructor(ban, 'ban', 'moderation', 'Ban', ['degage'])
    ban.execute(ban, _ban)
    ban.Push(ban)
