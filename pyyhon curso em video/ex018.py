g = list()
d = list()
ta = te = 0
for c in range(0,3):
    d.append(str(input('nome')))
    d.append(int(input('idade')))
    g.append(d[:])
    d.clear()

for p in g:
    if p[1]>=21:
        print(f'{p[0]} e maior de idade')
    else:
        print(f'{p[0]} menor de idade')