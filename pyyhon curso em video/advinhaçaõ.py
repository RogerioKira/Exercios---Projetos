from random import randint
from time import sleep
c = randint(0,5)
print('-=-' *20)
print('pense entre 0 e 5')
print('-=-' *20)
j = int(input( 'qual numero'))
sleep(3)
if j == c:
    print('parabens')
else:
    print('era {} nao {}'.format(c,j))