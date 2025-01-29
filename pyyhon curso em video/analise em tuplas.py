n = (int(input('digite numero')),
     int(input('digite numero')),
     int(input('digite numero')),
     int(input('digite numero')))
print(f'digitou os valores {n}')
print(f'valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'valor 3 apareceu na {n.index(3)+1} posicao')
else:
    print('sem 3')
print('valores digitados pares ', end= ' ')
for m in n:
    if m %2 == 0:
        print(m,end=' ')