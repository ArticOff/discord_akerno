# On importe les modules
import inspect, typing, discord, json, os
from discord.ext import commands as _commands

# On définit les variables d'auteur, de version et de description
__author__ = "Artic"
__version__ = "1.1.0"
__description__ = "En hommage à discord_akairo de discord.js, c'est un module qui fonctionne de la même façon."

def get_data(path: str):
    """
    Charge les données de la commande.
    """
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    return data

class ext:
    """
    La classe ext est une classe qui permet de définir les variables de l'extension et surtout les variables de discord.py.

    Mais vous pouvez utiliser discord.py directement.
    """
    Message = discord.Message
    Context = _commands.Context
    User = discord.User
    Member = discord.Member
    TextChannel = discord.TextChannel
    VoiceChannel = discord.VoiceChannel
    StageChannel = discord.StageChannel
    StoreChannel = discord.StoreChannel
    GroupChannel = discord.GroupChannel
    GroupCall = discord.GroupCall
    DMChannel = discord.DMChannel

class Command(object):
    """
    La classe Command est un objet qui permet de définir une commande.
    """
    def __new__(cls):
        """
        Permet de créer une commande.
        """
        return super(Command, cls).__new__(cls)
    
    def __init__(self):
        """
        Permet d'initialiser une commande.
        """
        name = name
        category = category
        description = description
        aliases = aliases

    def constructor(self, name: str, category: str, description: str, aliases: typing.Optional[list[str]]):
        """
        Cette fonction va contruire la commande.
        """
        self.name = name
        self.category = category
        self.description = description
        self.aliases = aliases
        self.filename = ''.join(os.path.splitext(os.path.basename(inspect.getmodule((inspect.stack()[1])[0]).__file__.removesuffix('.py'))))

    def execute(self, function: typing.Callable[[], typing.Any]):
        """
        Cette fonction va implémenter le code de votre commande.
        """
        self.function = function
        args = inspect.getfullargspec(function)[0]
        self.args = args

    def Push(self):
        """
        Cette fonction va ajouter la commande dans la base de donnée.
        """
        try:
            os.rename(f'command/{self.filename}.py', f'command/{self.category}/{self.filename}.py')
        except FileNotFoundError:
            pass
        self.path = f'{os.path.dirname(inspect.getmodule((inspect.stack()[1])[0]).__file__)}\\{self.filename}.py'
        command_info = {}
        command_info["filename"] = self.filename
        command_info["name"] = self.name
        command_info["category"] = self.category
        command_info["description"] = self.description
        command_info["aliases"] = self.aliases
        command_info["command"] = {}
        command_info["command"]["arguments"] = self.args
        command_info["command"]["function"] = self.function.__name__
        self.info = command_info
        type_info = self.category
        with open('kairo.commands.json', 'r+', encoding='utf-8') as file:
            _class = get_data('kairo.commands.json')
            for name in _class[type_info]:
                if name["name"] == self.name:
                    return False
            _class[type_info].append(command_info)
            file.seek(0)
            json.dump(_class, file, indent=4, separators=(',',': '), ensure_ascii=False)
        file.close()
        return print('Pushed !')
    
class CreateCommand:
    """
    Cette classe va vous permettre de configurer rapidement votre commande, plus qu'à écrire le code !
    """
    def __init__(self, name: str, category: str, description: str, aliases: typing.Optional[list[str]]):
        self.name = name.lower()
        self.category = category
        self.description = description
        self.aliases = aliases
        self.filename = ''.join(os.path.splitext(os.path.basename(inspect.getmodule((inspect.stack()[1])[0]).__file__.removesuffix('.py'))))
        if not os.path.exists(f'command/{self.category}'):
            categories = os.listdir('command')
            return print(f'Cette catégorie n\'existe pas ! [{"|".join(categories)}]')
        try:
            with open(f'{name}.py', 'x', encoding='utf-8') as fc:
                code = f"""
from importlib import machinery
discord_kairo = machinery.SourceFileLoader('discord_kairo','discord_kairo.py').load_module()

async def _{name}(bot ,message: discord_kairo.ext.Message):
    # écrit ton code ici !
    await message.reply('Coucou ! :wave:')

if __name__ == '__main__':
    {name} = discord_kairo.Command
    {name}.constructor({name}, "{name}", "{category}", "{description}", {aliases})
    {name}.execute({name}, _{name})
    {name}.Push({name})
"""
                fc.write(code)
                path = f'{os.path.dirname(inspect.getmodule((inspect.stack()[1])[0]).__file__)}\\{category}\\{name}.py'
                fc.close()
                os.rename(f'{name}.py', f'command/{category}/{name}.py')
        except FileExistsError:
            print(f'Cette commande existe déjà ! ({os.path.dirname(os.path.abspath(__file__))}\{category}\{name}.py)')
            return os.remove(f'{name}.py')
        print(f'Créé ! ({path})')
    
class Discord_kairo(_commands.Cog):
    """
    Le Cog à ajouter au bot pour relier le bot à l'extension Kairo.
    """
    def __init__(self, bot: _commands.Bot, mod_dir: str, uti_dir: str, fun_dir: str):
        """
        Ici, on récupère la variable bot.
        """
        commands = get_data('kairo.commands.json')
        self.mod_dir = mod_dir
        self.uti_dir = uti_dir
        self.fun_dir = fun_dir
        with open('kairo.dir.json', 'r+', encoding='utf-8') as file:
            dir = get_data('kairo.dir.json')
            dir["moderation"] = self.mod_dir
            dir["utility"] = self.uti_dir
            dir["fun"] = self.fun_dir
            file.write(json.dumps(dir, indent=4, separators=(',',': '), ensure_ascii=False))
        file.close()
        self.bot = bot
        self.commands = commands
        self.commands_moderation = commands["moderation"]
        self.commands_utility = commands["utility"]
        self.commands_fun = commands["fun"]

    @_commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """
        L'event on_message de discord.py est appelé lorsqu'un message est envoyé.
        """
        if message.author.bot:
            return
        if str(message.content).startswith(self.bot.command_prefix):
            for categories in os.listdir("./command"):
                for file in os.listdir(f"./command/{categories}"):
                    if file.endswith(".py"):
                        exec(f"from command.{categories}.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
            for cmd in self.commands_utility:
                if str(str(message.content).split()[0]).removeprefix("!") in cmd["aliases"] or str(str(message.content).split()[0]).replace(self.bot.command_prefix, '_') == f'_{cmd["name"]}':
                    return await eval("_{cmd}(self.bot, message)".format(cmd=str(cmd["name"]).removesuffix('\n')))
            for cmd in self.commands_moderation:
                if str(str(message.content).split()[0]).removeprefix("!") in cmd["aliases"] or str(str(message.content).split()[0]).replace(self.bot.command_prefix, '_') == f'_{cmd["name"]}':
                    return await eval("_{cmd}(self.bot, message)".format(cmd=str(cmd["name"]).removesuffix('\n')))
            for cmd in self.commands_fun:
                if str(str(message.content).split()[0]).removeprefix("!") in cmd["aliases"] or str(str(message.content).split()[0]).replace(self.bot.command_prefix, '_') == f'_{cmd["name"]}':
                    return await eval("_{cmd}(self.bot, message)".format(cmd=str(cmd["name"]).removesuffix('\n')))