import random
import pygame
import os

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

# agregar try catch aqui?


def render_text(size, text, color):
    if size == "T":
        font = font_T.render(text, True, color)
    elif size == "S":
        font = font_S.render(text, True, color)
    elif size == "M":
        font = font_M.render(text, True, color)
    elif size == "B":
        font = font_B.render(text, True, color)
    elif size == "L":
        font = font_L.render(text, True, color)
    return font


def game_intro():
    intro = True
    colors_fade = [white, (238, 255, 255), (238, 255, 255), (178, 255, 221),
                   (149, 255, 193), (120, 236, 165), (91, 207, 139), (60, 179, 113)]
    count = 0
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(background_color)
        text_logo = render_text("L", "Durak", white)
        screen.blit(text_logo, (width / 2 - text_logo.get_width() //
                                2, height / 2 - text_logo.get_height() // 2))
        term_text = render_text(
            "S", ">Presione cualquier botón para continuar...", colors_fade[count % len(colors_fade)])
        screen.blit(term_text, (width / 2 - term_text.get_width() //
                                2, height - 100 / 2 - term_text.get_height() // 2))
        pygame.display.flip()
        count += 1
        clock.tick(5)


def current_dir():
    return os.getcwd()


pygame.font.init()
cur_dirr = current_dir()
font_T = pygame.font.Font(cur_dirr + "/data/fonts/font.ttf", 12)
font_S = pygame.font.Font(cur_dirr + "/data/fonts/font.ttf", 20)
font_M = pygame.font.Font(cur_dirr + "/data/fonts/font.ttf", 60)
font_B = pygame.font.Font(cur_dirr + "/data/fonts/font.ttf", 80)
font_L = pygame.font.Font(cur_dirr + "/data/fonts/font.ttf", 100)

clock = pygame.time.Clock()
FPS = 3
deck = Baraja()
discarded = []

white = (255, 255, 255)


pygame.init()
(width, height) = (800, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Durak')
background_color = (60, 179, 113)
# screen.fill(background_color)
# pygame.display.flip()
running = True

while running:
    game_intro()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
