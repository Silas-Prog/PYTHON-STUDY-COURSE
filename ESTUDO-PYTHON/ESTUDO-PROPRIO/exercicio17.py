nota = [5, 8, 9, 10, 7]
nota1 = []
nota1 = nota
print("Nota: %i" %(nota))
print("")
print("Nota 1: %i" %(nota1))
print("")
x=0
vnota = 0
while(x<5):
    vnota = vnota + nota[x] 
    x = x + 1
vmedia = vnota/(x+1)
print(vmedia)