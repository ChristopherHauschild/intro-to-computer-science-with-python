# -*- coding: utf-8 -*-

class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        a, b, c = self.a, self.b, self.c
        lado = ''
        if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
            lado = 'isósceles'
        elif a == b and a == c:
            lado = 'equilátero'
        else:
            lado = 'escaleno'
        return lado
