from random import randrange

class Player:
    def __init__(self, id, fichas):
        self.id = id
        self.mano = []
        for x in range(7):
            self.mano.append(fichas.pop(randrange(len(fichas))))

    
    def play():
        pass

    def win():
        pass
    
    def verDobles(self):
        dobles = []
        for x in range(len(self.mano)):
            if (self.mano[x].isDouble()):
                dobles.append(self.mano[x])
        if (dobles):
            return dobles
        else:
            return None

    @property
    def verMano(self):
        verMano = []
        for x in range(len(self.mano)):
            verMano.append(self.mano[x].value)
        return verMano

class Ficha():

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __repr__(self):
        return ("[valor 1: {}, valor 2: {}]".format(self.value1,self.value2))

    def isDouble(self):
        if (self.value1 == self.value2):
            return True
        return False

    @property
    def value(self):
        return [self.value1, self.value2]

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
            fichas.append(Ficha.from_list(x))

        return fichas



class Tablero():
    arriba = []
    abajo = []

