l = ('lapis',1.75,
     'boracha',2
     ,'caderno',15.60,
     'estojo', 34,
     'transferidos',4.20)
for p in range(0,len(l)):
    if p % 2 == 0:
        print(f'{l[p]:.<30}', end='')
    else:
        print(f'R${l[p]:7.2f}')
