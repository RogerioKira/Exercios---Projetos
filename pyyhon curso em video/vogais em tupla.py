p = {'aprender', 'programas', 'linguagem', 'python'}
for r in p:
    print(f'\n na palavra {r.upper()} temos ', end='')
    for l in r:
        if l.lower() in 'aeiou':
            print(l, end= ' ')