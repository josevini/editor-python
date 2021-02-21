import os
import os.path
from modInput import *
from modShow import *

def accessFile():
    while True:
        name, ext = os.path.splitext(getText('Quer ler qual arquivo: '))
        filename = (name + ext) if ext else (name + '.txt')
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                toDesign('-', 42)
                delay('CONTEÚDO:', 0)
                content = file.read()
                show(changeColor(content if content else 'Vazio!', 'blue'))
                break
        except FileNotFoundError:
            delay(changeColor('Arquivo não encontrado!', 'red'))
        except UnicodeDecodeError:
            delay(changeColor('Formato de arquivo não suportado!', 'red'))

def accessDir():
    while True:
        dirname = getText('Quer listar qual pasta: ')
        try:
            listingResult = os.listdir(dirname)
            toDesign('-', 42)
            show('CONTEÚDO:')
            if listingResult:
                for dir in listingResult:
                    show(changeColor(dir, 'blue'))
            else:
                show(changeColor('Vazio!', 'blue'))
            break
        except FileNotFoundError:
            delay(changeColor('Pasta não encontrada!', 'red'))

def menuAccess():
    while True:
        toDesign('-', 42)
        createMenu('arquivo', 'pasta', msg='Deseja acessar um arquivo ou pasta?')
        toDesign('-', 42)
        op = interval(getNumber('Escolha uma opção: '), 0, 2)
        if op == 0:
            delay(changeColor('Cancelando...', 'red'))
            break
        elif op == 1:
            accessFile()
        elif op == 2:
            accessDir()
