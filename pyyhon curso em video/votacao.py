def v(a):
    from datetime import date
    at = date.today().year
    i = at - a
    if i < 16:
        return f'com {i} anos: nao vota'
    elif 16 <= i < 18 or i > 65:
        return f'com {i} anos: opcional'
    else:
        return f'com {i} anos: obrigatorio'

nasc = int(input('em que ano naceu'))
print(v(nasc))