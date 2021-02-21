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

def line(simb='', qtd=0):
    print(simb * qtd)

def header(msg='', char='-'):
    size = len(msg) * 3
    line(char, size)
    print(f'{msg.center(size)}')
    line(char, size)

def changeColor(text='', color='black'):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'gray': '\033[37m'
    }
    open = colors[color]
    close = '\033[m'
    return f'{open}{text}{close}'

def interval(value, min, max):
    if min <= value <= max:
        return value
    print(changeColor(f'Digite um valor entre {min} e {max}', 'red'))
