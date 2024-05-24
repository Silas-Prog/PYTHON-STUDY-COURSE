import time

time.sleep(1)
print("OLá, tudo bem?")
time.sleep(1.7)
print("Esse é o serviço inteligente de array do python.")
time.sleep(2)
print("Informe o serviço que você deseja abaixo.")
print(" ")
print("      SERVIÇOS:")
print("1. Substituir nome nos array")
print(" ")
num = int(input("Informe o número: "))
time.sleep(2)
print(" ")
print("serviço interessante.")
time.sleep(1)
print("Em breve teremos mais serviços a disposição")
time.sleep(2)
nomes = ["Silas", "Moral", "Mona","Lavi", "", "", ""]
if(num == 1):

    ind = int(input("Informe o índice: "))
    nom = str(input("Informe o nome: "))
    nomes[ind] = nom
    print("NOVO: %s" % nomes)