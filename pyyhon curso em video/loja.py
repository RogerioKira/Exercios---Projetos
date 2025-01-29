p = float(input('preço'))
print('''Forma de pagamento
[1] dinhero/cheque
[2] cartao
[3] 2x cartao
[4] 3x ou mais vezes no cartao''')
o = int(input('qual opção'))
if o == 1:
    t = p - (p *10/100)
elif o == 2:
    t = p - (p *5 /100)
elif o == 3:
    t = p
    pa = t /2
    print('sua compra sera parcelada em 2x de {}'.format(pa))
elif o == 4:
    t = p + (p * 20 /100)
    tp = int(input('quantas parcelas'))
    pa = t/tp
    print('compra parcelada em {}x de {:.2f} com juros'. format(tp,pa))
else:
    t = 0
    print('invalido')
print('sua compra de {:.2f} vai custar {:.2f} '.format(p,t))