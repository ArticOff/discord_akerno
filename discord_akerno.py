# On importe les modules
import inspect, typing, discord, json, os, datetime
from discord.ext import commands as _commands

# On définit les variables d'auteur, de version et de description
__author__ = "Artic"
__version__ = "1.5.0"
__description__ = "En hommage à discord_akairo de discord.js, c'est un framework qui fonctionne de la même façon."

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
        Les variables de permission.
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
    
    class EventName:
        """
        Les variables de nom d'event.
        """
        commandNotFound = 'commandNotFound'
        missingRequiredArgument = 'missingRequiredArgument'
        missingPermissions = 'missingPermissions'
        botMissingPermissions = 'botMissingPermissions'
        badArgument = 'badArgument'
        cooldown = 'cooldown'
        commandInvokeError = 'commandInvokeError'
        checkFailure = 'checkFailure'
        
        memberJoin = 'memberJoin'
        memberLeave = 'memberLeave'
        memberBan = 'memberBan'
        memberUnban = 'memberUnban'
        memberKick = 'memberKick'
        memberUpdate = 'memberUpdate'
        typing = 'typing'
        messageDelete = 'messageDelete'
        messageEdit = 'messageEdit'
        reactionAdd = 'reactionAdd'
        reactionRemove = 'reactionRemove'
        reactionClear = 'reactionClear'
        webhooksUpdate = 'webhookUpdate'
        userUpdate = 'userUpdate'
        guildJoin = 'guildJoin'
        guildLeave = 'guildLeave'
        guildUpdate = 'guildUpdate'
        roleCreate = 'roleCreate'
        roleUpdate = 'roleUpdate'
        roleDelete = 'roleDelete'
        guildAvailable = 'guildAvailable'
        guildUnavailable = 'guildUnavailable'
        voiceStateUpdate = 'voiceStateUpdate'
        inviteCreate = 'inviteCreate'
        inviteDelete = 'inviteDelete'
        groupJoin = 'groupJoin'
        groupLeave = 'groupLeave'
        relationshipAdd = 'relationshipAdd'
        relationshipRemove = 'relationshipRemove'
        relationshipUpdate = 'relationshipUpdate'
        guildIntegrationsUpdate = 'guildIntegrationsUpdate'
        guildChannelPinsUpdate = 'guildChannelPinsUpdate'
        privateChannelCreate = 'privateChannelCreate'
        privateChannelDelete = 'privateChannelDelete'
        privateChannelUpdate = 'privateChannelUpdate'
        privateChannelPinsUpdate = 'privateChannelPinsUpdate'
        bulkMessageDelete = 'bulkMessageDelete'
        connect = 'connect'
        disconnect = 'disconnect'
        resumed = 'resumed'
        shardConnect = 'shardConnect'
        shardDisconnect = 'shardDisconnect'
        shardResumed = 'shardResumed'
        on_ready = 'on_ready'


    class EventArg:
        """
        Les variables d'argument d'event.
        """
        error = 'error'
        guild = 'guild'
        member = 'member'
        context = 'ctx'
        reaction = 'reaction'
        message = 'message'
        user = 'user'
        channel = 'channel'
        webhook = 'webhook'
        invite = 'invite'
        role = 'role'
        group = 'group'
        before = 'before'
        after = 'after'
        relationship = 'relationship'
        last_pin = 'last_pin'
        messages = 'messages'
        shard_id = 'shard_id'
        reactions = 'reactions'
        when = 'when'

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
    
class Event(object):
    def __new__(cls):
        """
        Permet de créer un event.
        """
        return super(Command, cls).__new__(cls)
    
    def __init__(self):
        """
        Permet d'initialiser un event.
        """
        name = name
        category = category
        description = description
        aliases = aliases
    
    def execute(self, function: typing.Callable[[], typing.Any]):
        """
        Cette fonction va implémenter le code de votre event.
        """
        self.function = function
        args = inspect.getfullargspec(function)[0]
        self.args = args

    def constructor(self, category: str, name: str, event: str):
        """
        Cette fonction va contruire l'event.
        """
        self.name = name
        self.event = event
        self.category = category
        self.filename = ''.join(os.path.splitext(os.path.basename(inspect.getmodule((inspect.stack()[1])[0]).__file__.removesuffix('.py'))))
    
    def Push(self):
        """
        Cette fonction va ajouter l'event dans la base de donnée.
        """
        try:
            os.rename(f'{self.filename}.py', f'{self.category}/{self.filename}.py')
        except FileNotFoundError:
            pass
        self.path = f'{os.path.dirname(inspect.getmodule((inspect.stack()[1])[0]).__file__)}\\{self.filename}.py'
        event_info = {}
        event_info["filename"] = self.filename
        event_info["category"] = self.category
        event_info["name"] = self.name
        event_info["event"] = self.event
        event_info["function"] = {}
        event_info["function"]["arguments"] = self.args
        event_info["function"]["name"] = self.function.__name__
        self.info = event_info
        with open('akerno.events.json', 'r+', encoding='utf-8') as file:
            _class = get_data('akerno.events.json')
            for event in _class[self.category]:
                if event["name"] == self.name:
                    print(f'L\'event {self.name} se trouve déjà dans la base de donnée !')
                    return False
            _class[self.category].append(event_info)
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

class CreateEvent:
    """
    Cette classe va vous permettre de configurer rapidement votre commande, plus qu'à écrire le code !
    """
    def __init__(self, name: str, category: str, event: str, args: list[str] = None):
        self.name = name
        self.category = category
        self.event = event
        self.filename = ''.join(os.path.splitext(os.path.basename(inspect.getmodule((inspect.stack()[1])[0]).__file__.removesuffix('.py'))))
        if not os.path.exists(f'event/{self.category}'):
            categories = os.listdir('command')
            return print(f'Cette catégorie n\'existe pas ! [{"|".join(categories)}]')
        try:
            with open(f'{name}.py', 'x', encoding='utf-8') as fc:
                code = f"""
from importlib import machinery
discord_akerno = machinery.SourceFileLoader('discord_akerno','discord_akerno.py').load_module()

async def _{name}(bot, {", ".join(args)}):
    # écrit ton code ici !
    print('Coucou !')

if __name__ == '__main__':
    {name} = discord_akerno.Event
    {name}.constructor({name}, "{category}", "{name}", "{event}")
    {name}.execute({name}, _{name})
    {name}.Push({name})
"""
                fc.write(code)
                path = f'{os.path.dirname(inspect.getmodule((inspect.stack()[1])[0]).__file__)}\\{category}\\{name}.py'
                fc.close()
                os.rename(f'{name}.py', f'event/{category}/{name}.py')
        except FileExistsError:
            print(f'Cette commande existe déjà ! ({os.path.dirname(os.path.abspath(__file__))}\{category}\{name}.py)')
            return os.remove(f'{name}.py')
        print(f'Créé ! ({path})') 

class Discord_akerno(_commands.Cog):
    """
    Le Cog à ajouter au bot pour relier le bot à l'extension akerno.
    """
    def __init__(self, bot: _commands.Bot, eventDIR: str):
        """
        Ici, on récupère la variable bot.
        """
        self.eventDIR = eventDIR
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
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.on_ready:
                return await eval(f"_{filename}(self.bot)")
        return
                    
    @_commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """
        L'event on_message de discord.py est appelé lorsqu'un message est envoyé.
        """
        if message.author.bot:
            return
        with open('akerno.inhibitors.json', 'r+', encoding='utf-8') as file:
            inhibitors = get_data('akerno.inhibitors.json')
            if message.author.id in inhibitors["userID"]:
                return
            if message.guild.id in inhibitors["guildID"]:
                return
            if message.channel.id in inhibitors["channelID"]:
                return
            for word in inhibitors["word"]:
                if word in message.content.lower():
                    return
            for username in inhibitors["userName"]:
                if username in message.author.name:
                    return
            for guildname in inhibitors["guildName"]:
                if guildname in message.guild.name:
                    return
            for channelname in inhibitors["channelName"]:
                if channelname in message.channel.name:
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
                                __cmd__ = str(cmd['name']).removesuffix('\n')
                                return await eval(f"_{__cmd__}(self.bot, message)")
                            except discord.Forbidden:
                                return await message.reply(f'Je n\'ai pas le permission d\'effectuer cette commande !\npermission: `{cmd["permission"]["bot"]}`')
                        else:
                            return await message.reply(f'Vous n\'avez pas le permission d\'effectuer cette commande !\npermission: `{cmd["permission"]["user"]}`')

    @_commands.Cog.listener()
    async def on_command_error(self, ctx: _commands.Context, error: _commands.CommandError):
        """
        Pour éviter les spams dans la console, on utilise l'event on_command_error de discord.py.
        """
        for file in os.listdir(f"./event/command"):
            if file.endswith(".py"):
                exec(f"from event.command.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/command'):
            filename = file.removesuffix('.py')
            if isinstance(error, _commands.CommandNotFound) and filename == ext.EventName.commandNotFound:
                return await eval(f"_{filename}(self.bot, ctx, error)")
            if isinstance(error, _commands.MissingRequiredArgument) and filename == ext.EventName.missingRequiredArgument:
                return await eval(f"_{filename}(self.bot, ctx, error)")
            if isinstance(error, _commands.BadArgument) and filename == ext.EventName.badArgument:
                return await eval(f"_{filename}(self.bot, ctx, error)")
            if isinstance(error, _commands.MissingPermissions) and filename == ext.EventName.missingPermissions:
                return await eval(f"_{filename}(self.bot, ctx, error)")
            if isinstance(error, _commands.BotMissingPermissions) and filename == ext.EventName.botMissingPermissions:
                return await eval(f"_{filename}(self.bot, ctx, error)")
            if isinstance(error, _commands.CommandOnCooldown) and filename == ext.EventName.cooldown:
                return await eval(f"_{filename}(self.bot, ctx, error)")
            if isinstance(error, _commands.CommandInvokeError) and filename == ext.EventName.commandInvokeError:
                return await eval(f"_{filename}(self.bot, ctx, error)")
            if isinstance(error, _commands.CheckFailure) and filename == ext.EventName.checkFailure:
                return await eval(f"_{filename}(self.bot, ctx, error)")
        return
    
    @_commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """
        L'event on_member_join de discord.py est appelé lorsqu'un membre rejoint le serveur.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.memberJoin:
                return await eval(f"_{filename}(self.bot, member)")
        return
    
    @_commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        """
        L'event on_member_remove de discord.py est appelé lorsqu'un membre quitte le serveur.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.memberLeave:
                return await eval(f"_{filename}(self.bot, member)")
        return
    
    @_commands.Cog.listener()
    async def on_member_ban(self, member: discord.Member):
        """
        L'event on_member_ban de discord.py est appelé lorsqu'un membre est banni.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.memberBan:
                return await eval(f"_{filename}(self.bot, member)")
        return
    
    @_commands.Cog.listener()
    async def on_member_unban(self, member: discord.Member):
        """
        L'event on_member_unban de discord.py est appelé lorsqu'un membre est débanni.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.memberUnban:
                return await eval(f"_{filename}(self.bot, member)")
        return
    
    @_commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        """
        L'event on_member_update de discord.py est appelé lorsqu'un membre change de pseudo.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.memberUpdate:
                return await eval(f"_{filename}(self.bot, before, after)")
        return
    
    @_commands.Cog.listener()
    async def on_member_kick(self, member: discord.Member):
        """
        L'event on_member_kick de discord.py est appelé lorsqu'un membre est kick.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.memberKick:
                return await eval(f"_{filename}(self.bot, member)")
        return
    
    @_commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        """
        L'event on_message_edit de discord.py est appelé lorsqu'un message est édité.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.messageEdit:
                return await eval(f"_{filename}(self.bot, before, after)")
        return
    
    @_commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        """
        L'event on_message_delete de discord.py est appelé lorsqu'un message est supprimé.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.messageDelete:
                return await eval(f"_{filename}(self.bot, message)")
        return
    
    @_commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: discord.User):
        """
        L'event on_reaction_add de discord.py est appelé lorsqu'un membre ajoute une réaction.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.reactionAdd:
                return await eval(f"_{filename}(self.bot, reaction, user)")
        return
    
    @_commands.Cog.listener()
    async def on_reaction_remove(self, reaction: discord.Reaction, user: discord.User):
        """
        L'event on_reaction_remove de discord.py est appelé lorsqu'un membre supprime une réaction.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.reactionRemove:
                return await eval(f"_{filename}(self.bot, reaction, user)")
        return
    
    @_commands.Cog.listener()
    async def on_reaction_clear(self, message: discord.Message, reactions: list):
        """
        L'event on_reaction_clear de discord.py est appelé lorsqu'un message est supprimé.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.reactionClear:
                return await eval(f"_{filename}(self.bot, message, reactions)")
        return
    
    @_commands.Cog.listener()
    async def on_webhooks_update(self, channel: discord.TextChannel):
        """
        L'event on_webhooks_update de discord.py est appelé lorsqu'un channel est mis à jour.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.webhooksUpdate:
                return await eval(f"_{filename}(self.bot, channel)")
        return
    
    @_commands.Cog.listener()
    async def on_user_update(self, before: discord.User, after: discord.User):
        """
        L'event on_user_update de discord.py est appelé lorsqu'un utilisateur est mis à jour.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.userUpdate:
                return await eval(f"_{filename}(self.bot, before, after)")
        return  
    
    @_commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        """
        L'event on_guild_join de discord.py est appelé lorsqu'un serveur est ajouté.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.guildJoin:
                return await eval(f"_{filename}(self.bot, guild)")
        return
    
    @_commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        """
        L'event on_guild_remove de discord.py est appelé lorsqu'un serveur est supprimé.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.guildLeave:
                return await eval(f"_{filename}(self.bot, guild)")
        return
    
    @_commands.Cog.listener()
    async def on_guild_update(self, before: discord.Guild, after: discord.Guild):
        """
        L'event on_guild_update de discord.py est appelé lorsqu'un serveur est mis à jour.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.guildUpdate:
                return await eval(f"_{filename}(self.bot, before, after)")
        return
    
    @_commands.Cog.listener()
    async def on_guild_role_create(self, role: discord.Role):
        """
        L'event on_guild_role_create de discord.py est appelé lorsqu'un rôle est créé.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.roleCreate:
                return await eval(f"_{filename}(self.bot, role)")
        return
    
    @_commands.Cog.listener()
    async def on_guild_role_delete(self, role: discord.Role):
        """
        L'event on_guild_role_delete de discord.py est appelé lorsqu'un rôle est supprimé.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.roleDelete:
                return await eval(f"_{filename}(self.bot, role)")
        return
    
    @_commands.Cog.listener()
    async def on_guild_role_update(self, before: discord.Role, after: discord.Role):
        """
        L'event on_guild_role_update de discord.py est appelé lorsqu'un rôle est mis à jour.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.roleUpdate:
                return await eval(f"_{filename}(self.bot, before, after)")
        return
    
    @_commands.Cog.listener()
    async def on_guild_available(self, guild: discord.Guild):
        """
        L'event on_guild_available de discord.py est appelé lorsqu'un serveur est disponible.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.guildAvailable:
                return await eval(f"_{filename}(self.bot, guild)")
        return
    
    @_commands.Cog.listener()
    async def on_guild_unavailable(self, guild: discord.Guild):
        """
        L'event on_guild_unavailable de discord.py est appelé lorsqu'un serveur est indisponible.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.guildUnavailable:
                return await eval(f"_{filename}(self.bot, guild)")
        return

    @_commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        """
        L'event on_voice_state_update de discord.py est appelé lorsqu'un membre change de statut vocal.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.voiceStateUpdate:
                return await eval(f"_{filename}(self.bot, member, before, after)")
        return
    
    @_commands.Cog.listener()
    async def on_invite_create(self, invite: discord.Invite):
        """
        L'event on_invite_create de discord.py est appelé lorsqu'un lien d'invitation est créé.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.inviteCreate:
                return await eval(f"_{filename}(self.bot, invite)")
        return
    
    @_commands.Cog.listener()
    async def on_invite_delete(self, invite: discord.Invite):
        """
        L'event on_invite_delete de discord.py est appelé lorsqu'un lien d'invitation est supprimé.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.inviteDelete:
                return await eval(f"_{filename}(self.bot, invite)")
        return
    
    @_commands.Cog.listener()
    async def on_group_join(self, channel: discord.abc.GuildChannel, user: discord.User):
        """
        L'event on_group_join de discord.py est appelé lorsqu'un membre rejoint un groupe.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.groupJoin:
                return await eval(f"_{filename}(self.bot, channel, user)")
        return
    
    @_commands.Cog.listener()
    async def on_group_remove(self, channel: discord.abc.GuildChannel, user: discord.User):
        """
        L'event on_group_remove de discord.py est appelé lorsqu'un membre quitte un groupe.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.groupLeave:
                return await eval(f"_{filename}(self.bot, channel, user)")
        return
    
    @_commands.Cog.listener()
    async def on_relationship_add(self, relationship: discord.Relationship):
        """
        L'event on_relationship_add de discord.py est appelé lorsqu'un membre ajoute une relation.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.relationshipAdd:
                return await eval(f"_{filename}(self.bot, relationship)")
        return
    
    @_commands.Cog.listener()
    async def on_relationship_remove(self, relationship: discord.Relationship):
        """
        L'event on_relationship_remove de discord.py est appelé lorsqu'un membre supprime une relation.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.relationshipRemove:
                return await eval(f"_{filename}(self.bot, relationship)")
        return
    
    @_commands.Cog.listener()
    async def on_relationship_update(self, relationship: discord.Relationship):
        """
        L'event on_relationship_update de discord.py est appelé lorsqu'un membre change une relation.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.relationshipUpdate:
                return await eval(f"_{filename}(self.bot, relationship)")
        return
    
    @_commands.Cog.listener()
    async def on_guild_integrations_update(self, guild: discord.Guild):
        """
        L'event on_guild_integrations_update de discord.py est appelé lorsqu'un serveur modifie ses intégrations.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.guildIntegrationsUpdate:
                return await eval(f"_{filename}(self.bot, guild)")
        return
    
    @_commands.Cog.listener()
    async def on_guild_channel_pins_update(self, channel: discord.abc.GuildChannel, last_pin: datetime):
        """
        L'event on_guild_channel_pins_update de discord.py est appelé lorsqu'un salon modifie ses pins.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.guildChannelPinsUpdate:
                return await eval(f"_{filename}(self.bot, channel, last_pin)")
        return
    
    @_commands.Cog.listener()
    async def on_private_channel_create(self, channel: discord.abc.PrivateChannel):
        """
        L'event on_private_channel_create de discord.py est appelé lorsqu'un salon privé est créé.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.privateChannelCreate:
                return await eval(f"_{filename}(self.bot, channel)")
        return
    
    @_commands.Cog.listener()
    async def on_private_channel_delete(self, channel: discord.abc.PrivateChannel):
        """
        L'event on_private_channel_delete de discord.py est appelé lorsqu'un salon privé est supprimé.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.privateChannelDelete:
                return await eval(f"_{filename}(self.bot, channel)")
        return
    
    @_commands.Cog.listener()
    async def on_private_channel_update(self, before: discord.abc.PrivateChannel, after: discord.abc.PrivateChannel):
        """
        L'event on_private_channel_update de discord.py est appelé lorsqu'un salon privé est modifié.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.privateChannelUpdate:
                return await eval(f"_{filename}(self.bot, before, after)")
        return
    
    @_commands.Cog.listener()
    async def on_private_channel_pins_update(self, channel: discord.abc.PrivateChannel, last_pin: datetime):
        """
        L'event on_private_channel_pins_update de discord.py est appelé lorsqu'un salon privé modifie ses pins.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.privateChannelPinsUpdate:
                return await eval(f"_{filename}(self.bot, channel, last_pin)")
        return
    
    @_commands.Cog.listener()
    async def on_bulk_message_delete(self, messages: list[discord.Message]):
        """
        L'event on_bulk_message_delete de discord.py est appelé lorsqu'un groupe de messages est supprimé.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.bulkMessageDelete:
                return await eval(f"_{filename}(self.bot, messages)")
        return
    
    @_commands.Cog.listener()
    async def on_typing(self, channel: discord.abc.Messageable, user: discord.abc.User, when: datetime):
        """
        L'event on_typing de discord.py est appelé lorsqu'un utilisateur tape dans un salon.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.typing:
                return await eval(f"_{filename}(self.bot, channel, user, when)")
        return
    
    @_commands.Cog.listener()
    async def on_connect(self):
        """
        L'event on_connect de discord.py est appelé lorsque le bot se connecte.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.connect:
                return await eval(f"_{filename}(self.bot)")
        return

    @_commands.Cog.listener()
    async def on_disconnect(self):
        """
        L'event on_disconnect de discord.py est appelé lorsque le bot se déconnecte.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.disconnect:
                return await eval(f"_{filename}(self.bot)")
        return

    @_commands.Cog.listener()
    async def on_resumed(self):
        """
        L'event on_resumed de discord.py est appelé lorsque le bot reprend la connexion.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.resumed:
                return await eval(f"_{filename}(self.bot)")
        return

    @_commands.Cog.listener()
    async def on_shard_connect(self, shard_id: int):
        """
        L'event on_shard_connect de discord.py est appelé lorsque le bot se connecte à un shard.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.shardConnect:
                return await eval(f"_{filename}(self.bot, shard_id)")
        return
    
    @_commands.Cog.listener()
    async def on_shard_disconnect(self, shard_id: int):
        """
        L'event on_shard_disconnect de discord.py est appelé lorsque le bot se déconnecte d'un shard.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.shardDisconnect:
                return await eval(f"_{filename}(self.bot, shard_id)")
        return
    
    @_commands.Cog.listener()
    async def on_shard_resumed(self, shard_id: int):
        """
        L'event on_shard_resumed de discord.py est appelé lorsque le bot reprend la connexion à un shard.
        """
        for file in os.listdir(f"./event/client"):
            if file.endswith(".py"):
                exec(f"from event.client.{file.removesuffix('.py')} import _{file.removesuffix('.py')}")
        for file in os.listdir(f'{self.eventDIR}/client'):
            filename = file.removesuffix('.py')
            if filename == ext.EventName.shardResumed:
                return await eval(f"_{filename}(self.bot, shard_id)")
        return

class AkernoClient:
    """
    Cette classe va vous permettre de configurer rapidement votre bot, plus qu'à écrire le code !
    """
    def __init__(self, bot: _commands.Bot, eventDIR: str):
        self.prefix = bot.command_prefix
        self.bot = bot
        self.eventDIR = eventDIR
        self.akerno = Discord_akerno(self.bot, self.eventDIR)
        self.bot.add_cog(self.akerno)