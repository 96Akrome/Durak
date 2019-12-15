import shutil
import pygame
import os


# borra los archivos pyc y __pycache__
def limpiar_dir():
    for root, dirs, files in os.walk('.'):
        for dir in dirs:
            if dir == '__pycache__':
                path = os.path.join(root, dir)
                print('Borrando {}'.format(os.path.abspath(path)))
                shutil.rmtree(path)
        for name in files:
            if name.endswith('.pyc'):
                path = os.path.join(root, name)
                print('Borrando {}'.format(os.path.abspath(path)))
                os.remove(path)


# retorna direccion actual
def current_dir():
    return os.getcwd()
