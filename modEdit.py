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
def editContentFile():
    name, ext = os.path.splitext(getText('Quer editar qual arquivo? '))
    filename = name + ext if ext else name + '.txt'
    if os.path.exists(filename):
        with open(filename, 'a', encoding='utf-8') as file:
            content = getText('Digite aqui: ')
            file.write(content)
    else:
        delay(changeColor('Arquivo não encontrado!', 'red'))

def editFile():
    while True:
        line('-', 42)
        createMenu('Renomear', 'Editar conteúdo', msg='Opções disponíveis para edição')
        line('-', 42)
        op = interval(getNumber('Escolha a opção: '), 0, 2)
        if op == 0:
            delay(changeColor('Cancelando...', 'red'))
            break
        elif op == 1:
            renameFile()
        elif op == 2:
            editContentFile()

def editFolder():
    dirname = getText('Qual o nome da pasta? ')
    if os.path.exists(dirname):
        newDirname = getText('Informe o novo nome: ')
        try:
            os.rename(dirname, newDirname)
        except FileExistsError:
            delay(changeColor('Arquivo já existe!', 'red'))
    else:
        delay(changeColor('Pasta não encontrada!', 'red'))

def menuEdit():
    while True:
        line('-', 42)
        createMenu('arquivo', 'pasta', msg='Deseja editar um arquivo ou pasta?')
        line('-', 42)
        op = interval(getNumber('Escolha uma opção: '), 0, 2)
        if op == 0:
            delay(changeColor('Cancelando...', 'red'))
            break
        elif op == 1:
            editFile()
        elif op == 2:
            editFolder()
