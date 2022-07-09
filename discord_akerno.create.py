from discord_akerno import CreateCommand, ext

Permission = ext.Permission

CreateCommand('clear', 'moderation', 'efface des messages', ['clear'], Permission.gerer_les_messages, Permission.gerer_les_messages)

"""
1. le nom de la commande (et du fichier)
2. la catégorie (moderation, utility, fun)
3. la description
4. les aliases
5. les permissions requises pour l'utilisateur
6. les permissions requises pour le bot
"""
