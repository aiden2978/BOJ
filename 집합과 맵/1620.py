N, M = map(int, input().split( ))

pokemon = {}
for i in range(26):
    pokemon.update({str(input()):str(i+1)})

pokemonReverse = dict(map(reversed, pokemon.items()))
pokemon.update(pokemonReverse)

for _ in range(M):
    print(pokemon[str(input())])