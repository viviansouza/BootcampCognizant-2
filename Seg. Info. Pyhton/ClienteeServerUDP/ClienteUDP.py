import socket
#  criando objeto de conexão chamado "s"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,)

print("Cliente Socket criado com sucesso!!")

# estabelecer o localhost como host na porta 5433
host = "localhost"
porta = 5433
mensagem = "Olá servidor, tudo bem?"

# tentanto enviar e receber a mensagem

try:
    print("Cliente: " + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))  #empacotar a mensagem e enviar com pacotes udp para servidor

#Vão receber do servidor uma resposta de 4096 bytes
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode() # desempacota os dados
    print("Cliente: " + dados)

finally:
    print("Cliente: Fechando a conexão")
    s.close()  #fechar a conexão para não ficar em loop
