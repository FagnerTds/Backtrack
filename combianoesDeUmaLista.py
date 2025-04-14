def permutacao (nums):
  resultado = []

  def backtraking (caminho):
    if len(caminho) == len(nums):
      print (caminho)
      resultado.append(caminho[:])
      return
    
    for num in nums:
      if num in caminho:
        continue
      caminho.append(num)
      backtraking(caminho)
      caminho.pop()

  backtraking([])
  return resultado

print (permutacao ([4,7,9]))


  

