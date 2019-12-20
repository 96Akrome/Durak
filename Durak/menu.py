import pygame
import sys_tools as st


class Menu(st.Estados_Juego):
    def __init__(self):
        st.Estados_Juego.__init__(self)
        jacket_button1 = pygame.image.load(
            st.current_dir() + "/data/cards/jacket_1.png").convert_alpha()
        jacket_button1 = pygame.transform.scale(jacket_button1, (160, 226))

        jacket_button2 = pygame.image.load(
            st.current_dir() + "/data/cards/jacket_2.png").convert_alpha()
        jacket_button2 = pygame.transform.scale(jacket_button2, (160, 226))

        self.images = [jacket_button1, jacket_button2]

        self.next = "JUEGO"
        print("Estoy en clase Menu de modeulo menu.py")
        self.oplist = ["Jugar", "Salir"]
        # screen.fill(self.background_color)
        # screen.blit(jacket_button1, (0, 0))

    def clean(self):
        pass

    def get_event(self, event, keys):
        if event.type == pygame.QUIT:
            self.quit = True
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            self.st_done = True

    def voltear(self):
        if not self.volteada:
            self.image = self.images[0]
            self.volteada = True
        else:
            self.image = self.images[1]
            self.volteada = False

    def render(self, clock, screen, p):
        screen.fill(self.background_color)
        screen.blit(self.images[1], (70, 120))
        screen.blit(self.images[1], (290, 120))
        screen.blit(self.images[1], (520, 120))
