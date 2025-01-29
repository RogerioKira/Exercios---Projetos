t8 = th = t2 = 0
while True:
    i = int(input('idade'))
    s = ' '
    while s not in 'mMFf':
        s = str(input('sexo [M/F]')).strip().upper()[0]
    if i >= 18:
        t8 += 1
    if s == 'Mm':
        th += 1
    if s == 'Ff' and i < 20:
        t2 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('continuar [s/n]')).strip().upper()[0]
    if r == 'N':
        break
print(f'mais de 18 anos {t8}')
print(f'total temos {th} de homens')
print(f'e total de {t2} de mulheres com menos de 20')