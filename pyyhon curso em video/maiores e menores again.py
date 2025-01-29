r = 'S'
s = q = m = ma = me =0
while r in 'Ss':
    n = int(input('digite numero'))
    s += n
    q += 1
    if q ==1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me :
            me = n
    r = str(input('continuar[s/n]')).upper().strip()[0]
m = s/q
print('digitou {} numeros media {}'.format(q,m))
print('maior {} menor {}'.format(ma,me))