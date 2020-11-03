import sys
from Graph import *
from BinaryHeap import *
from FibonacciHeap import *


# Argumento por consola
tipo_heap = sys.argv[1]

# Argumentos por input
inp = input()
n = int(inp.split(" ")[0])
aristas = int(inp.split(" ")[1])

# Validacion y definicion de estructura
if (tipo_heap == "FibonacciHeap"):
    heap = FibonacciHeap(n)
elif (tipo_heap == "BinaryHeap"):
    heap = BinaryHeap(n)
else:
    raise Exception("Inserte tipo valido de estructura")

# Donde voy a ir guardando los pesos con sus vertices
caminos = []

# Lleno la lista caminos[]
for i in range(aristas):
    punto = input()
    temp = punto.split(" ")

    # Cambio los valores de str a int pero los dejo como arreglo
    for j in range(len(temp)):
        temp[j] = int(temp[j])

    # Arreglo los indices para disminuir 1
    temp[0] -= 1
    temp[1] -= 1

    # Caminos va a ser de la forma [[x1, x2, w1], [x1, x3, w2], ...] para cada linea del input, los valores son ints
    caminos.append(temp)

# Esta es la ultima linea del input
punto_inicial = input()

#Aqui tengo que crear el grafo
grafo = Graph(n)

# x tiene la forma [origen, destino, peso]
for x in caminos:
    # Reviso para crear x1 -> x2
    if not grafo.vertex_exist(x[0]):
        grafo.add_vertex(Vertex(x[0]))

    # Reviso para crear x2 -> x1
    if not grafo.vertex_exist(x[1]):
        grafo.add_vertex(Vertex(x[1]))

    # Estoy asegurado que los vertices existen

    # Agrego a x2 como vecino de x1 con peso w
    grafo.get_vertex(x[0]).add_vecino(x[1], x[2])

    # Agrego a x1 como vecino de x2 con peso w
    grafo.get_vertex(x[1]).add_vecino(x[0], x[2])

# Ojo con los indices
def dijkstra(grafo, inicio):

    distancias = [float('inf')] * n
    distancias[int(inicio) - 1] = 0

    for i in range(len(grafo.get_all_vertex())):
        heap.insert(grafo.get_vertex(i), distancias[i])

    while not heap.empty():
        actual = heap.extract_min()  # Actual es nodo, tiene la forma valor (vertex), key (distancia)

        vertice_actual = actual.get_value()
        vecinos_va = vertice_actual.get_vecinos()  # Lista de ints
        pesos_va = vertice_actual.get_pesos()  # Lista de ints

        for i in range(len(vecinos_va)):
            nodo_vecino = heap.graph_vertexs[vecinos_va[i] - 1]
            if(nodo_vecino == None):
                continue
            nuevo_peso = actual.get_key() + pesos_va[i]
            if nuevo_peso < nodo_vecino.get_key():
                vertice_vecino = nodo_vecino.get_value()
                distancias[vertice_vecino.get_number()] = nuevo_peso
                heap.decrease_key(nodo_vecino, nuevo_peso)

    return distancias

print(dijkstra(grafo, punto_inicial))