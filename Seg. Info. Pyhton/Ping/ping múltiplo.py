import os
import time  # tempo de espera de um comando para outro


# Com a abertura do hosts como um arquivo criar uma variável chamada dump, lê o arquivo e joga dentro do dump##

with open("hosts") as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print("Verificando o ip: ", ip)
        print("-"*60)
        os.system("ping -n 2 {} ".format(ip))  # dois pacotes
        print("-" * 60)
        time.sleep(5)  # espera de 5 segundos