def incomodam(n):
    if n <= 0:
        return ""
    elif n % 1 == 0:
        return "incomodam " + incomodam(n-1)
    else:
        return ""

def elefantes(n):
    if n <= 0:
        return ""
    elif n == 1:
        return "Um elefante incomoda muita gente\n"
    elif n == 2:
        return elefantes(n-1) + str(n) + " elefantes "+ incomodam(n) +"muito mais\n" 
    else:
        frase1 = str(n-1) + " elefantes incomodam muita gente\n"
        frase2 = str(n) + " elefantes "+ incomodam(n) +"muito mais\n"
        return elefantes(n-1) + frase1 +frase2
