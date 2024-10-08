t = 0
num = int(input("Informe um número: "))
while num != 0:
    if num > 99 and num < 1001:
        t+=1
    num = int(input("Informe um número: "))
print("A quantidade de número entre 100 e 1000 é %i" %(t))
    