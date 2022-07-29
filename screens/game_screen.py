from tkinter.font import BOLD
import pygame
from .base_screen import Screen
from models import Ball, Paddle
from pygame import mixer
import random


class GameScreen(Screen):
    """Example class for a Pong game screen"""

    def __init__(self, *args, **kwargs):
        # Call the parent constructor
        super().__init__(*args, **kwargs)

        # Create objects
        self.ball = Ball()
        self.ball.launch()
        self.p1 = Paddle("left")
        self.points1 = 0
        self.points2 = 0
        self.p2 = Paddle("right")
        self.paddles = pygame.sprite.Group()
        self.paddles.add(self.p1, self.p2)
        self.practice = False
        

    def process_event(self, event):
        # In this screen, we don't have events to manage - pass
        pass

    def process_loop(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.p2.up()
        elif keys[pygame.K_DOWN]:
            self.p2.down()
        elif keys[pygame.K_w]:
            self.p1.up()
        elif keys[pygame.K_s]:
            self.p1.down()
        # Update the ball position
        self.ball.update()

        # Update the paddles' positions
        self.paddles.update()

        # Blit everything
        self.paddles.draw(self.window)
        self.window.blit(self.ball.image, self.ball.rect)

        # sprite collide event handling, i.e. when ball hits paddle
        if pygame.sprite.spritecollide(self.ball, self.paddles, dokill=False):
            keys = pygame.key.get_pressed()
            # give a powershot when Shift key is pressed while ball hits paddle
            if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
                self.ball.bounce("horizontal", power=True)
                mixer.init()
                mixer.music.load('./sounds/powershot.wav')
                mixer.music.play()
            else:
                self.ball.bounce("horizontal")
            
            mixer.init()
            mixer.music.load('./sounds/paddle.wav')
            mixer.music.play()
       
        # determine a random launch direction for the ball
        launch_drt = random.choice(['left', None])

        # in practice mode
        if self.practice:
            if self.ball.off_limits:
                image = pygame.image.load('./images/oops.png')
                oops = pygame.transform.scale(image, (50, 50))
                
                mixer.init()
                mixer.music.load('./sounds/off_limits.wav')
                mixer.music.play()
                
                #visual effect (oops image blitted on screen) when ball goes off_limts
                self.window.blit(oops, (self.ball.rect))
                pygame.display.update()
                pygame.time.wait(1000)
                self.ball = Ball()
                self.ball.update()
                self.ball.launch(launch_drt)
                self.bgcolor = (255, 255, 255)
                pygame.display.update()
                pygame.display.flip()
                self.running = True

        #in case of ranked match
        elif not self.practice:
            arial = pygame.font.SysFont('arial', 24, bold=True)

            point1 = arial.render(f'{self.points1}', True, (0,0,0))
            point2 = arial.render(f'{self.points2}', True, (0,0,0))
            
            self.window.blit(point1, (55, 55))
            self.window.blit(point2, (555, 55))
            pygame.display.update()
            pygame.display.flip()

            if self.ball.off_limits:
                mixer.init()
                mixer.music.load('./sounds/off_limits.wav')
                mixer.music.play()
                #player 1 gets a point
                if self.ball.winp1:
                    self.points1 += 1
                    text_surface = arial.render('POINT: PLAYER 1', True, (0, 0, 0))
                    pygame.draw.rect(self.window, (255, 255, 255), (200,50,200,50))
                    self.window.blit(text_surface, (230, 60))
                    image = pygame.image.load('./images/oops.png')
                    oops = pygame.transform.scale(image, (50, 50))
                    self.window.blit(oops, (self.ball.rect))
                    pygame.display.update()
                    pygame.time.wait(3000)
            
                elif not self.ball.winp1:
                    self.points2 += 1
                    text_surface2 = arial.render('POINT: PLAYER 2', True, (0, 0, 0))
                    pygame.draw.rect(self.window, (255, 255, 255), (200,150,200,50))
                    self.window.blit(text_surface2, (230, 160))
                    image = pygame.image.load('./images/oops.png')
                    oops = pygame.transform.scale(image, (50, 50))
                    self.window.blit(oops, (self.ball.rect))
                    pygame.display.update()
                    pygame.time.wait(3000)

                #continue the match till scores of each player is less than 10
                if self.points1 < 10 and self.points2 < 10:
                    self.window.fill((255, 255, 255))
                    self.window.blit(point1, (55, 55))
                    self.window.blit(point2, (555, 55))
                    pygame.display.update()
                    pygame.display.flip()
                    self.ball = Ball()
                    self.ball.launch(launch_drt)
                    self.ball.update()
                    pygame.display.update()
                    self.running = True
                else:
                    self.running = False
 

        if not self.running:
            return True

        return False
