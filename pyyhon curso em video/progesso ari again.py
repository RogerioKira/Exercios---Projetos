print('gerador de pa')
p = int(input('primeiro'))
r = int(input('razao'))
t = p
c = 1
while c <= 10:
    print('{} ->'.format(t), end= ' ')
    t += r
    c +=1
print()