def no(*n, sit=False):
    """erro"""

    r = dict()
    r['total'] = len(n)
    r['maior'] = len(n)
    r['menor'] = len(n)
    r['media'] = len(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situaçao'] = 'BDA'
        elif r['media'] >= 5:
            r['situaçao'] = 'Razoavel'
        else:
            r['situcao'] = 'ruim'
    return r

res = no(5.5,2.5,1.5, sit=True)
print(res)
help(no)