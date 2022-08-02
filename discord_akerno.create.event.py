from discord_akerno import CreateEvent, ext

EventName = ext.EventName
Arg = ext.EventArg

CreateEvent("on_ready", "client", EventName.ready, [])

"""
1. le nom de la commande (et du fichier)
2. la catégorie (client, command)
3. le nom de l'event
4. les arguments
"""