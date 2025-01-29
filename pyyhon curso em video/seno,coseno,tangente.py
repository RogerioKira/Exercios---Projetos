from math import radians,sin,cos,tan
a = float(input('angulo:'))
s = sin(radians(a))
print('angulo {} seno {:.2f}'.format(a,s))
c = cos(radians(a))
print('angulo {} coseno {:.2f}'.format(a,c))
t = tan(radians(a))
print('angulo {} tangente {:.2f}'.format(a,t))