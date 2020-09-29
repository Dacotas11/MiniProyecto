class Tablero:

    def __init__(self):
        self.tablero = []

    
    def verMesa (self):
        return self.tablero

    def jugarFichaAlFinal (self, ficha):
        self.tablero.append(ficha)

    def jugarFichaAlInicio  (self, ficha):
        self.tablero.insert(0, ficha)

class Fichas:

    def __init__(self, valor1, valor2):
        self.valor1, self.valor2 = valor1, valor2

    def __repr__ (self):
        return "[{},{}]".format(self.valor1,self.valor2)

    def voltear (self):
        self.valor1, self.valor2 = self.valor2, self.valor1
