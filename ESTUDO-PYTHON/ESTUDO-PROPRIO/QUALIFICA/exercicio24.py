produto_a = ["Biscoito", "Recheado", "Chocolate","Toddy"]
produto_b = ["refrigerante","Fanta","Uva","Desconhecida"]
lista_produtos = [produto_a,produto_b]
for produto in lista_produtos:
    print("Compre agora um %s %s de %s da marca toddy %s" %(produto[0], produto[1], produto[2], produto[3]))