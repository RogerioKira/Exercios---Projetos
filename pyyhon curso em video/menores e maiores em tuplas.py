from random import randint
n = (randint(1,10), randint(1,10), randint(1,10),
randint(1,10),randint(1,10))
print('valores sorteados', end=' ')
for m in n:
    print(f'{m}', end='')
print(f'\n0 maior valor {max(n)}')
print(f'menor sorteado {min(n)}')