import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 7777))
server.listen(1)

connection, address = server.accept()

name_file = connection.recv(1024).decode() #decode transforma byte em string

try:
    while True:
        with open(name_file, 'rb') as file:
            for data in file.readlines():
                connection.send(data)
            
            print('Arquivo enviado!')

except Exception as exc:
    print("Deu ruim")

finally:
    server.close()
        




















#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind(('localhost', 7777))
#erver.listen(10)
#while True:
  #  sc, address = server.accept()
  #  nameFile = server.recv(1024).decode()
   # with open(nameFile, 'wb') as file:
     #  while 1:
     #       data = server.recv(10000000)
           #if not data:
         #       break
          #  file.write(data)


    #print(f'{nameFile} recebido!\n')

 # arquivof = open("recebido.txt", 'wb')  # abrir o arquivo para escrita
    #fim = 0
    #while (fim == 0):
     #   ler_buffer = sc.recv(1024)  # aloca no Buffer o que foi recebido

      #  while (ler_buffer):

       #     arquivof.write(ler_buffer)  # escreve no arquivo o buffer recebido
           # ler_buffer = sc.recv(1024)  # aloca o resto no buffer

            #fim = 1
    #arquivof.close()