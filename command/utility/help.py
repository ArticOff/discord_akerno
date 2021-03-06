import json, discord

from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _help(bot, message: discord_akerno.ext.Message):
    await message.delete()
    if len(str(message.content).split()) > 1:
        category = str(message.content).split()[1]
        with open('akerno.commands.json', 'r') as f:
            try:
                commands = json.load(f)
                embed = discord.Embed(title=f'help [{"".join(category)}]', description='Liste des commandes', color=discord.Color.blue())
                for command in commands[category.lower()]:
                    embed.add_field(name=f"{command['name']} - ({', '.join(command['aliases'])})", value=f"{command['description']} - `{str(str(message.content).split()[0]).removesuffix('help')}{command['name']}`", inline=False)
                await message.channel.send(embed=embed)
            except KeyError:
                await message.channel.send(f'La catégorie `{category}` n\'existe pas!')
    else:
        await message.channel.send(f'```{message.content} moderation\n{message.content} utility\n{message.content} fun```')

if __name__ == '__main__':
    help = discord_akerno.Command
    help.constructor(help, "help", "utility", "The help command", ['help'], None, None)
    help.execute(help, _help)
    help.Push(help)
