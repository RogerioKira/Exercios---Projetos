print('\033[4;30;45mola\033[m')

a = 3
b = 5
print('valores \033[32m{}\033[m e \033[31m{}\033[31m'.format(a,b))

c = {'limpa':'\033[m', 'azul': '\033[34m',
     'amarelo':'\033[7:30',
     'preto':'\033[7:30m'}
n = 'nigga'
print('nome{}{}'.format(c['preto'], n ,c['limpa']))

