from modExibe import *

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
        except ValueError as erro:
            atrasar(mudaCor('Digite um número válido!', 'red'))
