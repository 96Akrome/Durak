import pygame
import sys_tools as st

class Menu(st.Estados_Juego):
    def __init__(self):
        st.Estados_Juego.__init__(self)
        print("Estoy en clase Menu de modulo menu.py")
        jacket_button1 = pygame.image.load(
            st.current_dir() + "/data/cards/jacket_1.png").convert_alpha()
        jacket_button2 = pygame.image.load(
            st.current_dir() + "/data/cards/jacket_2.png").convert_alpha()
        #screen.fill(self.background_color)
        #screen.blit(jacket_button1, (0, 0))

    def clean(self):
        pass
