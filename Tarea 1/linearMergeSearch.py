#python linearSearch.py P.txt T.txt
# El output debiesen ser los numeros:
#   123456789 tercero
#   405487351 noveno
#   875484321 veintiunavo

# Cargar P entero en memoria
# Se carga T de a bloques B
# Por cada T, se busca linealmente en B

# file.tell() retorna la linea en la que estamos
# file.read(i) Lee i bytes desde donde estoy parado y deja al puntero en la posicion final + 1
# file.seek(i) nos mueve a la posicion i, file.seek(0, 2) me deja el puntero alfinal
import sys
import time

def main():
    # Para tomar tiempo de ejecución
    start_time = time.time()

    #Variables globales:
    M = 30000
    B = 50 # Bloques de a 5 lineas

    cuenta = 0 # De inputs y outputs
    inter = []  # Lista a la que agrego la interseccion

    indice_p = 0  # Lo ocupo para leer por bloques P
    p_arr = []  # Arreglo donde guardo la lectura por bloques de P

    indice_t = 0 # Lo ocupo para leer por bloques T
    t_arr = [] # Guardo T de B en B (borrando lo anterior)

    # Abrir archivos
    p = open("P.txt")  # Si se quiere probar mas rapido cambiar por sys.argv[1]
    t = open("T.txt")  # Si se quiere probar mas rapido cambiar por sys.argv[2]
    o = open("OutputLM.txt", "w")

    # Este while lee por bloques de tamaño B el archivo P y lo carga en P_arr
    while (p.tell() != p.seek(0, 2)):
        p.seek(indice_p)  # Despues de la comparacion, lo deja donde estaba

        buf = p.read(B).split('\n')  # Meto a un arreglo los que leo en el momento
        cuenta += 1  # Agrego una lectura a cuenta

        for k in range(len(buf) - 1):  # Excluyo el ultimo valor del split, ya que es ''
            p_arr.append(buf[k] + '\n')

        indice_p = p.tell()

    #Ordeno p_arr (funciona)
    quicksort(p_arr, 0, len(p_arr) - 1)

    # Este while va cargando T en bloques de a maximo B a la vez y compara como dicen en el enunciado
    while (t.tell() != t.seek(0, 2)):
        t.seek(indice_t)  # Despues de la comparacion, lo deja donde estaba

        buf = t.read(B).split('\n')  # Meto a un arreglo los que leo en el momento
        cuenta += 1  # Agrego una lectura a cuenta

        for k in range(len(buf) - 1):  # Excluyo el ultimo valor del split, ya que es ''
            t_arr.append(buf[k] + '\n')

        #Aqui abajo tengo que hacer el merge
        merge(p_arr, t_arr, inter)

        t_arr = []

        indice_t = t.tell()

    # Este for recorre la lista que tenemos de resultados y escribe el output en el .txt
    for j in inter:
        o.write(j)
        cuenta += 1  # Cada escritura que hago en output, agrega uno a la cuenta

    p.close()
    t.close()
    o.close()

    elapsed_time = time.time() - start_time

    return cuenta, elapsed_time

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if len(arr) == 1:
        return arr

    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi -1)
        quicksort(arr, pi + 1, high)


def merge(p, t, inter):
    punteroP = 0
    punteroT = 0
    while((punteroP != len(p)) and (punteroT != len(t))):
        if(p[punteroP] > t[punteroT]):
            punteroT += 1
        elif(p[punteroP] < t[punteroT]):
            punteroP += 1
        else:
            inter.append(p[punteroP])
            punteroP += 1
            punteroT += 1

main()