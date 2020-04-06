def busca(lista, x):
    
        primeiro = 0
        ultimo = len(lista)-1
        
        while primeiro <= ultimo:
            meio = int((primeiro + ultimo) / 2)

            print(meio)
            
            if lista[meio] == x:
                return meio
            elif lista[meio] > x:
                ultimo = meio -1
            elif lista[meio] < x:
                primeiro = meio + 1
            else:
                return False
            
        return False
