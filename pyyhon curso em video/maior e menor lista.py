l = []
ma = 0
me = 0
for c in range(0,5):
    l.append(int(input(f'digite um valor pa ra {c}')))
    if c == 0:
        ma = me = l[c]
    else:
        if l[c] > ma:
            ma = l[c]
        if l[c] < me:
            me = l[c]
print(f'voce digitou {l}')
print(f'maior {ma} nas posição', end=' ')
for i,v in enumerate(l):
    if v == ma:
        print(f'{i}...', end='')
print()
print(f'menor {me} na posição ', end=' ')
for i, v in enumerate(l):
    if v == me:
        print(f'{i}...', end=' ')
print()