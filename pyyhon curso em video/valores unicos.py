nu = list()
while True:
    n = int(input('digite'))
    if n not in nu:
        nu.append(n)
        print('valor adicionado')
    else:
        print('valor duplicado')
    r = str(input('continuar[S/N]'))
    if r in 'Nn':
        break
print(f'voce digitou {nu}')