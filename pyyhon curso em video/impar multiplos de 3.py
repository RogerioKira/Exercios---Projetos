s = 0
c = 0
for c in range (1,501,2):
    if c % 3 ==0:
        s = s +c
        c = c +1
print('soma {} valores {}'.format(c,s))