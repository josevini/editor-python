from modCriar import *
from modApagar import *
from modAcessar import *

def menu():
    while True:
        mensagem('MENU PRINCIPAL')
        geraMenu('criar', 'apagar', 'acessar', 'editar', stop='sair')
        desenha('-', 42)
        op = intervalo(entrada('Escolha uma opção: '), 0, 4)
        if op == 0:
            break
        elif op == 1:
            menuCriar()
        elif op == 2:
            menuApagar()
        elif op == 3:
            menuAcessar()
