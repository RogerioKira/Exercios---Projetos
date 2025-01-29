t = []
p = []
ma = me = 0
while True:
    t.append(str(input('nome')))
    t.append(float(input('peso')))
    if len(p) == 0:
        ma = me = t[1]
    else:
        if t[1] > ma:
            ma = t[1]
        if t[1] < me:
            me = t[1]
    p.append(t[:])
    t.clear()
    r = str(input('continuar[S/N]'))
    if r in 'Nn':
        break
print(f'os dados foram {p}')
print(f'vc cadastrou {len(p)} pessoas')
print(f'o maior peso foi {ma}, peso de ', end=' ')
for n in p:
    if n[1] == ma:
        print(f'{n[0]}', end=' ')
print()
print(f'menor peso {me}, peso de ', end=' ')
for n in p:
    if n[1] == me:
        print(f'[{n[0]}]', end=' ')
print()