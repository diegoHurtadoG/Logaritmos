
class BinaryHeapNode:
    def __init__(self, value, key):
        self.key = key
        self.value = value

class BinaryHeap:
    def __init__(self, n):
        self.min = None
        self.root = []
        self.count = 0
        self.graph_vertexs = [None]*n
    
    def insert(self, value, key):
        node = BinaryHeapNode(value, key)
        self.root.append(node)
        if self.min is None:
            self.min = node
        self.ajustar_hoja(node)
        self.graph_vertexs[value.vertex_number - 1] = node
        self.min = self.root[0]
    
    
    def empty(self):
        if self.min is None:
            return True
        else:
            return False

    def extract_min(self):
        min_node = self.min

        if not self.empty():
            last_node = self.root.pop(-1)
            if last_node != min_node:
                self.root[0] = last_node
                self.ajustar_raiz()
                self.min = self.root[0]
            else:
                self.min = None

        return min_node

    
    def decrease_key(self, node, key):
        if node.key < key:
            return None
        
        node.key = key

        self.ajustar_hoja(node)

        self.min = self.root[0]



    def ajustar_raiz(self):
        actual_node = self.get_node(0)
        node_index = self.root.index(actual_node)
        left_child_index = 2 * node_index + 1
        right_child_index = 2 * node_index + 2
        left_child = self.get_node(left_child_index)
        right_child = self.get_node(right_child_index)

        while(not (right_child is None and left_child is None)):
            
            if (left_child is None):
                if(right_child.key < actual_node.key):
                    self.root[right_child_index] = actual_node
                    self.root[node_index] = right_child
                else:
                    break
            
            elif (right_child is None):
                if(left_child.key < actual_node.key):
                    self.root[left_child_index] = actual_node
                    self.root[node_index] = left_child
                else:
                    break
            
            else:
                if(left_child.key >= actual_node.key and right_child.key >= actual_node.key):
                    break
                else:
                    if(left_child.key < right_child.key):
                        menor = left_child
                        menor_index = left_child_index
                    else:
                        menor = right_child
                        menor_index = right_child_index
                    self.root[menor_index] = actual_node
                    self.root[node_index] = menor
                          
            node_index = self.root.index(actual_node)
            left_child_index = 2 * node_index + 1
            right_child_index = 2 * node_index + 2
            left_child = self.get_node(left_child_index)
            right_child = self.get_node(right_child_index)
     
   

    def ajustar_hoja(self, node):
        actual_node = node
        try:
            node_index = self.root.index(actual_node)
        except:
            return
        parent_index = node_index//2
        parent = self.root[parent_index]

        while(parent != actual_node):
            if parent.key > node.key:
                self.root[parent_index] = node
                self.root[node_index] = parent
            
                node_index = self.root.index(actual_node)
                parent_index = node_index//2
                parent = self.root[parent_index]

            else:
                break
        

    def get_node(self, index):
        try:
            node = self.root[index]
        except:
            node = None
        return node







        




    