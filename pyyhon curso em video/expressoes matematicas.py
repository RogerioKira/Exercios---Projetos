e = str(input('digitou expressoes:'))
p = []
for s in e:
    if s =='(':
        p.append('(')
    elif s == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('valido')
else:
    print('errado')