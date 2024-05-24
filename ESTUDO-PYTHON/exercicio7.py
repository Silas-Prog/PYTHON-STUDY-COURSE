#cartao de credito
grana = float(input("Informe a sua renda: "))
if grana < 2000:
    limite = 1000
elif grana >= 2000 and grana < 4000:
    limite = 2000

elif grana >= 4000 and grana <6000:
    limite = 3000

elif grana > 10000:
    limite = 3000
    print("consulte o gerente para ver a possibilidade de aumento do limite.")
print("O seu limite é de R$%.2f reais" % limite)

