import os
import os.path
from modEntrada import *
from modExibe import *

def apagarArquivo():
    nome, ext = os.path.splitext(entradaTexto('Informe o nome do arquivo: '))
    filename = (nome + ext) if ext else (nome + '.txt')
    atrasar(mudaCor('Processando...', 'yellow'))
    if os.path.exists(filename):
        if os.path.getsize(filename) > 0:
            continuar = pergunta(mudaCor('O arquivo não está vazio, quer continuar? [s/n]: ', 'yellow'))
            if continuar:
                os.remove(filename)
                atrasar(mudaCor(f'Apagando o arquivo {filename}...', 'yellow'), 1.5)
                atrasar(mudaCor(f'Arquivo {filename} apagado!', 'green'))
            else:
                atrasar(mudaCor('Nenhum arquivo foi apagado!', 'red'))
        else:
            os.remove(filename)
            atrasar(mudaCor(f'Apagando o arquivo {filename}...', 'yellow'), 1.5)
            atrasar(mudaCor(f'Arquivo {filename} apagado!', 'green'))
    else:
        atrasar(mudaCor('Arquivo não encontrado!', 'red'))

def menuApagar():
    while True:
        desenha('-', 42)
        print("""Deseja apagar um arquivo ou uma pasta?
1 - Arquivo
2 - Pasta
0 - Cancelar""")
        desenha('-', 42)
        op = intervalo(entrada('Escolha uma opção: '), 0, 2)
        if op == 0:
            atrasar(mudaCor('Cancelando...', 'red'))
            break
        elif op == 1:
            apagarArquivo()
        elif op == 2:
            print('Apagar pasta...')
