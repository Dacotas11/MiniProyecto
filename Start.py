import main

mesa = main.Tablero()

ficha1 = main.Fichas(1,6)
ficha2 = main.Fichas(6,6)
ficha3 = main.Fichas(5,1)

fichas = main.Fichas.crearFichas()

jugador1 = main.Jugador("Jugador1", fichas)
jugador2 = main.Jugador("Jugador2", fichas)
jugador3 = main.Jugador("Jugador3", fichas)
jugador4 = main.Jugador("Jugador4", fichas)

ps = [jugador1, jugador2, jugador3, jugador4]
a = 0
print ("\n \n \n \n \n \n \n \n \n \n")
while (True):
  if (a == 4): a = 0
  
  print ("Tablero {}\n".format(mesa.verMesa()))
  
  if (ps[a].tieneFichas()):
    print (ps[a])
    print (ps[a].verMano())
    
    b = int(input("Selecciona que ficha jugar\n "))
    
    if (b == 0):
      print ("\n \n \n \n \n \n \n \n \n \n \n \nGAME OVER")
      break

    if (b == 8):
      print ("\n \n \n \n \n \n \n \n \n \nEl {} no va\n".format(ps[a]))
      a += 1
    
    if (b > 0 and b < 8):
      c = int(input("Flip\n "))
      d = int(input("principio o final\n "))
  
    if (b > 0 and b < 8):
      if (c == 2):
        ps[a].voltearFicha(b)

      if(d == 1):
        if (main.Juego.esJugableAlInicio(mesa, ps[a].fichas[b - 1], mesa.lenTablero())):
          mesa.jugarFichaAlInicio(ps[a].jugarFicha(b))
          print ("\n \n \n \n \n \n \n \n \n \n")
          if (not ps[a].tieneFichas()):
            print ("\n \n \n \n \n \n \n \nGano el {}!!!!".format(ps[a]))
            break
          a += 1
        else:
          print ("\n \n \n \n \nNo es Jugable\n")

      if(d == 2):
        if (main.Juego.esJugableAlFinal(mesa, ps[a].fichas[b - 1], mesa.lenTablero())):
          mesa.jugarFichaAlFinal(ps[a].jugarFicha(b))
          print ("\n \n \n \n \n \n \n \n \n \n")
          if (not ps[a].tieneFichas()):
            print ("Gano el {}".format(ps[a]))
            break
          a += 1
        else:
          print ("\nNo es Jugable")


"""print (mesa.verMesa())
print (jugador1.verMano())
x = int(input("aqui 1 \n"))
mesa.jugarFichaAlInicio(jugador1.jugarFicha(x))
print (mesa.verMesa())
print (jugador1.verMano())


mesa.jugarFichaAlFinal(jugador1.pop())
mesa.jugarFichaAlInicio(jugador1.pop())
mesa.jugarFichaAlInicio(jugador2.pop())
print (mesa.verMesa())
print (jugador1)

x = input("Selecciona con que ficha quieres jugar")"""