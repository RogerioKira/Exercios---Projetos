n = list()
p = list()
im = list()
while True:
    n.append(int(input('digitou:')))
    r = str(input('continuar[S/N]'))
    if r in 'Nn':
        break
for i,v in enumerate(n):
    if v % 2 == 0:
        p.append(v)
    elif v % 2 == 1:
        im.append(v)
print(f'a lista completa {n}')
print(f'lista pares{p}')
print(f'lista impares {im}')