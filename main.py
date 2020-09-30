from random import randrange

class Tablero:

    def __init__ (self):
        self.tablero = []

    def verMesa (self):
        return self.tablero

    def jugarFichaAlFinal (self, ficha):
        self.tablero.append(ficha)

    def jugarFichaAlInicio (self, ficha):
        self.tablero.insert(0, ficha)


class Fichas:

    def __init__ (self, valor1, valor2):
        self.valor1, self.valor2 = valor1, valor2

    def __repr__ (self):
        return "[{},{}]".format(self.valor1,self.valor2)

    def voltear (self):
        self.valor1, self.valor2 = self.valor2, self.valor1

    @classmethod
    def from_list(cls, list):
        return cls(list[0], list[1])

    @staticmethod
    def crearFichas():
        lista = []
        fichas = []
        a = 7
        b = 8
        while (a > 0):
            a -= 1
            b -= 1
            for y in range(b):
                lista.append([a, y])
        
        for x in lista:
            fichas.append(Fichas.from_list(x))
        return fichas


class Jugador:

    def __init__ (self, nombre, fichas):
        self.nombre, self.fichas = nombre, fichas

    def __repr__ (self):
        return self.nombre

    def verMano (self):
        return self.fichas

    def jugarFicha (self, posicion):
        return self.fichas.pop(posicion - 1)