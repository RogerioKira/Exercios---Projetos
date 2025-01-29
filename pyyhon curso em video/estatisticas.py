t = tm = m = c = 0
b = ' '
while True:
    p = str(input('nome'))
    pr = float(input('preço'))
    c += 1
    t += pr
    if pr > 1000:
        tm += 1
    if c == 1 or pr <m:
        m = pr
        b = pr
    r = ' '
    while r not in 'SN':
        r = str(input('continuar')).strip().upper()[0]
    if r == 'N':
        break
print('{:-^40}'.format('fim'))
print(f'total {t:.2f}')
print(f'temos {tm} produtos')
print(f'mais barato foi {b} que custa {m}')