import main

def buscar_doblep4(p1, p2, p3, p4):
  ps = [p1, p2, p3, p4]
  for x in range(4):
    dobles = ps[x].verDobles()
    if (dobles):
      for y in dobles:
        if (y.valor1 == 6):
          return x

def iniciarJuego():
  mesa = main.Tablero()
  fichas = main.Fichas.crearFichas()

  jugador1 = main.Jugador("Jugador1", fichas)
  jugador2 = main.Jugador("Jugador2", fichas)
  jugador3 = main.Jugador("Jugador3", fichas)
  jugador4 = main.Jugador("Jugador4", fichas)
  

  ps = [jugador1, jugador2, jugador3, jugador4]
  a = buscar_doblep4(jugador1,jugador2,jugador3,jugador4)
  print ("\n\n\n\n\n\n\n")
  while (True):
    try:
      if (a == 4): a = 0
      
      print ("Tablero {}\n\n".format(mesa.verMesa()))
      
      if (ps[a].tieneFichas()):
        print ("Es el turno de",ps[a])
        print (ps[a].verMano())
        
        b = int(input("Selecciona que ficha jugar\n "))
        

        if (b == 0):
          print ("\n \n \n \n \n \n \n \n \n \n \n \nGAME OVER")
          break

        if (b == 8):
          print ("\n \n \n \n \n \n \n \n \n \nEl {} no va\n".format(ps[a]))
          a += 1
          if (a == 4):
            a = 0
        
        if (b > 0 and b <= ps[a].lenMano()):
          c = int(input("Flip Si o NO(1/2)\n"))
          d = int(input("\nprincipio o final(1/2)\n"))
      
        if (b > 0 and b <= ps[a].lenMano()):
          if (c == 1):
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
              print ("\n \n \n \n \n\n\n\n\nNo es Jugable\n")

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
        else:
          print ("\n\n\n\n\nNo es Jugable")
    except ValueError:
      print ("\n\n\n\nSolo se aceptan numeros")

def inicio():
  while (True):
    try:
      print ("\n\nEste es un juego de Domino\nPresiona 1 para jugar\n2 para ver como jugar\n0 para salir del juego")
      inicio = int(input())
      if (inicio == 1):
        iniciarJuego()

      if (inicio == 2):
        print ("\n\n\n\nPara jugar primero elige una de las fichas, despues te va a presentar la opcion de hacerle flip si o no\ny despues seleccionar si quieres jugar al principio o al final del tablero\nsi no vas presiona 8\n\nNOTA: Todo se elige en numeros")

      if (inicio == 0):
        print ("\n\n\n\n\n\n\n\n\n\n\n\n\nMuchas Gracias")
        break
    except ValueError:
      print ("\n\n\n\nSolo se aceptan numeros")


inicio()