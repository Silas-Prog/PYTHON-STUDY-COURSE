numum = int(input("Informe o número de vezes que vou repetir o for: "))
s = 0
if(numum>0):
    for i in range(numum):
        num = float(input("Informe um número real: "))
        s += num
    print("A média dos números é %s." %(s/numum))
else:
    print("O número de repetição é menor que 1.")