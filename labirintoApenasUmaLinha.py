def labirinto_avancado(labirinto):
    resultado = []
    caminho = []
    linhas_visitadas = {}

    def backtrack (x,y):
        if x < 0 or y < 0 or x >= len(labirinto) or y >= len(labirinto[0]):
            return
        if labirinto[x][y] == 1:
            return
        if (x,y) in caminho:
            return
        linhas_visitadas[x] = linhas_visitadas.get(x,0) + 1
        if linhas_visitadas[x] > 3:
            linhas_visitadas[x] -= 1
            return
        
        caminho.append((x,y))

        if x == len(labirinto) -1 and y == len(labirinto[0]) - 1:
            resultado.append(caminho[:])
        
        else:
            backtrack(x + 1, y)
            backtrack(x - 1, y)
            backtrack(x, y + 1)
            backtrack(x, y - 1)

        caminho.pop()
        linhas_visitadas[x] -= 1

    backtrack(0,0)
    return resultado

labirinto = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0]
]

caminhos = labirinto_avancado(labirinto)

for c in caminhos:
    print(c)
    
