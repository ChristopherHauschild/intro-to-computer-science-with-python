def conta_letras(frase, contar="vogais"):
    texto = frase.lower().strip()
    aux = 0
    spc = " "
    vgs = "a","e","i","o","u"
    for i in texto:
        if contar == "vogais":
            if i in vgs:
                aux += 1
        else:
            if i not in vgs:
                if i in spc:
                    aux = aux - 1        
                aux += 1
    return aux
