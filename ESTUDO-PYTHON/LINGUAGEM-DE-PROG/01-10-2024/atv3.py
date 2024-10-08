idadema = 0
idademe = 10000
sal = 0
ts = 0
num = str(input("Deseja acessar o sistema? para sair 'Sair': "))
while num != "Sair":
    sa = float(input("Informe o seu salario: "))
    id = int(input("Informe a maior idade: "))
    di = int(input("Informe a menor idade: "))
    se = str(input("Informe o sexo. F ou M: "))
    if sa > 0:
        sal+=sa
        ts+=1
    if id > idadema:
        idadema = id
    elif id < idademe:
        idademe = di
    print("ts: ", ts)
    print("sal: ", sal)
    num = str(input("Deseja acessar o sistema? para sair 'Sair': "))
print("A média é: %i idade maior: %i idade menor: %i" %(sal/ts,idadema,idademe))