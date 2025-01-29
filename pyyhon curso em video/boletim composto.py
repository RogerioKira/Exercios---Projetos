f = list()
while True:
    n = str(input('nome:'))
    n1 = float(input('nota 1:'))
    n2 = float(input('nota 2:'))
    m = (n1+n2) / 2
    f.append([n,[n1,n2], m])
    r = str(input('continuar[S/n'))
    if r in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"Media":>8}')
for i,a, in enumerate(f):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    o = int(input('mostrar notas aluno(999 fim):'))
    if o == 999:
        print('fim ...')
        break
    if o <= len(f) - 1:
        print(f'notas de {f[o][0]} sao {f[o][1]}')
print('adeus')