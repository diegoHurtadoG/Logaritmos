#python indexedSearch.py P.txt T.txt
# El output debiesen ser los numeros:
#   123456789 tercero
#   405487351 noveno
#   875484321 veintiunavo

# Cargo P en memoria
# Armamos arreglo s con primer elemento de cada bloque (leemos 10, avanzamos B - 10, hasta el final)
# Busqueda binaria de elementos de P en s para encontrar i tal que s[i] contiene el valor
# Leer ese bloque de T y ver si se encuentra el valor

# file.tell() retorna la linea en la que estamos
# file.read(i) Lee i bytes desde donde estoy parado y deja al puntero en la posicion final + 1
# file.seek(i) nos mueve a la posicion i, file.seek(0, 2) me deja el puntero alfinal
import sys
import time

def main():
    # Para tomar tiempo de ejecución
    start_time = time.time()

    # Variables globales:
    M = 30000
    B = 500  # Bloques de a 2 lineas

    cuenta = 0 # De inputs y outputs

    indice_p = 0
    p_arr = [] #Elementos de P

    indice_s = 0
    s_arr = [] #Elementos de S

    t_arr = [] #Bloque temporal de T

    # Abrir archivos
    p = open("P.txt")  # Si se quiere probar mas rapido cambiar por "P.txt"
    t = open("T.txt")  # Si se quiere probar mas rapido cambiar por "T.txt"
    o = open("OutputI.txt", "w")

    # Cargo p en el arreglo p_arr, lo dejo con los \n
    while (p.tell() != p.seek(0, 2)):
        p.seek(indice_p)  # Despues de la comparacion, lo deja donde estaba

        buf = p.read(B).split('\n')  # Meto a un arreglo los que leo en el momento
        cuenta += 1  # Agrego una lectura a cuenta

        for k in range(len(buf) - 1):  # Excluyo el ultimo valor del split, ya que es ''
            p_arr.append(buf[k] + '\n')

        indice_p = p.tell()

    # Relleno s_arr con 1 cada B lineas, la primera de cada bloque
    while (indice_s <= t.seek(0,2)):
        t.seek(indice_s)  # Despues de la comparacion, lo deja donde estaba

        buf = t.read(10)  # Meto a un arreglo los que leo en el momento
        cuenta += 1  # Agrego una lectura a cuenta

        s_arr.append(buf)

        indice_s = (t.tell()-11) + (B/10)*11



    if( '' in s_arr): #Cuando |T|%B es 0, quedaba un string vacio alfinal que rompia el binary, no reconoce ultimo intervalo
        s_arr.pop()


    # Para cada P, busco indice, cargo el bloque, busco en el bloque
    for k in p_arr:
        i = bsearch(s_arr, k)
        if i==-1:
            continue
        t.seek(i * corregirIndice(B + 11)) # Es un 11 porque es largo de linea + 1 por tema de cursores
        temp = t.read(B).split('\n') #Temp es un arreglo de los numeros
        cuenta += 1

        for j in range(len(temp) - 1): #Dejo en t_arr los valores con el mismo formato
            t_arr.append(temp[j] + '\n')

        if (k in t_arr): # Aqui lo escribo, pero otra opcion es guardarlo en un arreglo y de ahi escribir el arreglo entero de una
            o.write(k)
            cuenta += 1

        t_arr = []

    p.close()
    t.close()
    o.close()

    elapsed_time = time.time() - start_time

    return cuenta, elapsed_time

#Dado un arreglo s y un valor x, busca el intervalo en el que estaria x
#Esta tirando bien los intervalos
def bsearch(arr, x):
    low = 0
    mid = 0
    high = len(arr) - 1
    while(low < high):
        mid = low + (high - low) // 2
        if (x <= arr[mid]):
            high = mid
        else:
            low = mid + 1

    if x >= arr[low]: #antes era ==
        return low
    if x < arr[low]:
        return low - 1
    else:
        return -1 # No deberia pasar nunca, pues siempre encuentra algun intervalo.

#Dado un numero, lo pasa al multiplo de 11 mas cercano (0, 11, 22, ...) va a servir para leer las lineas
def corregirIndice(n):
    return (n//11) * 11

main()