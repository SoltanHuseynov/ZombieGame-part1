import pygame
import os
#from pygame.sprite import Sprite
tesla_x=650
tesla_y=20

file=os.getcwd()

hole_star=[pygame.image.load(file+"\\levels\\hole_home\\star1.png"),pygame.image.load(file+"\\levels\\hole_home\\star2.png"),
            pygame.image.load(file+"\\levels\\hole_home\\star3.png"),pygame.image.load(file+"\\levels\\hole_home\\star4.png"),
            pygame.image.load(file+"\\levels\\hole_home\\star5.png"),pygame.image.load(file+"\\levels\\hole_home\\star6.png")]

class Stars(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=hole_star[0]
        self.index=0
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.x=tesla_x
        self.rect.y=tesla_y
    def update(self):
        if self.index+1>=len(hole_star):
            self.index=0
        self.image=hole_star[int(self.index)]
        self.image=pygame.transform.scale(self.image,(50,50))
        self.index+=0.3