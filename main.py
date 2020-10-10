from random import randrange

class Tablero:

    def __init__ (self):
        self.estado = []

    def verMesa (self):
        return self.estado

    def jugarFichaAlFinal (self, ficha):
        self.estado.append(ficha)

    def jugarFichaAlInicio (self, ficha):
        self.estado.insert(0, ficha)

    def lenTablero(self):
        return len(self.estado)

    def extremosMesa (self):
        if (self.estado):
            a = [self.estado[0].valor1, self.estado[self.lenTablero() - 1].valor2]
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
        return self.valor1 == self.valor2

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
        for ficha in self.fichas:
            if (ficha.esDoble()):
                dobles.append(ficha)
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

    def __init__(self):
        self.mesa = Tablero()
        self.fichas = Fichas.crearFichas()
        
    def crearJugadores(self):
        p1 = input("Inserta el nombre del primer jugador: ")
        p2 = input("Inserta el nombre del segundo jugador: ")
        p3 = input("Inserta el nombre del tercer jugador: ")
        p4 = input("Inserta el nombre del cuarto jugador: ")

        self.jugador1 = Jugador(p1, self.fichas)
        self.jugador2 = Jugador(p2, self.fichas)
        self.jugador3 = Jugador(p3, self.fichas)
        self.jugador4 = Jugador(p4, self.fichas)

    def buscar_doblep4(self):
        jugadores = self.jugadores
        for x in range(4):
            dobles = jugadores[x].verDobles()
            if (dobles):
                for y in dobles:
                    if (y.valor1 == 6):
                        return x

    @property
    def jugadores(self):
        return [self.jugador1, self.jugador2, self.jugador3, self.jugador4]

    @staticmethod
    def esJugable(mesa, ficha, fichasEnMesa):
        if (mesa.estado):
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
        if (mesa.estado):
            if (ficha.valor2 == mesa.extremosMesa()[0]):
                return True
            return False
        if (ficha.valor1 == 6 and ficha.valor2 == 6):
            return True
        return False

    @staticmethod
    def esJugableAlFinal(mesa, ficha, fichasEnMesa):
        if (mesa.estado):
            if (ficha.valor1 == mesa.extremosMesa()[1]):
                return True
            return False
        if (ficha.valor1 == 6 and ficha.valor2 == 6):
            return True
        return False

    def iniciarJuego(self):
        jugadores = self.jugadores
        a = self.buscar_doblep4()
        print ("\n\n\n\n\n\n\n")
        while (True):
            try:
                if (a == 4): a = 0
                
                print ("Tablero {}\n\n".format(self.mesa.verMesa()))
                
                if (jugadores[a].tieneFichas()):
                    print ("Es el turno de",jugadores[a])
                    print (jugadores[a].verMano())
                    
                    b = int(input("Selecciona que ficha jugar\n "))
                    

                    if (b == 0):
                        print ("\n \n \n \n \n \n \n \n \n \n \n \nGAME OVER")
                        break

                    if (b == 8):
                        print ("\n \n \n \n \n \n \n \n \n \n{} no va\n".format(jugadores[a]))
                        a += 1
                        if (a == 4):
                            a = 0
                    
                    if (b > 0 and b <= jugadores[a].lenMano()):
                        c = int(input("Flip Si o NO(1/2)\n"))
                        d = int(input("\nprincipio o final(1/2)\n"))
                
                    if (b > 0 and b <= jugadores[a].lenMano()):
                        if (c == 1):
                            jugadores[a].voltearFicha(b)

                        if(d == 1):
                            if (self.esJugableAlInicio(self.mesa, jugadores[a].fichas[b - 1], self.mesa.lenTablero())):
                                self.mesa.jugarFichaAlInicio(jugadores[a].jugarFicha(b))
                                print ("\n \n \n \n \n \n \n \n \n \n")
                                if (not jugadores[a].tieneFichas()):
                                    print ("\n \n \n \n \n \n \n \nGano {}!!!!".format(jugadores[a]))
                                    break
                                a += 1
                            else:
                                print ("\n \n \n \n \n\n\n\n\nNo es Jugable\n")

                        if(d == 2):
                            if (self.esJugableAlFinal(self.mesa, jugadores[a].fichas[b - 1], self.mesa.lenTablero())):
                                self.mesa.jugarFichaAlFinal(jugadores[a].jugarFicha(b))
                                print ("\n \n \n \n \n \n \n \n \n \n")
                                if (not jugadores[a].tieneFichas()):
                                    print ("Gano {}!!!!!".format(jugadores[a]))
                                    break
                                a += 1
                            else:
                                print ("\nNo es Jugable")
                    else:
                        print ("\n\n\n\n\nNo es Jugable")
            except ValueError:
                print ("\n\n\n\nSolo se aceptan numeros")

    def inicio(self):
        self.crearJugadores()
        while (True):
            try:
                print ("\n\nEste es un juego de Domino\nPresiona 1 para jugar\n2 para ver como jugar\n0 para salir del juego")
                inicio = int(input())
                if (inicio == 1):
                    self.iniciarJuego()

                if (inicio == 2):
                    print ("\n\n\n\nPara jugar primero elige una de las fichas, despues te va a presentar la opcion de hacerle flip si o no\ny despues seleccionar si quieres jugar al principio o al final del Tablero\nsi no vas presiona 8\n\nNOTA: Todo se elige en numeros")

                if (inicio == 0):
                    print ("\n\n\n\n\n\n\n\n\n\n\n\n\nMuchas Gracias")
                    break
            except ValueError:
                print ("\n\n\n\nSolo se aceptan numeros")