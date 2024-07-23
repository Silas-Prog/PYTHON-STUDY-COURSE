km = int(input("Informe a sua velocidade: "))
if km > 80:
    print("Você foi multado, o valor da multa é R$%.2f" %((km-80)*5))
else:
    print("Você não foi multado, parabens!")