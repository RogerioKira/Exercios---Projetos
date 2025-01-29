s = str(input('informe sexo[m/f]')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('invalidos')).strip().upper()[0]
print('sexo {} registrado'.format(s))