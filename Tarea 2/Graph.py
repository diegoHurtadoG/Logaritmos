
class Vertex:
    def __init__(self, vertex_number):
        self.vecinos = []
        self.pesos = []
        self.vertex_number = vertex_number
    
    def add_vecino(self, vertex, peso):
        self.vecinos.append(vertex)
        self.pesos.append(peso)




class Graph:
    def __init__(self, n):
        self.vertexs = [None]*n

    def add_vertex(self, vertex):
        self.vertexs[vertex.vertex_number] = vertex
    


