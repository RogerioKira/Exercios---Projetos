g = list()
p = dict()
s = m = 0
while True:
    p.clear()
    p['nome'] = str(input('Nome:'))
    while True:
        p['sexo'] = str(input('sexo: [M/F]')).upper()[0]
        if p['sexo'] in 'MF':
            break
        print('erro')
    p['idade'] = int(input('Idade:'))
    s += p['idade']
    g.append(p.copy())
    while True:
        r = str(input('continuar [s/n]')).upper()[0]
        if r in 'SN':
            break
        print('erro')
    if r == 'N':
        break
print(f'A)temos {len(g)} pessoas cadastradas')
m = s/len(g)
print(f'B) a media de idade {m:5.2f} anos')
print('C) as mulheres cadastradas foram ', end='')
for q in g:
    if q['sexo'] in 'Ff':
        print(f'{q["nome"]}', end='')
print()
print('D)lista dos acima da media')
for q in g:
    if q['idade']>=m:
        print('  ', end='')
        for k,v in q.items():
            print(f'{k} = {v}; ', end='')
        print()
print('fim')