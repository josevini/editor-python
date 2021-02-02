import os
import os.path
import time

def atrasar(msg='', seg=1.0):
    print(msg)
    time.sleep(seg)

def desenha(simb='', qtd=0):
    print(simb * qtd)

def mensagem(msg='', char='-'):
    desenha(char, len(msg) * 3)
    print(f'{msg.center(len(msg) * 3)}')
    desenha(char, len(msg) * 3)

def entradaTexto(msg=''):
    valor = input(msg)
    return valor

def pergunta(msg=''):
    resp = input(msg).lower()[0]
    if resp == 's':
        return True
    elif resp == 'n':
        return False
    else:
        print('Opção inválida!')

def entrada(msg=''):
    while True:
        valor = input(msg)
        try:
            return int(valor)
        except Exception as erro:
            print('Digite um número válido!')

def intervalo(valor, min, max):
    if min <= valor <= max:
        return valor
    print(f'Digite um valor entre {min} e {max}')

def criarArquivo():
    nome, ext = os.path.splitext(entradaTexto('Informe o nome do arquivo: '))
    filename = (nome + ext) if ext else (nome + '.txt')
    atrasar('Processando...', 1.3)
    if os.path.exists(filename):
        resp = pergunta('Arquivo encontrado! Quer sobrescrever? [s/n]: ')
        if resp:
            atrasar(f'Criando arquivo {filename}...', 1.5)
            file = open(filename, 'w', encoding='utf-8')
            atrasar(f'Arquivo {filename} criado!', 1.3)
        else:
            atrasar('Nenhum arquivo foi criado!', 1.3)
    else:
        atrasar(f'Criando arquivo {filename}...', 1.5)
        file = open(filename, 'w', encoding='utf-8')
        atrasar(f'Arquivo {filename} criado!', 1.3)

def criarPasta():
    while True:
        dirname = entradaTexto('Informe o nome da pasta: ')
        atrasar(f'Criando a pasta {dirname}...', 1.5)
        try:
            os.mkdir(dirname)
            atrasar(f'Pasta {dirname} criada!', 1.3)
            break
        except FileExistsError as erro:
            atrasar('Ops! Pasta encontrada, tente outro nome!', 1.3)
            desenha('-', 42)

def criar():
    while True:
        desenha('-', 42)
        print("""Deseja criar um arquivo ou uma pasta?
1 - Arquivo
2 - Pasta
0 - Cancelar""")
        desenha('-', 42)
        op = intervalo(entrada('Escolha uma opção: '), 0, 2)
        if op == 0:
            atrasar('Cancelando...', 1.3)
            break
        elif op == 1:
            criarArquivo()
        elif op == 2:
            criarPasta()
def menu():
    while True:
        mensagem('MENU PRINCIPAL')
        print("""1 - Criar
2 - Apagar
3 - Acessar
4 - Editar
0 - Sair""")
        desenha('-', 42)
        op = intervalo(entrada('Escolha uma opção: '), 0, 4)
        if op == 0:
            break
        elif op == 1:
            criar()

