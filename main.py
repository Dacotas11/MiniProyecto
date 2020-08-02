class Player:
    
    def __init__(self, id, fichas):
        pass

    def play():
        pass

    def win():
        pass


class Ficha():

    def __init__(self, value1, value2, id):
        self.id = id
        self.value1 = value1
        self.value2 = value2

    def __repr__(self):
        return ("valor 1: {}, valor 2: {}, id: {}".format(self.value1,self.value2,self.id))

    @classmethod
    def from_list(cls, list):
        return cls(list[0], list[1], list[2])

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
                lista.append([a, y, len(lista)])
        
        for x in lista:
            fichas.append(Ficha.from_list(x))

        return fichas



class Tablero():
    arriba = []
    abajo = []

Ficha.crearFichas()

a = [0, 1, 2]
prueba = Ficha.crearFichas()
print (prueba[0])