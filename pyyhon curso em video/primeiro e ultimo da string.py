f = str(input('digite:')).upper().strip()
print('letar a {}' 'vezes na frase' .format(f.count('A')))
print('a apareceu primeiro em {}' .format(f.find('A')+1))
print('ultima ves de A {}'.format(f.rfind('A')+1))