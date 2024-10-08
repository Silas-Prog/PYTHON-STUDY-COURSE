idademaior = 0
qntfeminino = 0
idade = int(input("Para iniciar aperte '0', para finalizar aperte '-1': "))
while idade != -1:
    idade = int(input("Informe a idade: "))
    if idade == -1:
        break
    sexo = str(input("Informe o seu sexo. F ou M: "))
    if idade > idademaior:
        idademaior = idade
    if idade > 17 and idade < 36 and sexo == "F":
        qntfeminino += 1
print("A maior idade dos habitantes é: %i e a quantidade de mulheres entre 18 e 35 é: %i" %(idademaior, qntfeminino))

    