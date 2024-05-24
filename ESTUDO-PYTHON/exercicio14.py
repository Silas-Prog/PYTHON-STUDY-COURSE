import time
lista = ["Maça", "Banana", "Uva", "Goiaba", ""]

i = 0

while i < 5:
    print(lista[i])
    i = i + 1
    if i ==4:
        i = 0
    time.sleep(1)

