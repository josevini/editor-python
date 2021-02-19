from modShow import *

def getText(msg=''):
    value = input(msg)
    return value

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
        value = input(msg)
        try:
            return int(value)
        except ValueError as erro:
            delay(changeColor('Digite um número válido!', 'red'))
