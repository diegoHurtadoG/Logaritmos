import sys
from Graph import *
from FibonacciHeap import *
from BinaryHeap import *
import time

def dijkstra(heap, vertices, vertice_inicial):
    #start_time = time.time()

    distancias = [float('inf')]*len(vertices)
    distancias[vertice_inicial - 1] = 0

    for vertice in vertices:
        numero_vertice = vertice.vertex_number
        heap.insert(vertice, distancias[numero_vertice - 1])

    while heap.empty() is False:
        nodo = heap.extract_min()
        vecinos = nodo.value.vecinos 
        pesos = nodo.value.pesos

        for i in range(len(vecinos)):
            if distancias[vecinos[i].vertex_number - 1] > distancias[nodo.value.vertex_number - 1] + pesos[i]:
                distancias[vecinos[i].vertex_number - 1] = distancias[nodo.value.vertex_number - 1] + pesos[i]
                heap.decrease_key(heap.graph_vertexs[vecinos[i].vertex_number - 1], distancias[vecinos[i].vertex_number - 1])

    #elapsed_time = time.time() - start_time
            
    #return distancias, elapsed_time
    return distancias


tipo_heap = sys.argv[1]

numero_vertices_aristas = input().split(" ")

numero_vertices = int(numero_vertices_aristas[0])
numero_aristas = int(numero_vertices_aristas[1])

if tipo_heap == "FibonacciHeap":
    heap = FibonacciHeap(numero_vertices)

elif tipo_heap == "BinaryHeap":
    heap = BinaryHeap(numero_vertices)

else:
    print("Heap no valido")


vertices = [None]*numero_vertices

for i in range(numero_aristas):
    arista = input().split(" ")
    numero_primer_vertice = int(arista[0])
    numero_segundo_vertice = int(arista[1])
    peso = int(arista[2])

    if vertices[numero_primer_vertice - 1] is None:
        primer_vertice = Vertex(numero_primer_vertice)
        vertices[numero_primer_vertice - 1] = primer_vertice

    if vertices[numero_segundo_vertice - 1] is None:
        segundo_vertice = Vertex(numero_segundo_vertice)
        vertices[numero_segundo_vertice - 1] = segundo_vertice

    primer_vertice = vertices[numero_primer_vertice - 1]
    segundo_vertice = vertices[numero_segundo_vertice - 1]

    primer_vertice.vecinos.append(segundo_vertice)
    primer_vertice.pesos.append(peso)

    segundo_vertice.vecinos.append(primer_vertice)
    segundo_vertice.pesos.append(peso)

vertice_inicial = int(input())

distancias = dijkstra(heap, vertices, vertice_inicial)

print(distancias)













    


