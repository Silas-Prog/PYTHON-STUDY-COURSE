print("Informe a nota do aluno.")
aluno = [ 0 , 0 , 0 , 0 ]
nota1 = int(input("Informe a 1º nota "))
nota2 = int(input("Informe a 2º nota "))
nota3 = int(input("Informe a 3º nota: "))
nota4 = int(input("Informe a 4º nota: "))
aluno[0] = nota1
aluno[1] = nota2
aluno[2] = nota3
aluno[3] = nota4
aluno.append((nota1+nota2+nota3+nota4)/4)
print(aluno)


lista = []
n = 0
while n < 5:
    elem = str(input("Informe o caracter: "))
    lista.append(elem)
    n = n + 1
print(lista)
listac = []
listac = aluno + lista
print(listac)