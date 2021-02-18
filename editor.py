from modCriar import *
from modApagar import *
from modAcessar import *
from modEditar import *

def menu():
    while True:
        message('MENU PRINCIPAL')
        createMenu('criar', 'apagar', 'acessar', 'editar', stop='sair')
        toDesign('-', 42)
        op = intervalo(getNumber('Escolha uma opção: '), 0, 4)
        if op == 0:
            break
        elif op == 1:
            menuCriar()
        elif op == 2:
            menuApagar()
        elif op == 3:
            menuAcessar()
        elif op == 4:
            menuEditar()
