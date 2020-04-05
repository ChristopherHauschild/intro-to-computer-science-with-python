def ordenada(lista):
    prox = 0
    if len(lista) == 0:
        return True
    else:
        for i in range(len(lista)):
            prox = i + 1
            if prox < len(lista):
                if lista[i] > lista[prox]:
                    return False
            else:
                return True
