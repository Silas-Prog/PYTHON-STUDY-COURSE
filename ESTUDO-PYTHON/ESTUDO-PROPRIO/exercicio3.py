import time
#concatenar e strings dinamicas:
espaco = " "

nome=str(input("Informe o seu nome: "))
sobrenome=str(input("Informe o seu sobrenome: "))
time.sleep(1)
print(espaco)
time.sleep(1)
print("Aguarde estamos procurando seu cadastro.")
time.sleep(2)
print(espaco)
idade=int(input("Informe a sua idade: "))
time.sleep(1)
print(espaco)
time.sleep(1)
print("Agora você irá informar o seu genero:")
time.sleep(1)
genero=int(input("0 para feminino e 1 para masculino. "))
time.sleep(2)
print(espaco)
print("Aguarde estamos procurando seu cadastro.")
print(espaco)
time.sleep(2)
print("Processo de identificação concluido.")
print(espaco)
time.sleep(1)
if genero == 1:
    print("Bem vindo, Sr. ", nome + espaco + sobrenome)
elif genero == 0:
    print("Bem vinda, Sra. ", nome + espaco + sobrenome)
else:
    print("Algo não está certo.")
print(espaco)
time.sleep(2)
print("PARA SELECIONAR UM SERVIÇO DIGITE O NUMERO DE REFERENCIA:")
print("1. Habilitação.")
print("2. Media das notas escolares")
print("3. Titulo eleitoral.")
print("4. Permissão para sair do país")
servico=int(input("Serviço escolhido: "))
time.sleep(1)
print(espaco)
print("Aguarde!")
time.sleep(1)
print(espaco)
print("*EM BREVE TEREMOS MAIS SERVIÇOS DISPONIVEIS AO POVO BRASILEIRO.")
print(espaco)
print(espaco)
time.sleep(2)

if servico == 1:
    if idade >= 18:
        print("Você pode emitir sua carteira de habilitação! recomendamos que procure uma autoescola.")
    else: 
        print("Você não pode emitir sua habilitação.")
        time.sleep(1.5)
        print("Sua idade é menor que 18 anos, sendo assim, menor de idade.")

elif servico == 2:
    nota1=float(input("Informe a 1º nota:"))
    nota2=float(input("Informe a 2º nota:"))
    nota3=float(input("Informe a 3º nota:"))
    nota4=float(input("Informe a 4º nota:"))
    medianota=(nota1+nota2+nota3+nota4)/4
    print(espaco)
    time.sleep(2)
    print("Sua média é: ",medianota)

elif servico == 3:
    if idade >= 16:
        print("Você pode emitir o seu titulo eleitoral")
        time.sleep(1)
        print("procure o cartorio eleitoral mais proximo de sua casa")
        time.sleep(1)
        print("e exerça sua cidadania na proxima eleição!")

elif servico == 4:

    passaport = str(input("Você possui passaporte? sim ou nao"))

    if passaport == "sim" and idade >= 18:

        print("Você está autorizado a sair do pais.") 
    
    elif passaport == "nao":
 
        print("Você está não autorizado a sair do pais.") 
        print("Você precisa fazer o seu passaporte.")
    
    elif idade < 18:

        print("Você não pode sair do pais.")
        print("Você é menor de idade.")

else:

    print("Numero invalido, voce irá retornar ao menu inicial.")

print(espaco)
print(espaco)
