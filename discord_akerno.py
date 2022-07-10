# On importe les modules
import inspect, typing, discord, json, os
from discord.ext import commands as _commands

# On définit les variables d'auteur, de version et de description
__author__ = "Artic"
__version__ = "1.4.2"
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
    CategoryChannel = discord.CategoryChannel

    class Permission:
        """
        Les vraibles de permission.
        """
        creer_une_invitation = 'create_instant_invite'
        expulser_des_membres = 'kick_members'
        bannir_des_membres = 'ban_members'
        administrateur = 'administrator'
        gerer_les_salons = 'manage_channels'
        gerer_le_serveur = 'manage_guild'
        ajouter_des_reactions = 'add_reactions'
        voir_les_logs_du_serveur = 'view_audit_log'
        voix_prioritaire = 'priority_speaker'
        video = 'stream'
        voir_les_salons = 'view_channel'
        envoyer_des_messages = 'send_messages'
        envoyer_des_messages_de_syntèse_vocale = 'send_tts_messages'
        gerer_les_messages = 'manage_messages'
        integrer_des_liens = 'embed_links'
        joindre_des_fichiers = 'attach_files'
        voir_les_anciens_messages = 'read_message_history'
        mentionner_des_membres = 'mention_everyone'
        utiliser_les_emojis_externes = 'use_external_emojis'
        utiliser_les_emojis = 'use_emojis'
        se_connecter = 'connect'
        parler = 'speak'
        rendre_les_membres_muets = 'mute_members'
        mettre_en_sourdine_des_membres = 'deafen_members'
        deplacer_des_membres = 'move_members'
        utiliser_la_detection_de_la_voix = 'use_vad'
        changer_le_pseudo = 'change_nickname'
        gerer_les_pseudos = 'manage_nicknames'
        gerer_les_roles = 'manage_roles'
        gerer_les_webhooks = 'manage_webhooks'
        gerer_les_emojis_et_les_autocollants = 'manage_emojis_and_stickers'
        utiliser_les_commandes_de_application = 'use_application_commands'
        gerer_les_evenements = 'manage_events'
        gerer_les_fils = 'manage_threads'
        creer_des_fils_publics = 'create_public_threads'
        creer_des_fils_privés = 'create_private_threads'
        utiliser_des_autocollants_externes = 'use_external_stickers'
        envoyer_des_messages_dans_les_fils = 'send_messages_in_threads'
        utiliser_les_activites = 'use_embedded_activities'
        exclure_temporairement_des_membres = 'moderate_members'


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

    def constructor(self, name: str, category: str, description: str, aliases: typing.Optional[list[str]], permissionUser: str = None, permissionBot: str = None):
        """
        Cette fonction va contruire la commande.
        """
        self.name = name
        self.category = category
        self.description = description
        self.aliases = aliases
        self.filename = ''.join(os.path.splitext(os.path.basename(inspect.getmodule((inspect.stack()[1])[0]).__file__.removesuffix('.py'))))
        self.permissionBot = permissionBot.lower() if permissionBot else None
        self.permissionUser = permissionUser.lower() if permissionUser else None

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
        command_info["permission"] = {}
        command_info["permission"]["bot"] = self.permissionBot
        command_info["permission"]["user"] = self.permissionUser
        self.info = command_info
        type_info = self.category
        with open('akerno.commands.json', 'r+', encoding='utf-8') as file:
            _class = get_data('akerno.commands.json')
            for name in _class[type_info]:
                if name["name"] == self.name:
                    print(f'La commande {self.name} se trouve déjà dans la base de donnée !')
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
    def __init__(self, name: str, category: str, description: str, aliases: typing.Optional[list[str]], permissionUser: str = None, permissionBot: str = None):
        self.name = name.lower()
        self.category = category
        self.description = description
        self.aliases = aliases
        self.filename = ''.join(os.path.splitext(os.path.basename(inspect.getmodule((inspect.stack()[1])[0]).__file__.removesuffix('.py'))))
        self.permissionBot = permissionBot.lower() if permissionBot else None
        self.permissionUser = permissionUser.lower() if permissionUser else None
        if not os.path.exists(f'command/{self.category}'):
            categories = os.listdir('command')
            return print(f'Cette catégorie n\'existe pas ! [{"|".join(categories)}]')
        try:
            with open(f'{name}.py', 'x', encoding='utf-8') as fc:
                code = f"""
from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _{name}(bot, message: discord_akerno.ext.Message):
    # écrit ton code ici !
    await message.reply('Coucou ! :wave:')

if __name__ == '__main__':
    {name} = discord_akerno.Command
    {name}.constructor({name}, "{name}", "{category}", "{description}", {aliases}, "{permissionUser if permissionUser else None}", "{permissionBot if permissionBot else None}")
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

class Discord_akerno(_commands.Cog):
    """
    Le Cog à ajouter au bot pour relier le bot à l'extension akerno.
    """
    def __init__(self, bot: _commands.Bot):
        """
        Ici, on récupère la variable bot.
        """
        commands = get_data('akerno.commands.json')
        categories = os.listdir('command')
        self.categories = categories
        with open('akerno.dir.json', 'r+', encoding='utf-8') as file:
            dirs = get_data('akerno.dir.json')
            dirs = {}
            for category in categories:
                dirs[category] = category
                file.seek(0)
            json.dump(dirs, file, indent=4, separators=(',',': '), ensure_ascii=False)
        file.close()
        with open('akerno.commands.json', 'r+', encoding='utf-8') as file:
            _class = get_data('akerno.commands.json')
            for category in categories:
                if category not in _class:
                    _class[category] = []
            file.seek(0)
            json.dump(_class, file, indent=4, separators=(',',': '), ensure_ascii=False)
        file.close()
        for category in categories:
            if category not in commands:
                commands[category] = []
            else:
                pass
        file.close()
        self.bot = bot
        self.commands = commands

    @_commands.Cog.listener()
    async def on_ready(self):
        for categories in os.listdir("./command"):
            for file in os.listdir(f"./command/{categories}"):
                if file.endswith(".py"):
                    cmd_ = []
                    for command in self.commands[categories]:
                        cmd_.append(command["name"])
                    if file.replace(".py", "") in cmd_:
                        pass
                    else:
                        print(f'{file} n\'a pas été trouvé dans la base de donnée !')
                    
    @_commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """
        L'event on_message de discord.py est appelé lorsqu'un message est envoyé.
        """
        if message.author.bot:
            return
        with open('akerno.inhibitors.json', 'r+', encoding='utf-8') as file:
            inhibitors = get_data('akerno.inhibitors.json')
            if message.author.id in inhibitors["user"]:
                return
            if message.guild.id in inhibitors["guild"]:
                return
            if message.channel.id in inhibitors["channel"]:
                return
            for word in inhibitors["word"]:
                if word in message.content.lower():
                    return
        file.close()
        if str(message.content).startswith(self.bot.command_prefix):
            for categories in os.listdir("./command"):
                for file in os.listdir(f"./command/{categories}"):
                    if file.endswith(".py"):
                        exec(f"from command.{categories}.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
            for _class_ in self.commands:
                for cmd in self.commands[_class_]:
                    if str(str(message.content).split()[0]).removeprefix("!") in cmd["aliases"] or str(str(message.content).split()[0]).replace(self.bot.command_prefix, '_') == f'_{cmd["name"]}':
                        permissionUser = [perm[0] for perm in message.author.guild_permissions if perm[1]]
                        if cmd["permission"]["user"] in permissionUser or cmd["permission"]["user"] == "none":
                            try:
                                return await eval("_{cmd}(self.bot, message)".format(cmd=str(cmd["name"]).removesuffix('\n')))
                            except discord.Forbidden:
                                return await message.reply(f'Je n\'ai pas le permission d\'effectuer cette commande !\npermission: `{cmd["permission"]["bot"]}`')
                        else:
                            return await message.reply(f'Vous n\'avez pas le permission d\'effectuer cette commande !\npermission: `{cmd["permission"]["user"]}`')

    @_commands.Cog.listener()
    async def on_command_error(self, ctx: _commands.Context, error: _commands.CommandError):
        """
        Pour éviter les spams dans la console, on utilise l'event on_command_error de discord.py.
        """
        return

class AkernoClient:
    """
    Cette classe va vous permettre de configurer rapidement votre bot, plus qu'à écrire le code !
    """
    def __init__(self, bot: _commands.Bot):
        self.intents = bot.intents.all()
        self.prefix = bot.command_prefix
        self.bot = bot
        self.akerno = Discord_akerno(self.bot)
        self.bot.add_cog(self.akerno)
