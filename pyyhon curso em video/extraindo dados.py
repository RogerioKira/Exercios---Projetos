v = []
while True:
    v.append(int(input('digite valor')))
    r = str(input('quer continuar[S/N]'))
    if r in 'Nn':
        break
print(f'voce digitou {len(v)} elementos.')
v.sort(reverse=True)
print(f'valores decendentes {v}')
if 5 in v:
    print('o valor 5 esta na lista')
else:
    print('5 nao esta na lista')