c = ('zero', 'um', 'dois', 'tres', 'quatro',
     'cinco', 'seis', 'sete', 'oito', 'nove'
     ,'dez')
while True:
    n = int(input('digite entre 0 e 10'))
    if 0 <= n <= 10:
        break
    print('again', end=' ')
print(f'digitou {c[n]}')