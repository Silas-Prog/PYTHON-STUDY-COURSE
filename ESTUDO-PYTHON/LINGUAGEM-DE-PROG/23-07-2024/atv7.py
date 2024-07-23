lado1 = float (input("Informe o lado 1: "))
lado2 = float (input("Informe o lado 2: "))
lado3 = float (input("Informe o lado 3: "))
if lado1 < 0 or lado2 < 0 or lado3 < 0:
  print ("Não é um triângulo")
if lado1 == lado2 and lado2 == lado3:
  print ("Triângulo Equilátero")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print ("Triângulo Escaleno")
else:
    print ("Triângulo Isósceles")