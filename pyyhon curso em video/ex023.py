def p(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

nu = int(input('digite numeros'))
if p(nu):
    print('é par')
else:
    print('nao e par')