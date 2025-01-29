def l(msg):
    ok = False
    v = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            v = int(n)
            ok = True
        else:
            print('erro')
        if ok:
            break
    return v

n = l('digite numeros')
print(f'vc digitou {n}')