from importlib import machinery
discord_kairo = machinery.SourceFileLoader('discord_kairo','discord_kairo.py').load_module()

async def _kick(bot, message: discord_kairo.ext.Message):
    user = message.mentions[0]
    await message.channel.send(f'{user.mention} has been kicked for `{" ".join(str(message.content).split()[2:])}`!')
    await user.kick(reason=" ".join(str(message.content).split()[2:]))

if __name__ == '__main__':
    kick = discord_kairo.Command
    kick.constructor(kick, 'kick', 'moderation', 'Kick', ['expulser'])
    kick.execute(kick, _kick)
    kick.Push(kick)