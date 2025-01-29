s = 0
m = 0
mh = 0
nv = ' '
tm = 0
for p in range(1,5):
    print(' {} pessoa'.format(p))
    n = str(input('nome:')).strip()
    i = int(input('idade:'))
    se = str(input('sexo[M/F]:')).strip()
    s += i
    if p == 1 and se in 'Mn':
        mh = i
        nv = n
    if se in 'Mn' and i > mh:
        mh = i
        nv = n
    if se in 'Ff' and i <20:
        tm += 1
    m = s /4
print(' media de idade do grupo em anos {}'.format(m))
print('homen  mias velho tem {} nome {}'.format(mh, nv))
print('sao {} mulheres com menos de 20'.format(tm))
