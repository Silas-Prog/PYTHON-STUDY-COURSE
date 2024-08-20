somanotas = 0
for i in range(4):
    nota = float(input("Informe a %sº nota: "%(i+1)))
    somanotas = somanotas + nota
media = somanotas/4
print("A média do aluno: ", media)