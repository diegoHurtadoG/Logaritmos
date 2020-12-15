import re
import generator
import random
import sys
import time
import Bloom
import objsize
import math


PORCENTAJE = 40 #Porcentaje que va a ser n de Q
n = 2000
m = int(sys.argv[1]) #Cantidad de bits del bitvector
q = int(n * 100 / PORCENTAJE) # Cantidad de Consultas
k = math.ceil(m * math.log(2, math.e) / n) #Numero de hashes

n_names = generator.generar(n) #Aqui genero L.txt

bf = Bloom.BloomFilter(m, k)

for element in n_names:
    bf.insertar(element)

file = open("L.txt", "r")

q_names = [] #Nombres que estan en q y no en n
#En este for voy a generar q - n nombre aleatorios para agregar al test
for i in range(q - n):
    name_buffer = ""
    for j in range(random.randint(generator.N_MIN, generator.N_MAX)):
        name_buffer = name_buffer + generator.caracteres[random.randint(0, len(generator.caracteres) - 1)]
    q_names.append(name_buffer)

#A este punto tengo n_names con los que estan y q_names con los que no estan
all_names = q_names + n_names # Todos los casos
random.shuffle(all_names) # Los mezclo



# Esto es para mantener la cuenta
positivos_reales = 0
falsos_positivos = 0
negativos = 0


#Por cada palabra p en la lista grande, busco en bf
#   - no esta -> continuo
#   - puede estar -> busco con grep
#       - esta -> epico
#       - no esta -> una lastima
start_time = time.time()
for p in all_names:
    esta = False # Va a ser la variable que me dice si efectivamente esta o no
    if bf.revisar(p):
        file.seek(0) # Sin esta linea, el puntero del archivo no va a partir desde el inicio del archivo siempre
        for line in file:
            if re.search(p, line):
                positivos_reales += 1
                esta = True
                break
        if esta == False:
            falsos_positivos += 1
    else:
        negativos += 1
elapsed_time = time.time() - start_time


print("Tiempo de ejecucion (sin incluir generacion de variables ni archivo): ", elapsed_time)
print("La memoria actual en uso es: ", objsize.get_deep_size(bf))
print("Falsos positivos: ", falsos_positivos)

#for o in objsize.traverse_bfs(bf):
#    print(o)
