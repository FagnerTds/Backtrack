def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("| " + " | ".join(linha) + " |")
    print()

def movimento_valido(tabuleiro, linha, coluna):
    return (
        0 <= linha < len(tabuleiro)
        and 0 <= coluna < len(tabuleiro[0])
        and tabuleiro[linha][coluna] == " "
    )

def chegou_destino(linha, coluna):
    return linha == 0 and coluna == 3

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
    melhor_profundidade = float("inf")
    melhor_linha, melhor_coluna = linha_atual, coluna_atual

    direcoes = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in direcoes:
        nova_linha = linha_atual + dx
        nova_coluna = coluna_atual + dy

        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            if chegou_destino(nova_linha, nova_coluna):
                return nova_linha, nova_coluna, profundidade + 1

            tabuleiro[nova_linha][nova_coluna] = "*"  # Marca como visitado
            _, _, nova_profundidade = proximo_movimento(
                tabuleiro, nova_linha, nova_coluna, profundidade + 1
            )
            tabuleiro[nova_linha][nova_coluna] = " "  # Desmarca

            if nova_profundidade < melhor_profundidade:
                melhor_linha = nova_linha
                melhor_coluna = nova_coluna
                melhor_profundidade = nova_profundidade

    return melhor_linha, melhor_coluna, melhor_profundidade

def main():
    tabuleiro = [
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        ["*", " ", "X", " "]
    ]

    linha_atual, coluna_atual = 3, 0

    mostrar_tabuleiro(tabuleiro)

    while not chegou_destino(linha_atual, coluna_atual):
        nova_linha, nova_coluna, profundidade = proximo_movimento(tabuleiro, linha_atual, coluna_atual, 0)

        if profundidade == float("inf"):
            print("Não há caminho possível até o destino!")
            break

        linha_atual, coluna_atual = nova_linha, nova_coluna
        tabuleiro[linha_atual][coluna_atual] = "*"
        print(f"Movimento para ({linha_atual}, {coluna_atual}) - Profundidade: {profundidade}")
        mostrar_tabuleiro(tabuleiro)

main()