# Função tratar texto !!
produtos = ["ABC123","abc000","abc111","abc222"]
texto = "   irc16521  "

def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto
texto = tratar_texto(texto)
print(texto)
for i, produto in enumerate(produtos):
    produtos[i] = tratar_texto(produto)
print(produtos)