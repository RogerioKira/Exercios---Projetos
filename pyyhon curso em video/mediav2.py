n1 = float(input('primeiro'))
n2 = float(input('segundo'))
m = (n1 + n2 ) /2
print('media {:.1f}'.format(m))
if 7> m >= 5:
    print('recuperaçao')
elif m<5:
    print('reprovado')
elif m >=7:
    print('aprovado')