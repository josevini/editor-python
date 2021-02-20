import os
import os.path
from modInput import *
from modShow import *

def renameFile():
    name, ext = os.path.splitext(getText('Quer renomear qual arquivo? '))
    filename = name+ext if ext else name+'.txt'
    if os.path.exists(filename):
        newName, newExt = os.path.splitext(getText('Informe o novo nome: '))
        newFilename = newName+newExt if newExt else newName+'.txt'
        try:
            os.rename(filename, newFilename)
        except FileExistsError:
            delay(changeColor('Arquivo já existe!', 'red'))
    else:
        delay(changeColor('Arquivo não encontrado!', 'red'))

def editFile():
    while True:
        toDesign('-', 42)
        createMenu('Renomear', 'Editar conteúdo', msg='Opções disponíveis para edição')
        toDesign('-', 42)
        op = interval(getNumber('Escolha a opção: '), 0, 2)
        if op == 0:
            delay(changeColor('Cancelando...', 'red'))
            break
        elif op == 1:
            renameFile()
        elif op == 2:
            name, ext = os.path.splitext(getText('Quer renomear qual arquivo? '))
            filename = name + ext if ext else name + '.txt'
            if os.path.exists(filename):
                newContent = getText('Digite aqui: ')
            else:
                delay(changeColor('Arquivo não encontrado!', 'red'))

def editarPasta():
    pass

def menuEditar():
    while True:
        toDesign('-', 42)
        createMenu('arquivo', 'pasta', msg='Deseja editar um arquivo ou pasta?')
        toDesign('-', 42)
        op = interval(getNumber('Escolha uma opção: '), 0, 2)
        if op == 0:
            delay(changeColor('Cancelando...', 'red'))
            break
        elif op == 1:
            editFile()
        elif op == 2:
            editarPasta()
