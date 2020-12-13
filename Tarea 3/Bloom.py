import mmh3 as mm
import BitVector as BV
import random

MAX_SEED = 100000 # Maximo del intervalo en el que se escogan semillas.
m = 20
k = 3

class BloomFilter:

    def __init__(self, m, k):
        # m es el largo del bit vector
        # k es la cantidad de funciones de hash
        self.bvector = BV.BitVector(size = m) # Inicializo el bitvector
        self.hash_n = k # Guardo la cantidad de hashes
        self.bvector.reset(0) # Me aseguro de que todos los bits partan en cero
        self.seeds = []

        for i in range(k):
            self.seeds.append(random.randint(0, MAX_SEED))

    def insertar(self, elemento):
        for semilla in self.seeds:
            index = mm.hash(elemento, semilla) % self.bvector.length()
            self.bvector[index] = 1

    def revisar(self, elemento):
        for semilla in self.seeds:
            index = mm.hash(elemento, semilla) % self.bvector.length()
            if self.bvector[index] == 0:
                return False

        return True

    def getBitVector(self):
        return self.bvector

'''
##De aqui para abajo es un test
bf = BloomFilter(m, k)

# Palabras que si van a estar
presentes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


# Palabras que no van a estar
ausentes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

for item in presentes:
    bf.insertar(item)

random.shuffle(presentes)
random.shuffle(ausentes)

testeo = presentes[:5] + ausentes
random.shuffle(testeo)
for word in testeo:
    if bf.revisar(word):
        if word in ausentes:
            print("'{}' es Falso Positivo".format(word))
        else:
            print("'{}' Si esta".format(word))
    else:
        print("'{}' No esta".format(word))
'''