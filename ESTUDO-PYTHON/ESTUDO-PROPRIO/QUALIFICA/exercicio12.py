valor = float(input("Informe o valor que você deseja sacar: "))

nota_200 = 0
nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
moeda1 = 0
moeda50 = 0
moeda25 = 0
moeda10 = 0
moeda5 = 0

while valor > 0:
    while valor >= 200:
        nota_200 = nota_200 + 1
        valor = valor - 200

    while valor >= 100:
        nota_100 = nota_100 + 1
        valor = valor - 100

    while valor >= 50:
        nota_50 = nota_50 + 1
        valor = valor - 50

    while valor >= 20:
        nota_20 = nota_20 + 1
        valor = valor - 20

    while valor >= 10:
        nota_10 = nota_10 + 1
        valor = valor - 10

    while valor >= 5:
        nota_5 = nota_5 + 1
        valor = valor - 5

    while valor >= 2:
        nota_2 = nota_2 + 1
        valor = valor - 2

    while valor >= 1:
        moeda1 = moeda1 + 1
        valor = valor - 1

    while valor >= 0.5:
        moeda50 = moeda50 + 1
        valor = valor - 0.5

    while valor >= 0.25:
        moeda25 = moeda25 + 1
        valor = valor - 0.25
        
    while valor >= 0.10:
        moeda10 = moeda10 + 1
        valor = valor - 0.10

    while valor >= 0.05:
        moeda5 = moeda5 + 1
        valor = valor - 0.05

if nota_200 > 0:
    print("200: %i " % nota_200)
elif nota_100 > 0: 
    print("100: %i " % nota_100)
elif nota_50 > 0:
    print("50: %i " % nota_50) 
elif nota_20 > 0:
    print("20: %i " % nota_20)
elif nota_10 > 0:
    print("10: %i " % nota_10) 
elif nota_5 > 0:
    print("5: %i " % nota_5)  
elif nota_2 > 0:
    print("2: %i " % nota_2) 
elif moeda1 > 0:
    print("MOEDA 1 real: %i" % moeda1)
elif moeda50 > 0:
    print("MOEDA 50 centavos: %i" % moeda50)
elif moeda25 > 0:
    print("MOEDA 25 centavos: %i" % moeda25)
elif moeda10 > 0:
    print("MOEDA 10 centavos: %i" % moeda10)
elif moeda5 > 0:
    print("MOEDA 5 centavos: %i " % moeda5)

