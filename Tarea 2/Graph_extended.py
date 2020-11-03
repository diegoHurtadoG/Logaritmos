
class Vertex:
    def __init__(self, vertex_number):
        self.vecinos = []
        self.pesos = []
        self.vertex_number = vertex_number
    
    def add_vecino(self, vertex, peso):
        self.vecinos.append(vertex)
        self.pesos.append(peso)


    ## Codigo Diego
    def __str__(self):
        info_propia = "Vertice numero: " + str(self.vertex_number)
        info_vecino = "Tiene de vecinos: " + str(self.vecinos)
        info_pesos = "Con pesos: " + str(self.pesos)
        return info_propia + "\n" + info_vecino + "\n" + info_pesos + "\n\n"

    def get_vecinos(self):
        return self.vecinos

    def get_pesos(self):
        return self.pesos

    def get_number(self):
        return self.vertex_number

    def delete_vecino(self, vertex):
        for i in range(len(self.vecinos)):
            if self.vecinos[i] == vertex:
                self.vecinos.pop(i)
                self.pesos.pop(i)



## El vertice 0 siempre va a ser nulo
class Graph:
    # Lo multiplico por n + 1 porque el cero siempre va a ser nulo, el 0 se ignora cuando se hace heap
    def __init__(self, n):
        self.vertexs = [None]*n

    def add_vertex(self, vertex):
        self.vertexs[vertex.vertex_number] = vertex

    ## Codigo Diego
    def vertex_exist(self, numero):
        for x in self.vertexs:
            if x == None:
                continue
            elif numero == x.vertex_number:
                return True
        return False

    def get_vertex(self, numero):
        for x in self.vertexs:
            if x == None:
                continue
            elif x.vertex_number == numero:
                return x

    def __str__(self):
        string_builder = ""

        for index, x in enumerate(self.vertexs):
            if x == None:
                string_builder = string_builder + "El vertice " + str(index) + " es nulo\n"
            else:
                string_builder = string_builder + str(x)

        return string_builder

    def get_all_vertex(self):
        return self.vertexs