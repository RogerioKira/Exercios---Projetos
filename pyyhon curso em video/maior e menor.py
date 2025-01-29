a = int(input('primeiro:'))
b = int(input('segyndo'))
c = int(input('terceiro'))
m = a
if  b<a and b <c:
    m = b
if c<a and c<b:
    m = c
n = a
if  b>a and b >c:
    n = b
if c>a and c>b:
    n = c
print('maior {}' .format(n))
print('menor {}'.format(m))
