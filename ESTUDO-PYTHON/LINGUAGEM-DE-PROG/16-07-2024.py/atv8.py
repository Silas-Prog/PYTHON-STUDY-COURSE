n1=float(input("Informe a 1º nota: "))
n2=float(input("Informe a 2º nota: "))
n3=float(input("Informe a 3º nota: "))
n4=float(input("Informe a 4º nota: "))
media=(n1+n2+n3+n4)/4
if(media>=6):
    print("você está acima da media, parabens!")
elif(media>=5 and media<=6 ):
    print("você está abaixo da média :(")
else:
    print("Você está reprovado")