import os
import os.path
from modEntrada import *
from modExibe import *

def menuAcessar():
    while True:
        desenha('-', 42)
        geraMenu('arquivo', 'pasta', msg='Deseja acessar um arquivo ou pasta?')
        desenha('-', 42)
        op = intervalo(entrada('Escolha uma opção: '), 0, 2)
        break
