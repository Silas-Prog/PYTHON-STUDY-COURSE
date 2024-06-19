# função da multiplicação
def multiplica(num1, num2):
    return num1 * num2
mult = multiplica(100,50)
print(mult)
print("")

# função do positivo
def e_positivo(num):
    if num > 0:
        return True
    elif num < 0:
        return False
posi = e_positivo(0)
print(posi)
print("")

# função ao quadrado
def quadrado(num):
    return num**2
quad = quadrado(8)
print(quad)
print("")

# funcao de leitor de letras
def conta_constantes(string):
    return len(string)
leitor = conta_constantes("Silas Santos")
print(leitor)
print("")

# função número menor
def menorr(n1,n2,n3):
    if n1 < n2:
        menor = n1
    elif n2 < n3:
        menor = n2
    else:
        menor = n3
    return menor
nm = menorr(200,100,50)
print(nm)
print("")

# somar números pares
def somar(lista):
    soma = 0
    for item in lista:
        if item % 2 == 0:
            soma += item
    return soma
listar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sl = somar(listar)
print(sl)
print("")