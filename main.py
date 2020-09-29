class Tablero:

    def __init__(self):
        self.tablero = []

    
    def verMesa (self):
        return self.tablero

    def jugarFichaAlFinal(self, ficha):
        self.tablero.append(ficha)
