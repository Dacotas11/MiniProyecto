class Tablero:

    def __init__(self):
        self.tablero = []

    
    def verMesa (self):
        return self.tablero

    def jugarFichaAlFinal(self, ficha):
        self.tablero.append(ficha)

    def jugarFichaAlInicio  (self, ficha):
        self.tablero.insert(0, ficha)
