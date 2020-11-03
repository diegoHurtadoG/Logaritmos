import sys
import random

MAX_PESO = 10**9

n = int(sys.argv[1])
p = float(sys.argv[2])

f = open("Grafo.txt", "w")

puntos = []

for i in range(n - 1):
    puntos.append([i, i + 1, random.randint(1, MAX_PESO)])

# No revisa dos veces, por nodo, solo lo hace una vez (si se ve como matriz, la recorre triangular)
for i in range(n - 1):
    for j in range(i + 1, n - 1): # i -> se permiten dobles arcos, (i + 1) -> No se permiten dobles arcos
        if p > random.random():
            puntos.append([puntos[i][0], puntos[j][1], random.randint(1, MAX_PESO)]) #Aqui estoy recorriendolo entero sin excluir ningun punto

f.write(str(n) + " " + str(len(puntos)) + "\n")
#print(n, len(puntos)) #Borrar si no se necesita

for i in range(len(puntos)): #Imprime los puntos en el formato necesario
    f.write(str(puntos[i][0]) + " " + str(puntos[i][1]) + " " + str(puntos[i][2]) + "\n")
    #print(puntos[i][0], puntos[i][1], puntos[i][2])

f.write(str(1))
#print(1)