ma = 0
me =0
for p in range(1,6):
    pe = float(input('peso {} pessoa'.format(p)))
    if p ==1:
        ma = pe
        me = pe
    else:
        if pe > ma:
            ma = pe
        if pe< me:
            me = pe
print('maior peso foi de {}'.format(ma))
print('menor peso lido {}'.format(me))