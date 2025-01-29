from time import sleep

def c(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f' contagem de {i} ate {f} de {p} em {p}')
    sleep(2.5)

    if i<f:
        co = i
        while co <= f:
            print(f'{co}', end='', flush=True)
            sleep(0.5)
            co += p
        print('Fim')
    else:
        co = 1
        while co >= f:
            print(f'{co}', end='', flush=True)
            sleep(0.5)
            co -= p
        print('Fim')

c(1,10,1)
c(10,0,2)
print('personalize a contagem')
ini = int(input('inicio'))
fim = int(input('fim'))
pas = int(input('passo'))
c(ini,fim,pas)