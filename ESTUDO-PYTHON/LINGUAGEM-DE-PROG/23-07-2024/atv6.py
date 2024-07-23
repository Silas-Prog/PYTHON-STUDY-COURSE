print("SISTEMA DE INTELIGÊNCIA DA POLICIA")
print("")
print("Responda com Sim ou Nao.")
p11 = str(input("Telefonou para a vítima?: "))
p22 = str(input("Esteve no local do crime?: "))
p33 = str(input("Mora perto da vítima?: "))
p44 = str(input("Devia para a vítima?: "))
p55 = str(input("Já trabalhou com a vítima?: "))

p1 = p11.upper()
p2 = p22.upper()
p3 = p33.upper()
p4 = p44.upper()
p5 = p55.upper()

x = 0
if(p1=="SIM"):
    x = x + 1
if(p2=="SIM"):
    x = x + 1
if(p3=="SIM"):
    x = x + 1
if(p4=="SIM"):
    x = x + 1
if(p5=="SIM"):
    x = x + 1

if(x==2):
    print("Você é suspeito.")
elif(x==3 or x==4):
    print("Você é Cúmplice.")
elif(x==5):
    print("Você é Assassino.")
else: 
    print("Você é inocente")

