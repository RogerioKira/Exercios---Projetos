from random import randint
from time import sleep


def s(lista):
    print('sorteando 5 valores da lista: ', end='')
    for c in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('pronto')

def so(lista):
    so = 0
    for v in lista:
        so += v
    print(f'somando valores pares de {lista},temos {so}')

nu = list()
s(nu)
so(nu)