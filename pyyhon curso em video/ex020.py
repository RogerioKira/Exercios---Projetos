e = dict()
b = list()
for c in range(0,3):
    e['uf'] = str(input('unidade federativa:'))
    e['sigla'] = str(input('sigla'))
    b.append(e.copy())
for w in b:
    for v in w.values():
        print(w,end=' ')
    print()