import time
espaco = ""
c = 0
x = 0
print("Ola, seja bem vindo ao sistema educacional do Colegio Dom Pedro II.")
print(espaco)
print("aguarde")
nome = str(input("Informe o seu nome: "))
time.sleep(1)
sobrenome = str(input("Informe o seu sobrenome: "))
time.sleep(1) 
idade = int(input("Informe a sua idade: "))
time.sleep(1)
seriaescolar = str(input("Informe a sua série: "))
time.sleep(1)
situacaoescolar = str(input("Informe se é fundamental ou medio."))
time.sleep(1)
print("Aguarde.. estamos analisando seus dados")
time.sleep(2)
print("Analise concluida")
print("O senhor se chama %s %s, tem %i anos está na %sº do ensino %s" %(nome , sobrenome , idade , seriaescolar , situacaoescolar))
print("Pronto, agora vamos entra na interfase de cadastro de alunos! *PARA PARAR DE CADASTRAR DIGITE parar")
while(nom or idade or serie != "parar"):
    nom = str(input("Informe o nome do aluno(a): "))
    idade = str(input("Informe a idade do aluno(a): "))
    serie = str(input("Informe a série do aluno(a): "))
    nom = nome
    idade = idadea
    serie = sserie
    if(nom or idade or serie != "parar"):
        list1 = [nom, idadea, sserie]
        print(list1)
        if(nom != nome or idade != idadea or serie != sserie):
            list2 = [nome, idade, serie]
            print(list2)





