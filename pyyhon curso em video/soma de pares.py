s = 0
c = 0
for c in range (1,7):
    n = int(input('digite {}'.format(c)))
    if n % 2 ==0:
        s += n
        c += 1
print('numero {} numeros pares e soma {}'.format(c,s))