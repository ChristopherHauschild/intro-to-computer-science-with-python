def primeiro_lex(lista):
    j = 0
    aux1 = ord(lista[0][0])
    while j < len(lista):
        if ord(lista[j][0]) <= aux1:
            aux3 = lista[j]
            aux1 = ord(lista[j][0])
        j = j + 1
    return aux3
