def insertion_sort(lista):
 
    if len(lista) <= 1: 
        return lista

    for i in range(1, len(lista)): 
        j = i - 1 
        key = lista[i]
        
        while j >= 0 and key < lista[j]: 
            lista[j + 1] = lista[j] 
            j = j - 1 
            lista[j + 1] = key 
 
    return lista

