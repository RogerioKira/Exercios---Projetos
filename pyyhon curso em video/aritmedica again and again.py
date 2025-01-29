p = int(input('primeiro'))
r = int(input('razao'))
t = p
c = 1
to = 0
m = 10
while m != 0:
    to = to + m
    while c <= to:
        print(' {} ->'.format(t),end= ' ')
        t += r
        c += 1
    print('pausa')
    m = int(input('quantos termos a mais:'))
print('progresao realizada com {} termos mostrados'.format(to))