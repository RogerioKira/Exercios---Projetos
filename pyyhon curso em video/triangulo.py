r1 = float(input('primeiro'))
r2 = float(input('segundo'))
r3 = float(input('terceiro'))
if r1<r2+r3 and r2<r1 + r3 and r3<r1 + r2:
    print('forman triangulo')
else:
    print('nao forma triangulo')