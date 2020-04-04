def calc_dimensoes(matriz): 
    linha = len(matriz)
    coluna = len(matriz[0])
    for item in matriz:
        coluna = len(item)
        break
    return linha, coluna

def soma_matrizes(m1, m2):
    linha, coluna = calc_dimensoes(m1)
    if calc_dimensoes(m1) != calc_dimensoes(m2):
        return False
    else:
        soma = m1
        for i in range(0,linha):
            for j in range(0,coluna):
                soma[i][j] = m1[i][j] + m2[i][j]
    return soma
