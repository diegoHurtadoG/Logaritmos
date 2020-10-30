#python binarySearch.py P.txt T.txt
# El output debiesen ser los numeros:
#   123456789 tercero
#   405487351 noveno
#   875484321 veintiunavo

# file.tell() retorna la linea en la que estamos
# file.read(i) Lee i bytes desde donde estoy parado y deja al puntero en la posicion final + 1
# file.seek(i) nos mueve a la posicion i, file.seek(0, 2) me deja el punt
import sys
import time
import os



def main():

    # Para tomar tiempo de ejecución
    start_time = time.time()

    #Variables globales: No se usan en esta busqueda, no aparecen en el enunciado.
    M = 30000
    B = 500 # Bloques de a 50 lineas, TIENE QUE SER MULTIPLOS DE 10

    cuenta = 0 # De inputs y outputs

    inter = [] # Lista a la que agrego la interseccion
    indice_p = 0 # Lo ocupo para leer por bloques
    p_arr = [] # Arreglo donde guardo la lectura por bloques

    #Abrir archivos
    p = open("P.txt") # Si se quiere probar mas rapido cambiar por "P.txt"
    t = open("T.txt") # Si se quiere probar mas rapido cambiar por "T.txt"
    o = open("OutputB.txt", "w")

    #Este while lee por bloques de tamaño B el archivo P
    while(p.tell() != p.seek(0, 2)):
        p.seek(indice_p) #Despues de la comparacion, lo deja donde estaba

        buf = p.read(B).split('\n') #Meto a un arreglo los que leo en el momento
        cuenta += 1 #Agrego una lectura a cuenta

        for k in range(len(buf) - 1): #Excluyo el ultimo valor del split, ya que es ''
            p_arr.append(buf[k] + '\n')

        indice_p = p.tell()


    # Este for recorre el arreglo en el que guardamos p y busca sus elementos en t
    for i in p_arr:
        cuenta = binarySearch(t, 0, t.seek(0, 2) - 11, i,  inter, cuenta) #El segundo parametro es el principio del ultimo numero

    # Este for recorre la lista que tenemos de resultados y escribe el output en el .txt
    for j in inter:
        o.write(j)
        cuenta += 1 #Cada escritura que hago en output, agrega uno a la cuenta

    p.close()
    t.close()
    o.close()

    elapsed_time = time.time() - start_time

    return cuenta, elapsed_time

#Dado un numero, lo pasa al multiplo de 11 mas cercano (0, 11, 22, ...) va a servir para leer las lineas
def corregirIndice(n):
    return (n//11) * 11

#Algoritmo de busqueda para archivos
def binarySearch(archivo, inicio, fin, x, out, cuenta):
    actual = 0

    while(inicio < fin):
        actual = corregirIndice((inicio + fin) // 2) # Este va a ser el puntero en el que estoy
        archivo.seek(actual) # Dejo el puntero en la posicion bien definida

        linea = archivo.read(10)
        cuenta += 1

        if linea > x:
            fin = archivo.tell() - 11 # El 11 se resta porque ahi elimino el que acabo de leer

        elif linea < x:
            inicio = archivo.tell() # No se resta 11 para no contar el que ya leimos

        else: #Aqui la linea la encuentra
            out.append(linea) #Agrego la linea a out
            return cuenta
    return cuenta

main()