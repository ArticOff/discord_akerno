from discord_akerno import CreateEvent, ext

EventName = ext.EventName
Arg = ext.EventArg

CreateEvent(EventName.commandNotFound, "command", [Arg.context, Arg.error])

"""
1. le nom de l'event' (et du fichier)
2. la catégorie (client, command)
3. les arguments
"""
