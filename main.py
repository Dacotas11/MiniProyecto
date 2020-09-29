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


class Jugador:

    def __init__ (self, nombre, fichas):
        self.nombre, self.fichas = nombre, fichas

    def __repr__ (self):
        return self.nombre

    def verMano (self):
        return self.fichas

    def jugarFicha (self, posicion):
        return self.fichas.pop(posicion - 1)