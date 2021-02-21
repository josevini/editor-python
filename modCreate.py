import os
import os.path
from modInput import *
from modShow import *

def createFile():
    total = getNumber('Quantos arquivos: ')
    while total > 0:
        toDesign('-', 42)
        name, ext = os.path.splitext(getText('Informe o nome do arquivo: '))
        continuar = question(changeColor('Deseja prosseguir com a ação? [s/n]: ', 'yellow'))
        if continuar:
            filename = (name + ext) if ext else (name + '.txt')
            delay(changeColor('Processando...', 'yellow'))
            if os.path.exists(filename):
                resp = question(changeColor('Arquivo encontrado! Quer sobrescrever? [s/n]: ', 'yellow'))
                if resp:
                    delay(changeColor(f'Criando arquivo {filename}...', 'yellow'), 1.3)
                    file = open(filename, 'w', encoding='utf-8')
                    delay(changeColor(f'Arquivo {filename} criado!', 'green'))
                else:
                    delay(changeColor('Nenhum arquivo foi criado!', 'red'))
            else:
                delay(changeColor(f'Criando arquivo {filename}...', 'yellow'), 1.3)
                file = open(filename, 'w', encoding='utf-8')
                delay(changeColor(f'Arquivo {filename} criado!', 'green'))
        else:
            delay(changeColor('Cancelando...', 'red'), 1.3)
        total -= 1

def createDir():
    while True:
        dirname = getText('Informe o nome da pasta: ')
        continuar = question(changeColor('Deseja prosseguir com a ação? [s/n]: ', 'yellow'))
        if continuar:
            delay(changeColor(f'Criando a pasta {dirname}...', 'yellow'), 1.3)
            try:
                os.mkdir(dirname)
                delay(changeColor(f'Pasta {dirname} criada!', 'green'))
                break
            except FileExistsError:
                delay(changeColor('Ops! Pasta encontrada, tente outro nome!', 'yellow'))
                toDesign('-', 42)
        else:
            delay(changeColor('Cancelando...', 'red'))
            break
def menuCreate():
    while True:
        toDesign('-', 42)
        createMenu('arquivo', 'pasta', msg='Deseja criar um arquivo ou pasta?')
        toDesign('-', 42)
        op = interval(getNumber('Escolha uma opção: '), 0, 2)
        if op == 0:
            delay(changeColor('Cancelando...', 'red'))
            break
        elif op == 1:
            createFile()
        elif op == 2:
            createDir()
