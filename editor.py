from modCriar import *
from modApagar import *

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
        elif op == 2:
            atrasar('Apagar...', 0)
