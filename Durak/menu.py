import pygame
import sys_tools as st


class Menu(st.Estados_Juego):
    def __init__(self):
        st.Estados_Juego.__init__(self)
        jacket_button1 = pygame.image.load(
            st.current_dir() + "/data/cards/jacket_1.png").convert_alpha()

        jacket_button2 = pygame.image.load(
            st.current_dir() + "/data/cards/jacket_2.png").convert_alpha()
        jacket_button2 = pygame.transform.scale(jacket_button2, (160, 226))

        self.b1 = pygame.Rect(70, 120, 160, 226)
        self.b2 = pygame.Rect(290, 120 ,160, 226)
        self.b3 = pygame.Rect(520, 120, 160, 226)

        jacket_button1 = pygame.transform.scale(jacket_button1, (160, 226))
        jacket_button2 = pygame.transform.scale(jacket_button2, (160, 226))

        self.images = [jacket_button1, jacket_button2]
        self.volteada = False
        print("Estoy en clase Menu de modeulo menu.py")
        self.oplist = ["Jugar", "Salir"]
        # screen.fill(self.background_color)
        # screen.blit(jacket_button1, (0, 0))

    def clean(self):
        pass

    def voltear(self):
        if not self.volteada:
            self.image = self.images[0]
            self.volteada = True
        else:
            self.image = self.images[1]
            self.volteada = False

    def get_event(self, event, keys):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.b1.collidepoint(pygame.mouse.get_pos()):
                self.voltear()
                self.st_done = True
                self.next = "JUEGO"

            elif self.b2.collidepoint(pygame.mouse.get_pos()):
                self.voltear()
                self.st_done = True
                self.next = "CREDITOS"

            elif self.b3.collidepoint(pygame.mouse.get_pos()):
                self.voltear()
                self.st_done = True
                self.next = "SALIR"

        elif event.type == pygame.QUIT:
            self.quit = True
            pygame.quit()

    def render(self, clock, screen, p):
        screen.fill(self.background_color)
        screen.blit(self.images[1], (70, 120))
        screen.blit(self.images[1], (290, 120))
        screen.blit(self.images[1], (520, 120))
        while not self.st_done:
            pygame.display.flip()
            [self.get_event(event, pygame.key.get_pressed())
             for event in pygame.event.get()]
