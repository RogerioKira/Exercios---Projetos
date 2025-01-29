n = int(input('numero inteiro'))
print('escolha base: '
      '[1] binario'
      '[2] octal'
      '[3] hexadecimal')
o = int(input('opção:'))
if o ==1:
    print('{} binario = {}'.format(n,bin(n)[2:]))
elif o ==2:
    print('{} octal = {}'.format(n,oct(n)[2:]))
elif o ==3:
    print('{} hexa = {}'.format(n,hex(n)[2:]))
else:
    print('erro')