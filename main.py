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

    def lenTablero(self):
        return len(self.tablero)

    def extremosMesa (self):
        if (self.tablero):
            a = [self.tablero[0].valor1, self.tablero[self.lenTablero() - 1].valor2]
            return a
        return None


class Fichas:

    def __init__ (self, valor1, valor2):
        self.valor1, self.valor2 = valor1, valor2

    def __repr__ (self):
        return "[{},{}]".format(self.valor1,self.valor2)

    def voltear (self):
        self.valor1, self.valor2 = self.valor2, self.valor1

    def esDoble(self):
        if (self.valor1 == self.valor2):
            return True
        return False

    @property
    def valores(self):
        return [self.valor1, self.valor2]

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

    def __init__ (self, nombre, fichasMesa):
        self.nombre = nombre
        self.fichas = []
        i = 0
        while (i < 7):
            self.fichas.append(fichasMesa.pop(randrange(len(fichasMesa))))
            i += 1

    def __repr__ (self):
        return self.nombre

    def lenMano(self):
        return len(self.fichas)
    
    def verMano (self):
        return self.fichas

    def verDobles(self):
        dobles = []
        for x in range(self.lenMano()):
            if (self.fichas[x].esDoble()):
                dobles.append(self.fichas[x])
        if (dobles):
            return dobles
        return None
    
    def jugarFicha (self, posicion):
        return self.fichas.pop(posicion - 1)

    def voltearFicha(self, posicion):
        self.fichas[posicion - 1].voltear()

    def tieneFichas(self):
        if (self.fichas):
            return True
        return False

class Juego:

    @staticmethod
    def esJugable(mesa, ficha, fichasEnMesa):
        if (mesa.tablero):
            if (ficha.valor1 == mesa.extremosMesa()[0] or ficha.valor1 == mesa.extremosMesa()[1]):  
                return True
            if (ficha.valor2 == mesa.extremosMesa()[0] or ficha.valor2 == mesa.extremosMesa()[1]):
                return True
            else:
                return False
        else:
            return True

    @staticmethod
    def esJugableAlInicio(mesa, ficha, fichasEnMesa):
        if (mesa.tablero):
            if (ficha.valor2 == mesa.extremosMesa()[0]):
                return True
            return False
        if (ficha.valor1 == 6 and ficha.valor2 == 6):
            return True
        return False

    @staticmethod
    def esJugableAlFinal(mesa, ficha, fichasEnMesa):
        if (mesa.tablero):
            if (ficha.valor1 == mesa.extremosMesa()[1]):
                return True
            return False
        if (ficha.valor1 == 6 and ficha.valor2 == 6):
            return True
        return False