import os
import os.path
from modEntrada import *
from modExibe import *

def deleteFile():
    nome, ext = os.path.splitext(getText('Informe o nome do arquivo: '))
    filename = (nome + ext) if ext else (nome + '.txt')
    delay(changeColor('Processando...', 'yellow'))
    if os.path.exists(filename):
        if os.path.getsize(filename) > 0:
            continuar = question(changeColor('O arquivo não está vazio, quer continuar? [s/n]: ', 'yellow'))
            if continuar:
                os.remove(filename)
                delay(changeColor(f'Apagando o arquivo {filename}...', 'yellow'), 1.3)
                delay(changeColor(f'Arquivo {filename} apagado!', 'green'))
            else:
                delay(changeColor('Nenhum arquivo foi apagado!', 'red'))
        else:
            os.remove(filename)
            delay(changeColor(f'Apagando o arquivo {filename}...', 'yellow'), 1.3)
            delay(changeColor(f'Arquivo {filename} apagado!', 'green'))
    else:
        delay(changeColor('Arquivo não encontrado!', 'red'))

def deleteDir():
    dirname = getText('Informe o nome da pasta: ')
    continuar = question(changeColor('Deseja prosseguir com a ação? [s/n]: ', 'yellow'))
    if continuar:
        delay(changeColor(f'Apagando a pasta {dirname}...', 'yellow'), 1.3)
        try:
            os.rmdir(dirname)
            delay(changeColor(f'Pasta {dirname} apagada!', 'green'))
        except FileNotFoundError:
            delay(changeColor('Essa pasta não existe!', 'red'))
        except OSError:
            delay(changeColor('A pasta não está vazia!', 'red'))
    else:
        delay(changeColor('Cancelando...', 'red'))

def menuDelete():
    while True:
        toDesign('-', 42)
        createMenu('arquivo', 'pasta', msg='Deseja apagar um arquivo ou pasta?')
        toDesign('-', 42)
        op = interval(getNumber('Escolha uma opção: '), 0, 2)
        if op == 0:
            delay(changeColor('Cancelando...', 'red'))
            break
        elif op == 1:
            deleteFile()
        elif op == 2:
            deleteDir()
