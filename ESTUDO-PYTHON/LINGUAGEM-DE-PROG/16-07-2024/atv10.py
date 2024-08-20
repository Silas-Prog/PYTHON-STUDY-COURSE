n1=float(input("Informe o 1º número: "))
n2=float(input("Informe o 2º número: "))
escolha=str(input("Informe a operação: "))
if(escolha=="+"):
    print("o resultado é %s" %(n1+n2))
elif(escolha=="-"):
    print("o resultado é %s" %(n1-n2))
elif(escolha=="*"):
    print("o resultado é %s" %(n1*n2))
elif(escolha=="/"):
    print("o resultado é %s" %(n1/n2))
else:
    print("Escolha invalida.")
