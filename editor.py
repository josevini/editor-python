import os
import os.path
import time

def atrasar(msg='', seg=1.0):
    print(msg)
    time.sleep(seg)

def desenha(simb='', qtd=0):
    print(simb * qtd)

def mensagem(msg='', char='-'):
    tamanho = len(msg) * 3
    desenha(char, tamanho)
    print(f'{msg.center(tamanho)}')
    desenha(char, tamanho)

def mudaCor(text='', cor='preto'):
    cores = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'gray': '\033[37m'
    }
    abre = cores[cor]
    fecha = '\033[m'
    return f'{abre}{text}{fecha}'

def entradaTexto(msg=''):
    valor = input(msg)
    return valor

def pergunta(msg=''):
    resp = input(msg).lower()
    if resp == 's':
        return True
    elif resp == 'n':
        return False
    else:
        atrasar(mudaCor('Opção inválida!', 'red'))

def entrada(msg=''):
    while True:
        valor = input(msg)
        try:
            return int(valor)
        except Exception as erro:
            atrasar(mudaCor('Digite um número válido!', 'red'))

def intervalo(valor, min, max):
    if min <= valor <= max:
        return valor
    print(mudaCor(f'Digite um valor entre {min} e {max}', 'red'))

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
            menuCriar()
