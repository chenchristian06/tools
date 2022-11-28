import socket
ircbot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'irc.christianchen'
PORT = 6667
NICK = "Kris"
ircbot.connect((HOST,PORT))

