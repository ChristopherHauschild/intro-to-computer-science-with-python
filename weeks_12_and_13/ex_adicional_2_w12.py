# -*- coding: utf-8 -*-

class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self,triangulo):
        
        a1, b1, c1 = self.a, self.b, self.c
        a2, b2, c2= triangulo.a, triangulo.b, triangulo.c

        if (a1 == b1 and b1 == c1) and (a2 == c2 and c2 == b2):
            return True
        else:
            return False

        
