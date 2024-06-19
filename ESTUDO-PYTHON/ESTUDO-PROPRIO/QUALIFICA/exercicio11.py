numero = int(input("Informe um número quaisquer: "))

divid = 0

contador = numero

while contador > 0:
    
    if contador % numero == 0:
        divid = divid + 1
    
    contador = contador - 1

if divid ==2:
   print("O numero %s é primo" % numero)
else:
    print("O numero %s não é primo" % numero)