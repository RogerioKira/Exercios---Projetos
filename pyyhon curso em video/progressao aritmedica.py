p = int(input('termo:'))
r = int(input('razao'))
d = p + (10-1) * r
for c in range(p,d + r ,r):
    print('{}'.format(c),end='→ ')
print('fim')