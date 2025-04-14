# Você tem uma matriz 2D (labirinto) onde:
# 0 representa um caminho livre,
# 1 representa uma parede,
# Você começa no canto superior esquerdo [0][0] e precisa chegar ao canto inferior direito [n-1][n-1].
# Só pode se mover pra cima, baixo, esquerda ou direita (sem diagonais), e não pode passar por cima de 1.

def encontrar_caminhos(labirinto):
    n = len(labirinto)
    caminho = []
    resultado = []

    def backtrack(x, y):
        # Verificações de limites e paredes
        if x < 0 or y < 0 or x >= n or y >= n:
            return
        if labirinto[x][y] == 1:
            return
        if (x, y) in caminho:
            return

        # Adiciona posição atual ao caminho
        caminho.append((x, y))

        # Se chegou ao destino, adiciona cópia do caminho ao resultado
        if x == n - 1 and y == n - 1:
            resultado.append(caminho[:])
        else:
            # Move em 4 direções
            backtrack(x + 1, y)  # baixo
            backtrack(x - 1, y)  # cima
            backtrack(x, y + 1)  # direita
            backtrack(x, y - 1)  # esquerda

        # Volta (backtrack)
        caminho.pop()

    backtrack(0, 0)
    return resultado

# Exemplo de labirinto:
labirinto = [
    [0, 0, 1],
    [1, 0, 1],
    [1, 0, 0]
]

# Chamada
caminhos = encontrar_caminhos(labirinto)

# Exibir todos os caminhos encontrados
for c in caminhos:
    print(c)