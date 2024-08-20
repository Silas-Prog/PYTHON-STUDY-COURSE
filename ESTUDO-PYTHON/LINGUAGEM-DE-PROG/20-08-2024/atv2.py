M = 0
somamasc = 0
F = 0
somafem = 0
somaidade = 0
for i in range(10):
    sexo = input("Informe o seu sexo. M ou F: ")
    idade = int(input("Informe a sua idade: "))
    if( sexo == 'M' or sexo == 'm'):
        M = M + 1
        somamasc+=idade
    else:
        F+=1
        somafem+=idade
    somaidade+=idade
print("A média das idades informadas é %s, a média das idades das pessoas do sexo masculino é %s e a  média das idades das pessoas do sexo feminino é %s" %(somaidade/10, somamasc/M, somafem/F))     