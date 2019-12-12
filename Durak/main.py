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

    def valorNaipe(self):
        try:
            int(self.rank)
            return int(self.rank)
        except ValueError:
            if self.rank == "J":
                return 11
            elif self.rank == "Q":
                return 12
            elif self.rank == "K":
                return 13
            elif self.rank == "A":
                return 14
            else:
                raise Exception("Calificacion de naipe inválida!")



class Baraja(object):
    def __init__(self):
        self.naipes = []
        self.cantidad = 52
        self.calificaciones = ["Picas", "Corazones", "Tréboles", "Diamantes"]
        self.figuras = ["J", "Q", "K", "A"]
        self.crearBaraja()

    def crearBaraja(self):
        for calif in self.calificaciones:
            [self.naipes.append(Naipe(calif, v)) for v in range(2, 11)]
            [self.naipes.append(Naipe(calif, l)) for l in self.figuras]

    def mostarCartas(self):
        [carta.printNaipe() for carta in self.naipes]

    # def barajar(self):
      # for i in range(len(self.naipes - 1, 0, -1)):


# class Jugador():
 #   def __init__(self):


card.printNaipe()
deck = Baraja()
deck.crearBaraja()
deck.mostarCartas()
