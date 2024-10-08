numpos = 1
numneg = 0
num = int(input("Informe um número: "))
while num != 1000:
    if num > 0:
        numpos *= num
    elif num < 0:
        numneg += num
    num = int(input("Informe um número: "))
print("O total dos positivos é %i" %(numpos))
print("O total dos negativos é %i" %(numneg))
