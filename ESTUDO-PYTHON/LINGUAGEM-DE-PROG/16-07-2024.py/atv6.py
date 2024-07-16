turn=str(input("Informe o seu turno: "))
if(turn=="M" or "m"):
    print("O turno é Matutino.")
elif(turn=="V" or "v"):
    print("O turno é vespertino.")
elif(turn=="N" or "n"):
    print("O turno é Noturno.")
else:
    print("Letra invalida.")