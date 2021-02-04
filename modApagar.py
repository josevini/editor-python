import os
import os.path
from modEntrada import *
from modExibe import *

def menuApagar():
    while True:
        desenha('-', 42)
        print("""Deseja apagar um arquivo ou uma pasta?
1 - Arquivo
2 - Pasta
0 - Cancelar""")
        desenha('-', 42)
        op = intervalo(entrada('Escolha uma opção: '), 0, 2)
        if op == 0:
            atrasar(mudaCor('Cancelando...', 'red'), 1.3)
            break
        elif op == 1:
            print('Apagar arquivo...')
        elif op == 2:
            print('Apagar pasta...')
