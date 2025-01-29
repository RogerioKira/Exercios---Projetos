from datetime import date
a = int(input('ano:'))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 !=0 or a %400 ==0:
    print('o ano {} é bissexto'.format(a))
else:
    print('o ano {} nao é bissexto'.format(a))