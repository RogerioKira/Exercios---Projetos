from random import randint
i = ('pedra','papel','tesoura')
c = randint(0,2)
print('''opções:
[0] pedra
[1] papel
[2] tesoura''')
j = int(input('jogada'))
print('computador jogou {}'.format(i[c]))
print('jogador jogou {}'.format(i[j]))
if c ==0:
    if j ==0:
        print( ' empate')
    elif j ==1:
        print('jogador vence')
    elif j == 2:
        print('computador vence')
    else:
        print('invalido')
elif c == 1:
    if j ==0:
        print('computador vence')
    elif j ==1:
        print('empate')
    elif j == 2:
        print('jogador vence')
    else:
        print('invalido')
elif c ==2:
    if j == 0:
        print('jogador vence')
    elif j == 1:
        print('computador vence')
    elif j == 2:
        print('empate')
    else:
        print('invalido')