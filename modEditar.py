import os
import os.path
from modEntrada import *
from modExibe import *

def editarArquivo():
    while True:
        toDesign('-', 42)
        createMenu('Renomear', 'Editar conteúdo', msg='Opções disponíveis para edição')
        toDesign('-', 42)
        op = intervalo(getNumber('Escolha a opção: '), 0, 2)
        if op == 0:
            delay(changeColor('Cancelando...', 'red'))
        elif op == 1:
            pass
        elif op == 2:
            pass
def editarPasta():
    pass

def menuEditar():
    while True:
        toDesign('-', 42)
        createMenu('arquivo', 'pasta', msg='Deseja editar um arquivo ou pasta?')
        toDesign('-', 42)
        op = intervalo(getNumber('Escolha uma opção: '), 0, 2)
        if op == 0:
            delay(changeColor('Cancelando...', 'red'))
            break
        elif op == 1:
            editarArquivo()
        elif op == 2:
            editarPasta()
