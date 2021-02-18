import os
import os.path
from modEntrada import *
from modExibe import *

def acessarArquivo():
    while True:
        nome, ext = os.path.splitext(getText('Quer ler qual arquivo: '))
        filename = (nome+ext) if ext else (nome+'.txt')
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                toDesign('-', 42)
                delay('CONTEÚDO:', 0)
                content = file.read()
                show(changeColor(content if content else 'Vazio!', 'blue'))
                break
        except FileNotFoundError:
            delay(changeColor('Arquivo não encontrado!', 'red'))

def acessarPasta():
    while True:
        dirname = getText('Quer listar qual pasta: ')
        try:
            listagem = os.listdir(dirname)
            toDesign('-', 42)
            show('CONTEÚDO:')
            if listagem:
                for dir in listagem:
                    show(changeColor(dir, 'blue'))
            else:
                show(changeColor('Vazio!', 'blue'))
            break
        except FileNotFoundError:
            delay(changeColor('Pasta não encontrada!', 'red'))

def menuAcessar():
    while True:
        toDesign('-', 42)
        createMenu('arquivo', 'pasta', msg='Deseja acessar um arquivo ou pasta?')
        toDesign('-', 42)
        op = interval(getNumber('Escolha uma opção: '), 0, 2)
        if op == 0:
            delay(changeColor('Cancelando...', 'red'))
            break
        elif op == 1:
            acessarArquivo()
        elif op == 2:
            acessarPasta()
