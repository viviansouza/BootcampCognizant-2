import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!")

host = "localhost"
porta = 5432

s.bind((host, porta))
mensagem = "\nServidor: Oláaaa Cliente, e aí... tudo bem?"

while 1:
    dados, endereco = s.recvfrom(4096)
    if dados:
        print("Srvidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode()), endereco)
