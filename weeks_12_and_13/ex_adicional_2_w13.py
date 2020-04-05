def ordena(lista):
    
    for i in range(len(lista)):
        lista = SelectionSort(lista)
    return lista
    
        
def SelectionSort(lista):
    valor_minimo = 0
    for i in range(len(lista)):
        valor_minimo = i
        for j in range(i + 1, len(lista)): #Percorrendo lista da esquerda para a direita
            if lista[j] < lista[valor_minimo]:
                valor_minimo = j
        lista[i], lista[valor_minimo] = lista[valor_minimo], lista[i]
    return lista
        
