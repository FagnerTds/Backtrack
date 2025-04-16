def desenha_tabuleiro(tabuleiro):
  for linha in tabuleiro:
    print("| " + " | ".join(linha) + " |")
  print()

def movimentos_validos(tabuleiro, linha, coluna):
  return (
    0 <= linha < len(tabuleiro)
    and 0 <= coluna < len(tabuleiro[0])
    and tabuleiro[linha][coluna] == " "
  )

def destino(linha, coluna):
  return linha == 0 and coluna == 3

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
  melhor_profundidade = float("inf")
  melhor_linha = linha_atual
  melhor_coluna = coluna_atual

  direcoes = [(0,-1),(0,1), (-1,0), (1,0)] #esquerda, direita, cima, baixo

  for dx, dy in direcoes:
    nova_linha = linha_atual + dx
    nova_coluna = coluna_atual +dy

    if movimentos_validos(tabuleiro, nova_linha, nova_coluna):
      if destino(nova_linha,nova_coluna):
        return nova_linha, nova_coluna, profundidade + 1
      
      tabuleiro[nova_linha][nova_coluna] = "*"
      _,_, nova_profundidade = proximo_movimento(tabuleiro, nova_linha, nova_coluna, profundidade + 1)
      tabuleiro[nova_linha][nova_coluna] = " "

      if nova_profundidade < melhor_profundidade:
        melhor_profundidade = nova_profundidade
        melhor_linha = nova_linha
        melhor_coluna = nova_coluna

  return melhor_linha, melhor_coluna, melhor_profundidade

def main():

  tabuleiro = [
    [" ", " ", "x", " "], 
    [" ", " ", " ", " "], 
    [" ", " ", " ", "x"], 
    ["*", "x", "x", " "]
  ]

  linha_atual, coluna_atual = 3,0

  desenha_tabuleiro(tabuleiro)

  print ("*************************************************")
  print ("*************************************************")


  while not destino(linha_atual, coluna_atual):
    nova_linha, nova_coluna, profundidade = proximo_movimento(tabuleiro, linha_atual, coluna_atual, 0)

    if profundidade == float("inf"):
      print ("Não existe um caminho possível até o destino ;(")
      break

    linha_atual, coluna_atual = nova_linha, nova_coluna
    tabuleiro[linha_atual][coluna_atual] = "*"

    desenha_tabuleiro(tabuleiro)
    if not destino(linha_atual, coluna_atual):
      print(f"Este movimento foi para ({linha_atual}, {coluna_atual}) - faltam {profundidade -1 } passos até o destino\n\n")
    else:
      print ("PARABÉNS VOCÊ CHEGOU AO DESTINO !!!!!!!")
    

main()





