import pygame

from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from screens.game_screen import GameScreen
from screens.welcome_screen import WelcomeScreen
from screens.gameover_screen import GameOverScreen


def main():
    #iniate pygame module
    pygame.init()

    #create a window with given width and height
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    #diaplay the first screen (welcome screen) using the given window 
    screen = WelcomeScreen(window)
    #run the display
    result = screen.loop()
    practice = screen.practice

    #if quit button not pressed
    if not screen.end:
        # and if welcome screen has stopped running 
        if result:

            #create a gamescreen displaying ball and paddles
            screen = GameScreen(window)

            #check if the player selected practice (True) or ranked (False) mode
            screen.practice = practice
            result = screen.loop()
            pointsp1 = screen.points1
            pointsp2 = screen.points2
            
            #if its ranked mode and quit button not pressed
            if not screen.end and not screen.practice:

                #if game screen is stopped running          
                if result:
                    screen = GameOverScreen(window)
                    screen.pointsp1 = pointsp1
                    screen.pointsp2 = pointsp2
                    screen.loop()
                    if not screen.quit:
                        main()
                    elif screen.end or screen.quit:
                        screen.running = False

            else:
                screen.running = False
    else:
        screen.running = False




if __name__ == "__main__":
    main()
