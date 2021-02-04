import os
import os.path
from modEntrada import *
from modExibe import *

def criarArquivo():
    nome, ext = os.path.splitext(entradaTexto('Informe o nome do arquivo: '))
    continuar = pergunta(mudaCor('Deseja prosseguir com a ação? [s/n]: ', 'yellow'))
    if continuar:
        filename = (nome + ext) if ext else (nome + '.txt')
        atrasar(mudaCor('Processando...', 'yellow'), 1.3)
        if os.path.exists(filename):
            resp = pergunta(mudaCor('Arquivo encontrado! Quer sobrescrever? [s/n]: ', 'yellow'))
            if resp:
                atrasar(mudaCor(f'Criando arquivo {filename}...', 'yellow'), 1.5)
                file = open(filename, 'w', encoding='utf-8')
                atrasar(mudaCor(f'Arquivo {filename} criado!', 'green'), 1.3)
            else:
                atrasar(mudaCor('Nenhum arquivo foi criado!', 'red'), 1.3)
        else:
            atrasar(mudaCor(f'Criando arquivo {filename}...', 'yellow'), 1.5)
            file = open(filename, 'w', encoding='utf-8')
            atrasar(mudaCor(f'Arquivo {filename} criado!', 'green'), 1.3)
    else:
        atrasar(mudaCor('Cancelando...', 'red'), 1.3)

def criarPasta():
    while True:
        dirname = entradaTexto('Informe o nome da pasta: ')
        continuar = pergunta(mudaCor('Deseja prosseguir com a ação? [s/n]: ', 'yellow'))
        if continuar:
            atrasar(mudaCor(f'Criando a pasta {dirname}...', 'yellow'), 1.5)
            try:
                os.mkdir(dirname)
                atrasar(mudaCor(f'Pasta {dirname} criada!', 'green'), 1.3)
                break
            except FileExistsError as erro:
                atrasar(mudaCor('Ops! Pasta encontrada, tente outro nome!', 'yellow'), 1.3)
                desenha('-', 42)
        else:
            atrasar(mudaCor('Cancelando...', 'red'), 1.3)
            break
def menuCriar():
    while True:
        desenha('-', 42)
        print("""Deseja criar um arquivo ou uma pasta?
1 - Arquivo
2 - Pasta
0 - Cancelar""")
        desenha('-', 42)
        op = intervalo(entrada('Escolha uma opção: '), 0, 2)
        if op == 0:
            atrasar(mudaCor('Cancelando...', 'red'), 1.3)
            break
        elif op == 1:
            criarArquivo()
        elif op == 2:
            criarPasta()