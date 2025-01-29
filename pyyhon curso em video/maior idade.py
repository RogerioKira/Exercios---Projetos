from datetime import date
a = date.today().year
t =0
tm =0
for p in range(1,8):
    n = int(input('ano de nacimento'.format(p)))
    i = a - n
    if i >= 21:
        t += 1
    else:
        tm += 1
print('tivemos {} maiores de idade'.format(t))
print('tivemos {} menores de idade'.format(tm))