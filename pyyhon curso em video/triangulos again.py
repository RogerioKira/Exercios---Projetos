r1 = float(input('primeiro'))
r2 = float(input('segundo'))
r3 = float(input('terceiro'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('forma triangulo ', end='')
    if r1 == r2 == r3:
        print('equilatero')
    elif r1 != r2 != r3 != r1:
        print('escaleno')
    else:
        print('isoceles')
else:
    print('nao forma triangulo')