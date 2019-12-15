import pygame
from naipe import Naipe
from baraja import Baraja
import text_tools as tt
from jugador import jugadorAI, jugadorHumano
from sys_tools import limpiar_dir

# de los puntos propuestos por roberto, van cumplidos
# 1. OOP : clases Naipe, Baraja, Jugador
# 2. Comprension de listas (en crearBaraja y mostrarCartas de clase Baraja)
# 3. Try/excepciones (en valorNaipe de clase Naipe)


def menu_screen():
    menu = True
    print("Capte una clave, estoy en menu")
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(background_color)
        S_text = tt.render_text("T", "lmao se supone que esto es el menu!", white)
        screen.blit(S_text, (width / 2 - S_text.get_width() //
                             2, height / 2 - S_text.get_height() // 2))
        pygame.display.update()


def game_intro_screen():
    intro = True
    colors_fade = [white, (238, 255, 255), (238, 255, 255), (178, 255, 221),
                   (149, 255, 193), (120, 236, 165), (91, 207, 139), (60, 179, 113)]
    count = 0
    screen.fill(background_color)
    text_logo = tt.render_text("L", "Durak", white)
    screen.blit(text_logo, (width / 2 - text_logo.get_width() //
                            2, height / 2 - text_logo.get_height() // 2))
    while intro:
        term_text = tt.render_text(
            "S", ">Presione cualquier tecla para continuar...", colors_fade[count % len(colors_fade)])
        screen.blit(term_text, (width / 2 - term_text.get_width() //
                                2, height - 100 / 2 - term_text.get_height() // 2))
        pygame.display.flip()
        count += 1
        clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                intro = False
                menu_screen()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


clock = pygame.time.Clock()


white = (255, 255, 255)

deck = Baraja()
discarded = []
pygame.init()
(width, height) = (800, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Durak')
background_color = (60, 179, 113)
# screen.fill(background_color)
# pygame.display.flip()
running = True

while running:
    game_intro_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            limpiar_dir
            running = False
