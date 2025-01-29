from time import sleep
c = ('\033[m',
     '\033[0;30;41',
     '\033[m030,42',
     '\033[0;30;43',
     '\033[0;30;44',
     '\033[0;30;45',
     '\033[7;30m');

def a(c):
    t(f'acessando comando \'{c}\'', 4)
    print(c[6], end='')
    help(c)
    print(c[0], end='')
    sleep(2)

def ti(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print(c[0], end='')
    sleep(1)

comando = ''