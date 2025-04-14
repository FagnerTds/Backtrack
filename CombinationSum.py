## Queremos encontrar todas as combinações de números do array nums que somam exatamente o valor target.

def combination (nums, target):
  resultado = []

  def backtrack(caminho, total, inicio):
    if total > target:
      return
    if total == target:
      resultado.append(caminho[:])
      return
    
    for i in range(inicio, len(nums)):
      num = nums[i]
      caminho.append(num)
      backtrack(caminho, total + num, i + 1) ##se eu quiser que o número se repita devo colocar apenas o i
      caminho.pop()

  backtrack([],0,0)
  return resultado
print(combination([1,2,3,4],5))
