import os  ##importa o módulo ou biblioteca

print("#"*60) ##imprimindo 60 vezes
ip_ou_rost = input("Digite o ip ou host a ser verificado: ")
print("-"*60)
os.system('ping -n 6 {}'.format(ip_ou_rost))
##chamando system da biblioteca os - comando ping com um número de pacotes -n que serão 6
print("-"*60)
