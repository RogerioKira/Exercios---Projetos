from datetime import date
a = date.today().year
n = int(input('nacimento'))
i = a - n
print('nacido {} tem {} anos em {}'.format(n,i,a))
if i ==18:
    print('alistese')
elif i <18:
    s = 18 -i
    print('falta {} anos para alistar'.format(s))
    print('alistamento sera em {}'.format(a))
elif i >18:
    s = i - 18
    print('faz {} desde o alistamento'.format(s))
    an =a - s
    print('alistamento foi em {}'.format(an))