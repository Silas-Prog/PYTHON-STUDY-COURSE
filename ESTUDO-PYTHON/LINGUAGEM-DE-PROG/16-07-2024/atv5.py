let = str(input("Informe a letra: "))
letra = let.upper()
if(letra=="A" or letra== "E" or letra== "I" or letra== "O" or letra=="U"):
    print("A letra %s é uma vogal. " %(let))  
else:
    print("A letra %s é uma consoante." %(let))
