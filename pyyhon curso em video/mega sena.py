from random import randint
from time import sleep
l = list()
j = list()
q = int(input('quantos sorteios'))
t = 1
while t <= q:
    c = 0
    while True:
        n = randint(1,60)
        if n not in l:
            l.append(n)
            c += 1
        if c >= 6:
            break
    l.sort()
    j.append((l[:]))
    l.clear()
    t += 1
print('-='*3, f'sorteado {q} jogos', '-='*3)
for i,r in enumerate(j):
    print(f'jogo {i+1}: {r}')
    sleep(1)
print('<boa sorte>')