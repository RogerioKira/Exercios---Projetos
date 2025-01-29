p = float(input('pseo'))
a = float(input('altura'))
imc = p/(a **2)
print(' IMC de {:.1f}'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc <25:
    print('media')
elif 25 <= imc <30:
    print('sobrepeso')
elif 30 <= imc < 40:
    print('obesidade')
elif imc >= 40:
    print('obsidade morbida')