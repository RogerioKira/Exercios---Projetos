from random import randint
c = randint(0,10)
print('adivinhe entre 1 e 10')
a = False
p = 0
while not a:
    j = int(input('palpite'))
    p +=1
    if j == c:
        a = True
    else:
        if j < c:
            print('mais,tente de novo')
        elif j > c:
            print('menos, tente de novo')
print('parabens demorou {} tentativas'.format(p))