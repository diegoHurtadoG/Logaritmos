import sys
import random
import numpy as np
import os
import time


def generate_P(P_size):
    f = open("P.txt", "w")
    for i in range(P_size):
        element = str(np.random.randint(1,1000000000)) + "\n"
        if len(element)<10:
            element = add_zeros(element)
        f.write(element)
    f.close()


def generate_T(T_size):
    T = []
    for i in range(T_size):
        element = str(np.random.randint(1,1000000000)) + "\n"
        if len(element)<10:
            element = add_zeros(element)
        T.append(element)
    
    T.sort()

    f = open("T.txt", "w")
    f.writelines(T)
    f.close()


def add_zeros(element):
    zero_number = 10 -  len(element)
    for i in range(zero_number):
        element = "0" + element
    return element


def read_file(file, bytes, size):
    f = open(file, "r")
    for i in range(size):
        print(f.read(bytes))
    f.close()


start_time = time.time()

# We read the size of P and T
P_size = int(sys.argv[1])
T_size = int(sys.argv[2])

# We generate P and T
generate_P(P_size)
generate_T(T_size)

elapsed_time = time.time() - start_time

