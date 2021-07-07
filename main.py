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

    @property
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

    def sumaValores(self):
        return self.valor1 + self.valor2

    def voltear (self):
        self.valor1, self.valor2 = self.valor2, self.valor1

    def esDoble(self):
        return self.valor1 == self.valor2

    @property
    def valores(self):
        return [self.valor1, self.valor2]

    @classmethod
    def crearFichas(cls):
        lista = [[l,r] for l in range(0,7) for r in range(l, 7)]
        fichas = []
        for ficha in lista:
            fichas.append(cls(ficha[0],ficha[1]))
        return fichas


class Jugador:

    def __init__ (self, nombre):
        self.nombre = nombre
        self.fichas = []

    def asignarFichas(self, mano):
        self.fichas = mano

    def __repr__ (self):
        return self.nombre

    def sumaMano(self):
        suma = []
        for ficha in self.fichas:
            suma.append(ficha.sumaValores())
        return sum(suma)

    def lenMano(self):
        return len(self.fichas)
    
    def verMano (self):
        return self.fichas

    def verManoConIndice(self):
        return list(enumerate(self.fichas, 1))

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
        self.jugador1 = Jugador("Jugador 1")
        self.jugador2 = Jugador("Jugador 2")
        self.jugador3 = Jugador("Jugador 3")
        self.jugador4 = Jugador("Jugador 4")

    def crearJugadores(self):
        for jugador in self.jugadores:
            fichasJugador = []
            for i in range(7):
                fichasJugador.append(self.fichas.pop(randrange(len(self.fichas))))
            jugador.asignarFichas(fichasJugador)

    def nombrarJugadores(self):
        self.jugador1.nombre = input("Inserta el nombre del primer jugador: ")
        self.jugador2.nombre = input("Inserta el nombre del segundo jugador: ")
        self.jugador3.nombre = input("Inserta el nombre del tercer jugador: ")
        self.jugador4.nombre = input("Inserta el nombre del cuarto jugador: ")

    def buscar_doblep4(self):
        jugadores = self.jugadores
        for x in range(4):
            dobles = jugadores[x].verDobles()
            if (dobles):
                for y in dobles:
                    if (y.valor1 == 6):
                        return x

    def hayTranque(self):
        for jugador in self.jugadores:
            for ficha in jugador.fichas:
                if (self.esJugable(self.mesa, ficha, self.mesa.lenTablero)):
                    return False
        return True

    def puedeJugar(self, jugador):
        for ficha in jugador.fichas:
            if (self.esJugable(self.mesa, ficha, self.mesa.lenTablero)):
                return True
        return False

    def ganadorPorTranque(self):
        ganador = self.jugador1
        for jugador in self.jugadores:
            if (jugador.sumaMano() < ganador.sumaMano()):
                ganador = jugador
        return ganador

    @property
    def jugadores(self):
        return [self.jugador1, self.jugador2, self.jugador3, self.jugador4]

    @staticmethod
    def esPrimeroEnJugar(ficha):
        if (ficha.valor1 == 6 and ficha.valor2 == 6):
            return True
        return False

    @staticmethod
    def esJugable(mesa, ficha, fichasEnMesa):
        if (mesa.estado):
            if (ficha.valor1 == mesa.extremosMesa[0] or ficha.valor1 == mesa.extremosMesa[1]):  
                return True
            if (ficha.valor2 == mesa.extremosMesa[0] or ficha.valor2 == mesa.extremosMesa[1]):
                return True
            else:
                return False
        else:
            return True

    @staticmethod
    def esJugableAlInicio(mesa, ficha, fichasEnMesa):
        if (mesa.estado and ficha.valor2 == mesa.extremosMesa[0]):
            return True
        return Juego.esPrimeroEnJugar(ficha)

    @staticmethod
    def esJugableAlFinal(mesa, ficha, fichasEnMesa):
        if (mesa.estado and ficha.valor1 == mesa.extremosMesa[1]):
            return True
        return Juego.esPrimeroEnJugar(ficha)

    def iniciarJuego(self):
        jugadores = self.jugadores
        a = self.buscar_doblep4()
        print ("\n\n\n\n\n\n\n")
        while (True):
            if (self.hayTranque()):
                print ("El ganador por tranque es {}!!!".format(self.ganadorPorTranque()))
                break
            try:
                if (a == 4): a = 0
             
                if (not self.puedeJugar(jugadores[a])):
                    print ("{} no va.".format(jugadores[a]))
                    a += 1
                    continue
                
                print ("Tablero {}\n\n".format(self.mesa.verMesa()))
                
                if (jugadores[a].tieneFichas()):
                    print ("Es el turno de",jugadores[a])
                    print (jugadores[a].verManoConIndice())
                    
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
        decision = int(input("Presiona 1 si quiere nombrar los jugadores y 2 si desea dejarlos de forma generica: "))
        if (decision == 1):
            self.nombrarJugadores()
        while (True):
            try:
                print ("\n\nEste es un juego de Domino\nPresiona 1 para jugar\n2 para ver como jugar\n0 para salir del juego")
                inicio = int(input())
                if (inicio == 1):
                    self.iniciarJuego()

                if (inicio == 2):
                    print ("\n\n\n\nPara jugar primero elige una de las fichas, despues te va a presentar la opcion de hacerle flip si o no\ny despues seleccionar si quieres jugar al principio o al final del Tablero\nsi no puedes jugar presiona 8\n\nNOTA: Todo se elige en numeros")

                if (inicio == 0):
                    print ("\n\n\n\n\n\n\n\n\n\n\n\n\nMuchas Gracias")
                    break
            except ValueError:
                print ("\n\n\n\nSolo se aceptan numeros")