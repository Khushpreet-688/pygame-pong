from cgitb import text
import pygame
from pygame import mixer
from screens.base_screen import Screen

class WelcomeScreen(Screen):
    """
    Class of pong Welcome screen 
    It displays a heading and two buttons => one for practice match and other for ranked one
    A click any of these buttons generated events that are handled in process_event method
    """
    def __init__(self, window, fps=60, bgcolor=None):
        super().__init__(window, fps=60, bgcolor=None)
        self.window = window
        self.practice = True
        if not self.bgcolor:
            self.bgcolor = (0,0,255)
        self.click = False
        

    def process_event(self, event):
        """
        This function checks for mousebuttondown event in the area spanned by two buttons
        and does what's intended
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            if 200 <= x <= 400 and 350 <= y <= 400:
                self.running = False
                self.practice = True
          
            elif 200 <= x <= 400 and 450 <= y <= 500:
                self.running = False
                self.practice = False
              


        

    def process_loop(self):
        """
        This function is used to build the display of the welcome screen by blitting 
        game heading and two button areas for ranked and practice match
        """
        
        #loading background image
        image = pygame.image.load('images/background.png')
        bgimage = pygame.transform.scale(image, (600, 600))
        self.window.blit(bgimage, (0,0))
        
        #blitting the heading and two buttons for selecting between practice and ranked match
        arial = pygame.font.SysFont('arial', 24)
        headingfont = pygame.font.SysFont('TimesNewRoman', 30, bold=True)
        heading = headingfont.render('PONG', True, (0,0,0))
        pygame.draw.rect(self.window, (100, 255, 100), (230, 200, 130, 50))
        self.window.blit(heading, (250, 210))
        text_surface = arial.render('Practice Mode', True, (0, 0, 0))
        pygame.draw.rect(self.window, (100, 255, 100), (200,350,200,50))
        self.window.blit(text_surface, (230, 360))
        text_surface2 = arial.render('Ranked Match', True, (0, 0, 0))
        pygame.draw.rect(self.window, (100, 255, 100), (200,450,200,50))
        self.window.blit(text_surface2, (230, 460))

        

        if not self.running:
            return True
        return False

        
        