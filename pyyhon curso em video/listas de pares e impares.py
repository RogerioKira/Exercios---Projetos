n = [[], []]
v = 0
for c in range(1,8):
    v = int(input(f'digite o {c}o. valor:'))
    if v % 2 == 0:
        n[0].append(v)
    else:
        n[1].append(v)
n[0].sort()
n[1].sort()
print(f'valores pares foram:{n[0]}')
print(f'valores impares digitados:{n[1]}')