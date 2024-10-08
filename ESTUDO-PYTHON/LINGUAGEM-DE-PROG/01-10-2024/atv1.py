tpost = 0
tneg = 0
vtotal = 0
totalnum = 0
pesq = str(input("Deseja informe um número? para finalizar escreva 'fim'."))
while pesq != "fim":
    num = int(input("Informe um número: "))
    vtotal += num
    totalnum += 1
    if num > 0:
        tpost += 1
    elif num < 0:
        tneg += 1
    pesq = str(input("Deseja continuar? para finalizar escreva 'fim'."))
print("A média aritmetica é: %i, a quantidade de valores positivos é: %i, a quantidade de valores negativos é: %i." %(vtotal/totalnum, tpost, tneg))
    