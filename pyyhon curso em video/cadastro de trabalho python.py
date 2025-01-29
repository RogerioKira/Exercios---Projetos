from datetime import datetime
d = dict()
d['nome'] = str(input('nome:'))
n = int(input('ano de nacimento:'))
d['idade'] = datetime.now().year-n
d['ctps'] = int(input('carteira de trabalho(0 caso nao):'))
if d['ctps'] !=0:
    d['contratação'] = int(input('ano de contratacao'))
    d['salario'] = float(input('salario'))
    d['aponsentadoria'] = d['idade'] + ((d['contratação'] + 35) - datetime.now().year)
for k, v in d.items():
    print(f'{k} tem o valor {v}')