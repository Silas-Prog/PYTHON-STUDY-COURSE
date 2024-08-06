qalunos = int(input("Informe quantos alunos tem na sala: "))
somaidade = 0
for i in range(qalunos):
    idade = int(input("Informe a sua idade: "))
    somaidade = somaidade + idade
print("A soma das idades é %s" %(somaidade))