km = int(input("Informe a sua velocidade: "))
if(km>80):
    valor=(km-80)*5
    print("O valor da multa é %f" %(valor))
else:
    print("Continue andando dentro do permitido!")