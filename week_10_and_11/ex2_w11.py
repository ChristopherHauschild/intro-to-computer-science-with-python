def menor_nome(lista_nomes):

    comprimento = len(lista_nomes[0].strip())
    aux = []
    j = 0
    while j < len(lista_nomes):    
        if len(lista_nomes[j].strip()) <= comprimento:
            aux = lista_nomes[j].strip().capitalize()
            comprimento = len(lista_nomes[j].strip())
        j = j + 1    
    return aux

