import os
import os.path
from modEntrada import *
from modExibe import *

def acessarArquivo():
    while True:
        nome, ext = os.path.splitext(entradaTexto('Quer ler qual arquivo: '))
        filename = (nome+ext) if ext else (nome+'.txt')
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                desenha('-', 42)
                atrasar('CONTEÚDO:', 0)
                exibir(mudaCor(file.read(), 'blue'))
                break
        except FileNotFoundError:
            atrasar(mudaCor('Arquivo não encontrado!', 'red'))

def acessarPasta():
    while True:
        dirname = entradaTexto('Quer listar qual pasta: ')
        try:
            listagem = os.listdir(dirname)
            desenha('-', 42)
            exibir('CONTEÚDO:')
            if listagem:
                for dir in listagem:
                    exibir(mudaCor(dir, 'blue'))
            else:
                exibir(mudaCor('Vazio!', 'blue'))
            break
        except FileNotFoundError:
            atrasar(mudaCor('Pasta não encontrada!', 'red'))

def menuAcessar():
    while True:
        desenha('-', 42)
        geraMenu('arquivo', 'pasta', msg='Deseja acessar um arquivo ou pasta?')
        desenha('-', 42)
        op = intervalo(entrada('Escolha uma opção: '), 0, 2)
        if op == 0:
            break
        elif op == 1:
            acessarArquivo()
        elif op == 2:
            acessarPasta()
