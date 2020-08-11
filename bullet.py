import pygame
from pygame.sprite import Sprite
import random
import os
file=os.getcwd()


#attack1=pygame.image.load(file+"\\player\\attack\\Bullet.png")
attack2=pygame.image.load(file+"\\player\\attack\\bullet1.png")

class Bullet(Sprite):
    def __init__(self,x,y,foring):
        super().__init__()
        self.rote=foring
        self.IMage=attack2
        self.rect=self.IMage.get_rect()
        self.rect.x=x+65
        self.rect.y=y+80
        self.bulletspeed=12*self.rote
        self.radius=8
        #self.BULLET=(self.rect.x,self.rect.y,5,5)
    def update(self,win180):
        self.rect.x+=self.bulletspeed
        if self.rect.x<0 or self.rect.x >890:
            self.kill()
        win180.blit(pygame.transform.scale(attack2,(10,10)),(self.rect.x,self.rect.y))



       
