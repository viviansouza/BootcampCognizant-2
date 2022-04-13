import ctypes

atributo_ocultar = 0X02

retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado.")
else:
    print("Arquivo não foi ocultado.")