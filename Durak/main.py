import random

# de los puntos propuestos por roberto, van cumplidos
# 1. OOP : clases Naipe, Baraja, Jugador
# 2. Comprension de listas (en crearBaraja y mostrarCartas de clase Baraja)


class Naipe(object):
    def __init__(self, calificacion, valor):
        self.calificacion = calificacion
        self.valor = valor

    def printNaipe(self):
        print("{} de {}".format(self.valor, self.calificacion))


class Baraja(object):
    def __init__(self):
        self.naipes = []
        self.calificaciones = ["Picas", "Corazones", "Tréboles", "Diamantes"]
        self.figuras = ["A", "J", "Q", "K"]
        self.crearBaraja()

    def crearBaraja(self):
        for calif in self.calificaciones:
            [self.naipes.append(Naipe(calif, v)) for v in range(1, 11)]
            [self.naipes.append(Naipe(calif, l)) for l in self.figuras]

    def mostarCartas(self):
        [carta.printNaipe() for carta in self.naipes]

    # def barajar(self):
    #   for i in range(len(self.naipes - 1, 0, -1)):


# class Jugador(object):
 #   def __init__(self):


deck = Baraja()
deck.crearBaraja()
deck.mostarCartas()
