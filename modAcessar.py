import os
import os.path
from modEntrada import *
from modExibe import *

def acessarArquivo():
    while True:
        nome, ext = os.path.splitext(entradaTexto('Quer ler qual arquivo: '))
        filename = (nome+ext) if ext else (nome+'.txt')
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read())

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
            pass
        break
