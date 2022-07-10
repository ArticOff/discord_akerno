from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _kick(bot, message: discord_akerno.ext.Message):
    user = message.mentions[0]
    await message.channel.send(f'{user.mention} has been kicked for `{" ".join(str(message.content).split()[2:])}`!')
    await user.kick(reason=" ".join(str(message.content).split()[2:]))

if __name__ == '__main__':
    kick = discord_akerno.Command
    kick.constructor(kick, 'kick', 'moderation', 'Kick', ['expulser'], 'kick_members', 'kick_members')
    kick.execute(kick, _kick)
    kick.Push(kick)
