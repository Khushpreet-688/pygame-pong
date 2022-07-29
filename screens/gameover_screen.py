import pygame
from screens.base_screen import Screen

class GameOverScreen(Screen):
    """
    This is a GameOverScreen class that inherits from screen class
    It is used to display the game over heading, final scores of two players and quit and replay buttons.
    """
    def __init__(self, window, fps=60, bgcolor=None):
        super().__init__(window, fps, bgcolor)
        self.window = window
        self.pointsp1 = 0
        self.pointsp2 = 0
        if not self.bgcolor:
            self.bgcolor = (0,0,255)
        self.quit = False

    def process_event(self, event):
        """
        This function is used to detect mousebuttondown event on the area spanned by quit and replay buttons
        and does what's intended
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            if 100 <= x <= 275 and 400 <= y <= 450:
                self.running = False
                self.quit = True
            elif 325 <= x <= 500 and 400 <= y <= 450:
                self.running = False
                self.quit = False
        

    def process_loop(self):
        """
        This function is used to display the Game Over text, Player 1 and Player 2 final scores
        and Quit and Replay buttons
        """
        arial = pygame.font.SysFont('arial', 24)
        text_surface = arial.render('Game Over', True, (0, 0, 0))
        pygame.draw.rect(self.window, (100, 255, 100), (100,150,400,50))
        self.window.blit(text_surface, (160, 160))
        text_surface2 = arial.render('Quit', True, (0, 0, 0))
        pygame.draw.rect(self.window, (100, 255, 100), (100,400,175,50))
        self.window.blit(text_surface2, (120, 410))
        text_surface2 = arial.render('Replay', True, (0, 0, 0))
        pygame.draw.rect(self.window, (100, 255, 100), (325,400,175,50))
        self.window.blit(text_surface2, (345, 410))

        
        text_surface3 = arial.render(f'Player 1: {self.pointsp1}', True, (0, 0, 0))
        pygame.draw.rect(self.window, (100, 255, 100), (200, 250, 200, 50))
        self.window.blit(text_surface3, (230, 260))
        text_surface4 = arial.render(f'Player 2: {self.pointsp2}', True, (0, 0, 0))
        pygame.draw.rect(self.window, (100, 255, 100), (200, 300, 200, 50))
        self.window.blit(text_surface4, (230, 310))

        if not self.running:
            return True
        return False
