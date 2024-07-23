n1 = float(input("Informe a sua 1º nota: "))
n2 = float(input("Informe a sua 2º nota: "))
n3 = float(input("Informe a sua 3º nota: "))
n4 = float(input("Informe a sua 4º nota: "))
m = n1+n2+n3+n4/4
if(m>6):
    print("APROVADO. A sua média é %s." %(m))
elif(m>=5 and m<6):
    print("RECUPERAÇÃO. A sua média é %s." %(m))
else: 
    print("REPROVADO. A sua média é %s." %(m))