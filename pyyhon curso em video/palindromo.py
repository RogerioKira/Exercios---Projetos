f = str(input('frase')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j)-1,-1,-1):
    i+=j[l]
if i == j:
    print('palindromo')
else:
    print('nao palindromo')