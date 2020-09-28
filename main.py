from random import randrange

class Player:
    def __init__(self, name, fichas):
        self.name = name
        self.mano = []
        i = 0
        while (i < 7):
            self.mano.append(fichas.pop(randrange(len(fichas))))
            i += 1

    def jugar(self, ficha):
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

    def __repr__(self):
        return self.name

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

    def spin(self):
        x = self.value2
        y = self.value1
        self.value1 = x
        self.value2 = y

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

    def __init__(self):
        self.tablero = []

    def verTablero(self):
        return self.tablero

    def jugada(self, ficha):
        self.tablero.append(ficha)
    
    @staticmethod
    def buscar_doblep4(p1, p2, p3, p4):
        ps = [p1, p2, p3, p4]
        for x in range(4):
            doubles = ps[x].verDobles()
            if (doubles):
                for y in doubles: 
                    if (y.value1 == 6):
                        print (y, x)
                        return ps[x]