v = float(input('velocidade do carro'))
if v > 80:
    print ('multa')
    m = (v-80) * 7
    print('pague {:.2f}'.format(m))
print('bom dia')