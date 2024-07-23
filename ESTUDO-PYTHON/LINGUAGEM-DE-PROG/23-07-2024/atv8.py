preco01 = float (input("Informe o preço do produto: "))
preco02 = float (input("Informe o preço do produto: "))
preco03 = float (input("Informe o preço do produto: "))
if preco01 < preco02 and preco01 < preco03:
  print ("O produto mais barato é o produto 1")
elif preco02 < preco01 and preco02 < preco03:
  print ("O produto mais barato é o produto 2")
else:
  print ("O produto mais barato é o produto 3")