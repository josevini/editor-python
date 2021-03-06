from modCreate import *
from modDelete import *
from modAccess import *
from modEdit import *

def menu():
    while True:
        header('MENU PRINCIPAL', size=42)
        createMenu('criar', 'editar', 'acessar', 'apagar', stop='sair')
        line('-', 42)
        op = interval(getNumber('Escolha uma opção: '), 0, 4)
        if op == 0:
            break
        elif op == 1:
            menuCreate()
        elif op == 2:
            menuEdit()
        elif op == 3:
            menuAccess()
        elif op == 4:
            menuDelete()
