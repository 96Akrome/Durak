import random
import pygame

# de los puntos propuestos por roberto, van cumplidos
# 1. OOP : clases Naipe, Baraja, Jugador
# 2. Comprension de listas (en crearBaraja y mostrarCartas de clase Baraja)
# 3. Try/excepciones (en valorNaipe de clase Naipe)


class Naipe(object):
    def __init__(self, calificacion, valor):
        self.calificacion = calificacion
        self.valor = valor
        self.trump = False

    def isTrump(self, trump):
        if self.calificacion == trump:
            self.trump = True
        return self.trump

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
        self.cantidad = 36
        self.calificaciones = ["Picas", "Corazones", "Tréboles", "Diamantes"]
        self.figuras = ["J", "Q", "K", "A"]
        self.crearBaraja()

    def mostarCartas(self):
        [carta.printNaipe() for carta in self.naipes]

    def barajar(self):
        random.shuffle(self.naipes)
        # self.mostarCartas() - imprime la baraja con shuffle

    def crearBaraja(self):
        for calif in self.calificaciones:
            [self.naipes.append(Naipe(calif, v)) for v in range(6, 11)]
            [self.naipes.append(Naipe(calif, l)) for l in self.figuras]
        self.barajar()

    def sacarDeBaraja(self):
        return self.naipes.pop()


class Jugador(object):
    def __init__(self):
        self.cartas = {"Picas": [], "Corazones": [],
                       "Tréboles": [], "Diamantes": []}
        self.esHumano = ""
        self.cantidad = 0

    def sacarCarta(self, baraja):
        temp = baraja.sacarDeBaraja()
        self.cartas[temp.calificacion].append(temp)
        self.cantidad += 1


class jugadorAI(Jugador):
    def __init__(self):
        Jugador.__init__(self)
        self.esHumano = False


class jugadorHumano(Jugador):
    def __init__(self):
        Jugador.__init__(self)
        self.esHumano = True


deck = Baraja()
discarded = []


pygame.init()
(width, height) = (800, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Durak')
background_color = (60, 179, 113)
screen.fill(background_color)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
