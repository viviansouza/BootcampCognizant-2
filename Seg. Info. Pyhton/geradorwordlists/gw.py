import itertools

string = input("String a ser permutada")
resultado = itertools.permutations(string, len(string))  # iteração com os caracteres

for i in resultado:
    print("".join(i))
