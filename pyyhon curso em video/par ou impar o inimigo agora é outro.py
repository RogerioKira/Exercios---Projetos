from random import randint
v = 0
while True:
    j = int(input('digite valor'))
    c = randint(0,10)
    t = j + c
    ti = ' '
    while ti not in 'PI':
        ti = str(input('par ou impar[P/I]')).strip().upper()[0]
    print(f'jogou {j} e a maquina {c}, total {t}', end= ' ')
    print('deu par' if t % 2 == 0 else 'impar')
    if ti == 'P':
        if t % 2 == 0:
            print('venceu')
            v += 1
        else:
            print('perdeu')
            break
    elif ti == 'I':
        if t % 2 == 1:
            print('venceu')
            v += 1
        else:
            print('perdeu')
            break
    print('de novo')
print(f'fim ,vitorias humanas {v} vezes')