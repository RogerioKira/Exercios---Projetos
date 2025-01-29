t = list()
j = dict()
p = list()
while True:
    j.clear()
    j['nome'] = str(input('nome:'))
    to = int(input(f'quantas patidas {j["nome"]} jogou'))
    p.clear()
    for c in range (0,to):
        p.append(int(input(f'quantos gols {c+1}')))
    j['gols'] = p[:]
    j['total'] = sum(p)
    t.append(j.copy())
    while True:
        r = str(input('continuar [S/N]')).upper()[0]
        if r in 'SN':
            break
        print('erro')
    if r == 'N':
        break
print('cod', end=' ')
for i in j.keys():
    print(f'{i:<15}', end=' ')
print()
for k,v in enumerate(t):
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    b = int(input('mostar jogador (999 para)'))
    if b == 999:
        break
    if b >= len(t):
        print(f'erro')
    else:
        print(f'lrvantamento do jogador {t[b]["nome"]}:')
        for i,g in enumerate(t[b]['gols']):
            print(f' no jogo {i+1} fez {g} gols')
print('volte sempre')