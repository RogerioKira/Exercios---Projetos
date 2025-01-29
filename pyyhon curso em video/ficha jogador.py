def f(j='<desconhecido>', gol=0):
    print(f'jogador {j} fez {gol} gol(s) no campeonato')

n = str(input("nome do jogado"))
g = str(input("numero gols"))
if g.isnumeric():
    g = int(g)
else:
    g =0
if n.strip() == '':
    f(gol=g)
else:
    f(n,g)