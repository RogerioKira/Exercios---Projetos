c = float(input('casa'))
s = float(input('salario'))
a = int(input('anos de financiamento'))
p = c/(a*12)
m = s *30 /100
print('pagar casa {:.2f} em {} anos'.format(c,a),end='')
print('prestaçao {:.2f}'.format(p))
if p <= m:
    print('emprestimo concedido')
else:
    print('negado')