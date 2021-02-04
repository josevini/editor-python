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

def mudaCor(text='', cor='black'):
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

def intervalo(valor, min, max):
    if min <= valor <= max:
        return valor
    print(mudaCor(f'Digite um valor entre {min} e {max}', 'red'))
