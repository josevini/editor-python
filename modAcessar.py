import os
import os.path
from modEntrada import *
from modExibe import *

def menuAcessar():
    while True:
        desenha('-', 42)
        print("""Deseja acessar um arquivo ou pasta?
1 - Arquivo
2 - Pasta
0 - Cancelar""")
        break
