def minMax(temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas)," C.")
    print("A maior temperatura do mês foi: ", maxima(temperaturas)," C.")

def maxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i += 1
    return max

def minima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min

def teste_pontual_min(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array", temp)
        print("Valor esperado: ", valor_esperado, "Valor calculado: ", valor_calculado)

def teste_pontual_max(temp, valor_esperado):
    valor_calculado = maxima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array", temp)
        print("Valor esperado: ", valor_esperado, "Valor calculado: ", valor_calculado)

def testa_maxima():
    print("Iniciando os testes")
    teste_pontual_max([1,5],5)
    teste_pontual_max([0, 2, 1],2)
    teste_pontual_max([0, 1, 2, 3, 8, 5, 6],8)
    teste_pontual_max([30, 24, 25, 22, 31, 29, 32, 33, 23],33)
    teste_pontual_max([-2, -4, -15, -8, -1],-1)
    print("Finalizando os testes")
        
def testa_minima():
    print("Iniciando os testes")
    teste_pontual_min([0],0)
    teste_pontual_min([0, 0, 0],0)
    teste_pontual_min([0, 1, 2, 3, 4, 5, 6],0)
    teste_pontual_min([30, 24, 25, 22, 31, 29, 32, 33, 23],22)
    teste_pontual_min([-2, -4, -15, -8, -1],-15)
    print("Finalizando os testes")
