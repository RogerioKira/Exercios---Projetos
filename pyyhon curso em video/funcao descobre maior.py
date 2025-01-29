from time import sleep

def m(* n):
    c = m = 0
    print('\n Analisando valores')
    for v in n:
        print(f'{v}', end='', flush=True)
        sleep(0.3)
        if c == 0:
            m = v
        else:
            if v > m:
                m = v
        c += 1
    print(f'foram informados {c} valores')
    print(f'o maior valor {m}')

m(2,9,4,5,7,1)