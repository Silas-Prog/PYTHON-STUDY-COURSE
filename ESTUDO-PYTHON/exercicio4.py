nome = input("Informe o seu nome: ")
gen = int(input("Informe o seu genero, Feminino 0 e Masculino 1: "))
saudm = "Ola, Sr. "
saudf = "Ola, Sra. "
if(gen == 0):
    print(saudf + nome)
elif(gen ==1):
    print(saudm + nome)