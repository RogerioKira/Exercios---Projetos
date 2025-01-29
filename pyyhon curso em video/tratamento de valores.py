n = c = s =0
n = int(input('digite numero 999 para parar'))
while n !=999:
    s += n
    c += 1
    n = int(input('digite 999 para parar'))
print('vc digitou {} numeros e a soma da {}'.format(c,s))