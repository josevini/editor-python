import os
import os.path
from modEntrada import *
from modExibe import *

def menuEditar():
    desenha('-', 42)
    geraMenu('arquivo', 'pasta', msg='Deseja editar um arquivo ou pasta?')
    desenha('-', 42)
