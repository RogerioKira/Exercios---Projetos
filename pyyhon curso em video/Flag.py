s = c =0
while True:
    n = int(input('digite 999 para parar'))
    if n == 999:
        break
    c += 1
    s += n
print(f'soma {c} valores foi {s}')