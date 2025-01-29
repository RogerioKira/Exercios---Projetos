n1 = int(input('primeiro'))
n2 = int(input('segundo'))
o = 0
while o != 5:
    print('''   [1]soma
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair
    ''')
    o = int(input('qual opçao'))
    if o == 1:
        s =n1 + n2
        print('soma entre {} + {} é {}'.format(n1,n2,s))
    elif o == 2:
        p = n1 * n2
        print ('o resultado de {} x {} é {}'.format(n1,n2,p))
    elif o == 3:
        if n1 > n2:
            m = n1
        else:
            m = n2
        print('entre {} e {} maior valor {}'.format(n1,n2,m))
    elif o == 4:
        print('informe numeros')
        n1 =int(input('primeiro'))
        n2 =int(input('segundo'))
    elif o == 5:
        print('fim')
    else:
        print('erro')
print('fim ,vai tomar cu')