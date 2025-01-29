a = dict()
a['n'] = str(input('Nomes'))
a['m'] = float(input(f'media {a["n"]}: '))
if a['m'] >= 7:
    a['s'] = 'aprovado'
elif 5 <= a['m'] < 7:
    a['s'] = 'recuperacao'
else:
    a['s'] = 'Reprovado'
for k,v in a.items():
    print(f'{k} e igual a {v}')