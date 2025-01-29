j = dict()
p = list()
j['nome'] = str(input('nome do jogador'))
t = int(input(f'quantas partidas {j["nome"]} jogou'))
for c in range(0,t):
    p.append(int(input(f' quantos gols {c}')))
j['gols'] = p[:]
j['total'] = sum(p)
print(j)
for k,v in j.items():
    print(f'o campo {k} tem valor {v}')
print(f'o jogador{j["nome"]} jogou {len(j["gols"])} partidas')
for i, v in enumerate(j['gols']):
    print(f' => na partida {i}, fez {v} gols')
print(f'foi um total de {j["total"]} gols')