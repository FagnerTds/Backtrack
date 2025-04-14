def backtraking (numeros):
  
  if len(numeros) == 3:
    print (numeros)
    return
  
  for i in range(1,4):
    if i not in numeros:
      numeros.append(i)
      backtraking(numeros)
      numeros.pop()

backtraking([])

