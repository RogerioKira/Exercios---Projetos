from datetime import date
a = date.today().year
n = int(input('nacimento'))
i = a - n
print('atleta tem {} anos'.format(i))
if i <= 9:
    print('mirim')
elif i <= 14:
    print('infantil')
elif i <= 19:
    print('junior')
elif i <=25:
    print('senior')
else:
    print('master')