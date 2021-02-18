import os
import os.path
from modEntrada import *
from modExibe import *

def editarArquivo():
    desenha('-', 42)
    geraMenu('Editar conteúdo', 'Renomear', msg='Opções disponíveis para edição')
    desenha('-', 42)
    op = intervalo(getNumber('Escolha a opção: '), 0, 2)
    if op == 0:
        atrasar(mudaCor('Cancelando...', 'red'))

def editarPasta():
    pass

def menuEditar():
    while True:
        desenha('-', 42)
        geraMenu('arquivo', 'pasta', msg='Deseja editar um arquivo ou pasta?')
        desenha('-', 42)
        op = intervalo(getNumber('Escolha uma opção: '), 0, 2)
        if op == 0:
            atrasar(mudaCor('Cancelando...', 'red'))
            break
        elif op == 1:
            editarArquivo()
        elif op == 2:
            editarPasta()
