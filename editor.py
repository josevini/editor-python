from modCreate import *
from modDelete import *
from modAccess import *
from modEditar import *

def menu():
    while True:
        message('MENU PRINCIPAL')
        createMenu('criar', 'apagar', 'acessar', 'editar', stop='sair')
        toDesign('-', 42)
        op = interval(getNumber('Escolha uma opção: '), 0, 4)
        if op == 0:
            break
        elif op == 1:
            menuCriar()
        elif op == 2:
            menuApagar()
        elif op == 3:
            menuAccess()
        elif op == 4:
            menuEditar()
