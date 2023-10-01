import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print('Conectado ao servidor!\n')

name_file = str(input('Digite o nome do arquivo a ser enviado -->'))

client.send(name_file.encode())

with open(name_file, 'wb') as file:
    while 1:
        data = client.recv(1000000) 
        if not data:
          break
        file.write(data)

print(f'{name_file} Recebido!\n')




                   
          

          