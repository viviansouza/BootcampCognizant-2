import random
import string

tamanho = int(input("Digite o tamanho de senha que você deseja: "))

chars = string.ascii_letters + string.digits + "!@#$%&*()-=+;/?"

rnd = random.SystemRandom()

print("".join(rnd.choice(chars)for i in range(tamanho)))
"""
rnd.choice retorna uma lista com caracteres randômicos.
"""



