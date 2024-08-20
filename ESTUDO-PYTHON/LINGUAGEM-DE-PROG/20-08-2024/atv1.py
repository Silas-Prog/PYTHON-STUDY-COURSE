s = 0
for i in range(15):
    idade = int(input("Informe a idade: "))
    if(idade>=18):
        s += 1
if(s>0):
    print("A quantidade de pessoa com idade igual ou superior a 18 é", s)
else:
    print("")
