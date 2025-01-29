n = int(input('numero:'))
tot = 0
for c in range(1,n +1):
    if n % c ==0:
        print(end='')
        tot +=1
    else:
        print(end='')
    print('{} '.format(c), end='')
print('\n numero {} e divisivel {} vezes'.format(n,tot))
if tot == 2:
    print('primo')
else:
    print('nao primo')