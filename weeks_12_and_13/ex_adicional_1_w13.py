import random

def lista_grande(n):
    lista = []
    i = 0
    aux = 0
    while i < n:
        aux = random.randint(-2*n,2*n)
        lista.append(aux)
        i += 1
    return lista
    
