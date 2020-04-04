def calc_dimensoes(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    for item in matriz:
        coluna = len(item)
        break
    return "{}".format(linha) + "X" + "{}".format(coluna)

def dimensoes(matriz):
    print(calc_dimensoes(matriz))


