import pygame
import os
import random
#from pygame.sprite import Sprite
file=os.getcwd()

import bullet
import player_attack
import Enemiy
zombie=Enemiy.enemiy2(800,400,50,100)

player_x=25
player_y=390

player_width=120
player_height=120

player_runRight=[pygame.image.load(file+"\\player\\run\\right\\run1.png"),pygame.image.load(file+"\\player\\run\\right\\run2.png"),
                  pygame.image.load(file+"\\player\\run\\right\\run3.png"),pygame.image.load(file+"\\player\\run\\right\\run4.png"),
                  pygame.image.load(file+"\\player\\run\\right\\run5.png"),pygame.image.load(file+"\\player\\run\\right\\run6.png"),
                  pygame.image.load(file+"\\player\\run\\right\\run7.png"),pygame.image.load(file+"\\player\\run\\right\\run8.png"),
                  pygame.image.load(file+"\\player\\run\\right\\run9.png"),pygame.image.load(file+"\\player\\run\\right\\run10.png")]

player_runLeft=[pygame.image.load(file+"\\player\\run\\left\\run1.png"),pygame.image.load(file+"\\player\\run\\left\\run2.png"),
                 pygame.image.load(file+"\\player\\run\\left\\run3.png"),pygame.image.load(file+"\\player\\run\\left\\run4.png"),
                 pygame.image.load(file+"\\player\\run\\left\\run5.png"),pygame.image.load(file+"\\player\\run\\left\\run6.png"),
                 pygame.image.load(file+"\\player\\run\\left\\run7.png"),pygame.image.load(file+"\\player\\run\\left\\run8.png"),
                 pygame.image.load(file+"\\player\\run\\left\\run9.png"),pygame.image.load(file+"\\player\\run\\left\\run10.png")]

player_idleR=[pygame.image.load(file+"\\player\\idle\\idle1.png"),pygame.image.load(file+"\\player\\idle\\idle2.png"),
            pygame.image.load(file+"\\player\\idle\\idle3.png"),pygame.image.load(file+"\\player\\idle\\idle4.png"),
            pygame.image.load(file+"\\player\\idle\\idle5.png"),pygame.image.load(file+"\\player\\idle\\idle6.png"),
            pygame.image.load(file+"\\player\\idle\\idle7.png"),pygame.image.load(file+"\\player\\idle\\idle8.png"),
            pygame.image.load(file+"\\player\\idle\\idle9.png"),pygame.image.load(file+"\\player\\idle\\idle10.png")]

player_idleL=[pygame.image.load(file+"\\player\\idleLeft\\idle1.png"),pygame.image.load(file+"\\player\\idleLeft\\idle2.png"),
            pygame.image.load(file+"\\player\\idleLeft\\idle3.png"),pygame.image.load(file+"\\player\\idleLeft\\idle4.png"),
            pygame.image.load(file+"\\player\\idleLeft\\idle5.png"),pygame.image.load(file+"\\player\\idleLeft\\idle6.png"),
            pygame.image.load(file+"\\player\\idleLeft\\idle7.png"),pygame.image.load(file+"\\player\\idleLeft\\idle8.png"),
            pygame.image.load(file+"\\player\\idleLeft\\idle9.png"),pygame.image.load(file+"\\player\\idleLeft\\idle10.png")]

player_idle=[pygame.image.load(file+"\\player\\attack\\R\\idle1.png"),pygame.image.load(file+"\\player\\attack\\L\\idle1.png")]


class PlayerAnime(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.index=0
        self.indexidle=0
        self.left=False
        self.right=False
        self.jump=False
        self.jumpCount=7
        self.Image=player_runRight[0]
        self.rect=self.Image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
        self.even=True
        self.attackR=False
        self.attackL=False
        self.shoot=0
        self.playerspeed=random.randint(4,7)
        self.bell=100

    def anime(self,Windows):
        if self.index+1>=len(player_runRight):
            self.index=0
        if not self.even:
            if self.right:
               Windows.blit(pygame.transform.scale(player_runRight[self.index//2],(player_width,player_height)),(self.rect.x,self.rect.y))
               self.index+=1
            elif self.left:
                Windows.blit(pygame.transform.scale(player_runLeft[self.index//2],(player_width,player_height)),(self.rect.x,self.rect.y))
                self.index+=1
        else:
            if self.left:
                if self.indexidle+1>=len(player_idleR):
                    self.indexidle=0
                Windows.blit(pygame.transform.scale(player_idleL[self.indexidle//2],(player_width,player_height)),(self.rect.x,self.rect.y))
                self.indexidle+=1
    
            else:
                if self.indexidle+1>=len(player_idleR):
                    self.indexidle=0
                Windows.blit(pygame.transform.scale(player_idleR[self.indexidle//2],(player_width,player_height)),(self.rect.x,self.rect.y))
                self.indexidle+=1

    def update(self,win64):
        Keys=pygame.key.get_pressed()
        self.anime(win64)
        if Keys[pygame.K_d]:
            self.right=True
            self.left=False
            self.even=False
            if self.rect.x<780:
               self.rect.x+=self.playerspeed
        
        elif Keys[pygame.K_a]:
            self.left=True
            self.right=False
            self.even=False
            if self.rect.x >25:
               self.rect.x-=self.playerspeed
        else:
            self.even=True
            self.index=0
        if not self.jump:
            if Keys[pygame.K_SPACE]:
               self.jump=True
               self.rect.x+=7
               if self.left==True:
                   self.rect.x-=7
        else:
            if self.jumpCount >=-7:
                self.rect.y-=(self.jumpCount*abs(self.jumpCount))*1
                self.jumpCount-=1
            else:
                self.jumpCount=7
                self.jump=False 
    def bullet1(self,all_B,all_P):
        if self.left:
            foring=-1        
        else:
            foring=1  
        attack=bullet.Bullet(self.rect.x,self.rect.y,foring)
        all_B.add(attack)
        all_P.add(attack)
    def shiled(self,win121):
        if self.bell <0:
            self.bell=0
        bar_lenght=100
        bar_height=10
        fill=(self.bell/9)*bar_height
        fill_win=pygame.Rect(self.rect.x-5,self.rect.y-20,fill,bar_height)
        pygame.draw.rect(win121,(255,0,0),fill_win)
           