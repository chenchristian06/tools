from irc_class import *
import os
import random

## IRC Config
server = "127.0.0.1" # Provide a valid server IP/Hostname
port = 6697
channel = "#python"
botnick = "techbeamers"
botnickpass = "guido"
botpass = "caca"
irc = IRC()
irc.connect(server, port, channel, botnick, botpass, botnickpass)

while True:
    text = irc.get_response()
    print(text)
 
    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send(channel, "Hello!")
