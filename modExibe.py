import time

def createMenu(*ops, stop='cancelar', msg=''):
    if msg:
        print(msg)
    for pos, op in enumerate(ops):
        print(f'{pos + 1} - {op.capitalize() if op else "default"}')
    print(f'0 - {stop.capitalize()}')

def show(msg=''):
    print(msg)

def delay(msg='', seg=1.0):
    print(msg)
    time.sleep(seg)

def toDesign(simb='', qtd=0):
    print(simb * qtd)

def message(msg='', char='-'):
    tamanho = len(msg) * 3
    toDesign(char, tamanho)
    print(f'{msg.center(tamanho)}')
    toDesign(char, tamanho)

def changeColor(text='', cor='black'):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'gray': '\033[37m'
    }
    open = colors[cor]
    close = '\033[m'
    return f'{open}{text}{close}'

def intervalo(valor, min, max):
    if min <= valor <= max:
        return valor
    print(changeColor(f'Digite um valor entre {min} e {max}', 'red'))
