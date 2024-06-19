lista_produtos = ["faca","garfo","prato","panela","frigideira"]

for p in lista_produtos:
    print(p.capitalize())


lista_precos = [10, 10, 20, 200, 50]

for preco in lista_precos:
    print(preco/10)

produtos = {
    "faca": 10,
    "garfo": 10,
    "prato": 20,
    "panela": 200,
    "frigideira": 50,
}
print("")
for pr in produtos:
    print(pr.capitalize())
    print(produtos[pr])
    