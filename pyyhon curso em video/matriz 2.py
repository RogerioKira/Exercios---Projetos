m = [[0,0,0],[0,0,0],[0,0,0]]
s = ma = sc =0
for l in range(0,3):
    for c in range(0,3):
        m[l][c]= int(input(f'digite valor para [{l},{c}]'))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{m[l][c]:^5}]', end='')
        if m[l][c] % 2 == 0:
            s += m[l][c]
    print()
print(f'soma dos valores  pares {s}')
for l in range(0,3):
    sc += m[l][2]
print(f'soma terceira {sc}')
for c in range(0,3):
    if c == 0:
        ma = m[1][c]
    elif m[1][c]>ma:
        ma = m[1][c]
print(f'maior da segunda {ma}')