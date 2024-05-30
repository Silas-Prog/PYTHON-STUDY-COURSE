lista = [55, 98, 30, 10]

maior_valor = 0
for n in lista:
    if n > maior_valor:
        maior_valor = n
print("o maior valor é %d " % maior_valor)

menor_valor = maior_valor
for i in lista:
    if i < menor_valor:
        menor_valor = i
print("o menor valor é %d " % menor_valor)