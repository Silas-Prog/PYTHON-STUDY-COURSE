nota_mona = {
    "Nota_1": 10,
    "Nota_2": 8,
    "Nota_3": 6,
    "Nota_4": 9
}
urna = {
    "Display": "I2C",
    "teclado": "Matriz 3x4",
    "ESP": 8266,
    "Custo": 46.20,

}
print(nota_mona and urna)
print("O valor total é: %.2s." % urna['Custo'])