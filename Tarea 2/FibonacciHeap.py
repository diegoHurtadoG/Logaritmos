import math

class Node:
    def __init__(self, value, key):
        self.parent = None
        self.children = None
        self.degree = 0
        self.mark = False
        self.left = None
        self.right = None
        self.value = value
        self.key = key


class FibonacciHeap:

    def __init__(self, n):
        self.root_list = None
        self.min = None
        self.graph_vertexs = [None]*n
        self.count = 0


    # Value es un objeto de tipo Vertex
    def insert(self, value, key):
        node = Node(value, key)
        node.left = node
        node.right = node

        self.insert_to_root_list(node)

        if self.min is None or node.key < self.min.key:
            self.min = node

        self.count += 1
        self.graph_vertexs[value.vertex_number - 1] = node

        return None


    def empty(self):
        if self.min is None:
            return True
        else: 
            return False
    

    def decrease_key(self, node, key):
        if key > node.key:
            return None

        node.key = key
        parent = node.parent

        if parent is not None and node.key < parent.key:
            self.cortar(node, parent)
            self.cortar_en_cascada(parent)

        if node.key < self.min.key:
            self.min = node


    # Recordar eliminar el nodo del graph
    def extract_min(self):
        min_node = self.min
        if min_node is not None:
            if min_node.children is not None:
                children = [x for x in self.iterar_lista(min_node.children)]
                for i in range(len(children)):
                    self.insert_to_root_list(children[i])
                    children[i].parent = None
            
            self.eliminar_de_root_list(min_node)
            # Buscamos el nuevo minimo
            if min_node == min_node.right:
                self.min = self.root_list = None
            
            else:
                self.min = min_node.right
                self.consolidar()
            self.count -= 1
            self.graph_vertexs[min_node.value.vertex_number - 1] = None
        
        return min_node    


    def iterar_lista(self, head):
        nodo = stop = head
        f = False
        while True:
            if nodo == stop and f == True:
                break
            elif nodo == stop:
                f = True
            yield nodo
            nodo = nodo.right

    def insert_to_root_list(self, node):
        if self.root_list is None:
            self.root_list = node     
        else:
            node.right = self.root_list.right
            node.left = self.root_list
            self.root_list.right.left = node
            self.root_list.right = node

    
    def cortar(self, first_node, second_node):
        self.eliminar_de_hijos(second_node, first_node)
        second_node.degree -= 1
        self.insert_to_root_list(first_node)
        first_node.parent = None
        first_node.mark = False


    def cortar_en_cascada(self, node):
        parent = node.parent
        if parent is not None:
            if node.mark is False:
                node.mark = True
            else:
                self.cortar(node, parent)
                self.cortar_en_cascada(parent)

    def eliminar_de_hijos(self, padre, hijo):
        if padre.children == padre.children.right:
            padre.children = None
        elif padre.children == hijo:
            padre.children = hijo.right
            hijo.right.parent = padre
        hijo.left.right = hijo.right
        hijo.right.left = hijo.left
    

    def consolidar(self):
        a = [None]*int(math.log(self.count) * 2)
        nodos = [h for h in self.iterar_lista(self.root_list)]

        for h in range(len(nodos)):
            nodo = nodos[h]
            d = nodo.degree
            while a[d] != None:
                another_node = a[d]
                if nodo.key > another_node.key:
                    t = nodo
                    nodo, another_node = another_node, t
                self.link(another_node, nodo)
                a[d] = None
                d += 1
            a[d] = nodo
        

        for i in range(len(a)):
            if a[i] is not None:
                if a[i].key < self.min.key:
                    self.min = a[i]

    
    def link(self, node, another_node):
        self.eliminar_de_root_list(node)
        node.left = node.right = node
        self.insert_to_child_list(another_node, node)
        another_node.degree += 1
        node.parent = another_node
        node.mark = False

    
    def eliminar_de_root_list(self, node):
        if node == self.root_list:
            self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left

    
    def insert_to_child_list(self, node, another_node):
        if node.children is None:
            node.children = another_node
        else:
            another_node.right = node.children.right
            another_node.left = node.children
            node.children.right.left = another_node
            node.children.right = another_node


