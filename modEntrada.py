from modExibe import *

def getText(msg=''):
    valor = input(msg)
    return valor

def question(msg=''):
    resp = input(msg).lower()
    if resp == 's':
        return True
    elif resp == 'n':
        return False
    else:
        delay(changeColor('Opção inválida!', 'red'))

def getNumber(msg=''):
    while True:
        valor = input(msg)
        try:
            return int(valor)
        except ValueError as erro:
            delay(changeColor('Digite um número válido!', 'red'))
