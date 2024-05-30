nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))
gen = int(input("Informe o seu genero: fem = 0 e masc = 1: "))
grana = float(input("Informe quanto dinheiro você tem na poupança: "))
salario = float(input("Informe o seu salario: "))
porcentagem = 10

if(gen ==1):
    print("Ola, Sr. %s, você tem %i anos." %(nome, idade))
elif(gen ==0):
    print("Ola, Sra. %s, você tem %i anos." %(nome, idade))

aumento = salario+(salario*(porcentagem/100))
juros = grana / 20
cartaocredito = 2009.41
print("Você tem R$%.2f reais na sua poupança, o rendimento foi de R$%.2f reais, e a fatura do seu cartão de credito é de R$%.2f reais." % (grana, juros, cartaocredito))
print("O saldo atual da sua conta poupança com o rendimnte é de ", grana + juros)
print("O seu novo salario é de R$%.2f" % aumento)
grana = grana - cartaocredito + aumento

print("O saldo atual da sua conta poupança é de ", grana)

if aumento > 1800:
    print("Lembre-se que você tem que pagar o imposto de renda.")

