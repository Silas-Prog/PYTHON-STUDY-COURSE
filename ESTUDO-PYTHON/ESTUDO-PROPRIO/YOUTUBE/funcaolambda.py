preco = 1000

def calcular_imposto(preco):
    return preco * 0.3
print(calcular_imposto(preco))
print("")
calcular_imposto2 = lambda p: p * 0.3
# o primeiro " p " recebe uma informação, e retorna o p apos os dois pontos como resposta executando a operação que estiver no lugar.
print(calcular_imposto2(10000))
print("")
precos = [100, 500, 10, 25]
impostos=list(map(lambda x:x*0.3,precos))
print(impostos)