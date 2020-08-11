import pygame
from pygame.sprite import Sprite
import os
import random

file=os.getcwd()

level_menu2=pygame.image.load(file+"\\level_menu\\grass1.jpg")
level_menu3=pygame.image.load(file+"\\level_menu\\grass2.jpg")
level_menu4=pygame.image.load(file+"\\level_menu\\MoonBG.png")
level_menu5=pygame.image.load(file+"\\level_menu\\SnowBG.png")
menus_x=0
menus_y=0
import Home
hole=Home.Stars()
all_star=pygame.sprite.Group()
all_star.add(hole)
import Player
player=Player.PlayerAnime()
all_player=pygame.sprite.Group()
all_bullet=pygame.sprite.Group()#BULLET
all_player.add(player)
import Enemiy
zombieX=800
zombieY=400
zombieW=50
zombieH=100
zombies1=range(1,3)
zombies2=range(1,6)
zombies3=range(1,9)
zombies4=range(1,12)

Zombie1=range(10,17)
Zombie2=range(15,25)
Zombie3=range(20,30)

all_zombie1=pygame.sprite.Group()
all_zombie2=pygame.sprite.Group()
all_zombie3=pygame.sprite.Group()

all_Zombie1=pygame.sprite.Group()
all_Zombie2=pygame.sprite.Group()
all_Zombie3=pygame.sprite.Group()
all_Zombie4=pygame.sprite.Group()

zombie=Enemiy.enemiy2(zombieX,zombieY,zombieW,zombieH)
zombie22=Enemiy.Enemiy3(zombieW,zombieH,zombieY)

#big zombies
for i in zombies1:
    zombie1=Enemiy.enemiy2(zombieX,zombieY,zombieW,zombieH)
    all_Zombie1.add(zombie1)
for x in zombies3:
    zombie2=Enemiy.enemiy2(zombieX,zombieY,zombieW,zombieH)
    all_Zombie3.add(zombie2)   
for d in zombies4:
    zombie3=Enemiy.enemiy2(zombieX,zombieY,zombieW,zombieH)
    all_Zombie4.add(zombie3)   

#leyter Zombie
for zet in Zombie1:
    zombie20=Enemiy.Enemiy3(zombieW,zombieH,zombieY)
    all_zombie1.add(zombie20)
for log in Zombie2:
    zombie21=Enemiy.Enemiy3(zombieW,zombieH,zombieY)
    all_zombie2.add(zombie21)
for sin in Zombie3:
    zombie23=Enemiy.Enemiy3(zombieW,zombieH,zombieY)
    all_zombie3.add(zombie23)
#collison
T=False
t=False
bell=100
enbell=100
enbell2=100
scor=0
scortext=pygame.font.SysFont("comicsansms",30)
belltext=pygame.font.SysFont("comicsansms",15)
bellenemiy=pygame.font.SysFont("comicsansms",15)
bellenemiy2=pygame.font.SysFont("comicsansms",15)
def collison2(windows):
    global T,t,scor,bell,enbell,enbell2,scortext,belltext,bellenemiy,bellenemiy2
    hitZ1=pygame.sprite.spritecollide(player,all_Zombie1,False)
    if hitZ1:
        player.bell-=0.1
        bell-=0.1
    elif player.bell <=0:
        player.rect.x=-2000
        player.rect.y=2000
    hitZ2=pygame.sprite.groupcollide(all_Zombie1,all_bullet,T,True)
    if hitZ2:
        zombie.bell-=2.5
        scor+=50
        enbell-=2.5
    elif zombie.bell <=0:
        zombie1.rect.x=2000
        T=True
    hitz1=pygame.sprite.spritecollide(player,all_zombie1,False)
    if hitz1:
        player.bell-=0.1
        bell-=0.1
    elif player.bell <=0:
        player.rect.x=-2000
        player.rect.y=-2000
    hitz2=pygame.sprite.groupcollide(all_zombie1,all_bullet,t,True)
    if hitz2:
        zombie22.bell-=3.5
        scor+=40
        enbell2-=3.5
    elif zombie22.bell <=0:
        zombie20.rect.y=2000
        t=True
    elif scor==3450:
        Menu_run3(windows)
    bellrender=belltext.render("%"+str(bell)+"attack",10,(0,0,0))
    Enerender=bellenemiy.render("%"+str(enbell)+"attack",10,(0,0,0))
    Enerender2=bellenemiy2.render("%"+str(enbell2)+"attack",10,(0,0,0))
    scorRender=scortext.render(str(scor)+"/3450",15,(0,0,0))
    windows.blit(scorRender,(700,20))
    windows.blit(bellrender,(player.rect.x-30,player.rect.y-40))
    windows.blit(Enerender,(100,10))
    windows.blit(Enerender2,(430,10))

def collison3(windows):
    global T,t,scor,bell,enbell,enbell2,scortext,belltext,bellenemiy,bellenemiy2
    hitZ1=pygame.sprite.spritecollide(player,all_Zombie3,False)
    if hitZ1:
        player.bell-=0.1
        bell-=0.1
    elif player.bell <=0:
        player.rect.x=-2000
        player.rect.y=2000
    hitZ2=pygame.sprite.groupcollide(all_Zombie3,all_bullet,T,True)
    if hitZ2:
        zombie.bell-=3.5
        scor+=100
        enbell-=3.5
    elif zombie.bell <=0:
        zombie2.rect.x=2000
        T=True
    hitz1=pygame.sprite.spritecollide(player,all_zombie2,False)
    if hitz1:
        player.bell-=0.1
        bell-=0.1
    elif player.bell<=0:
        player.rect.x-=2000
        player.rect.y=2000
    hitz2=pygame.sprite.groupcollide(all_zombie2,all_bullet,t,True)
    if hitz2:
        zombie22.bell-=4.5
        scor+=50
        enbell2-=4.5
    elif zombie22.bell<=0:
        zombie21.rect.y=2000
        t=True
    bellrender=belltext.render("%"+str(bell)+"attack",10,(0,0,0))
    Enerender=bellenemiy.render("%"+str(enbell)+"attack",10,(0,0,0))
    Enerender2=bellenemiy2.render("%"+str(enbell2)+"attack",10,(0,0,0))
    scorRender=scortext.render(str(scor)+"/5200",15,(0,0,0))
    windows.blit(scorRender,(700,20))
    windows.blit(bellrender,(player.rect.x-30,player.rect.y-40))
    windows.blit(Enerender,(100,10))
    windows.blit(Enerender2,(430,10))

def collison4(windows):
    global T,t,scor,bell,enbell,enbell2,scortext,belltext
    hitZ1=pygame.sprite.spritecollide(player,all_Zombie4,False)
    if hitZ1:
        player.bell-=0.1
        bell-=0.5
    if player.bell <=0:
        player.rect.x=-2000
    hitZ2=pygame.sprite.groupcollide(all_Zombie4,all_bullet,T,True)
    if hitZ2:
        zombie.bell-=5.5
        scor+=200
        enbell-=5.5
    if zombie.bell <=0:
        zombie3.rect.x=2000
        T=True
    hitz1=pygame.sprite.spritecollide(player,all_zombie3,False)
    if hitz1:
        player.bell-=0.2
        bell-=0.2
        enbell2-=0.2
    elif player.bell<=0:
        player.rect.x=-2000
        player.rect.y=2000
    hitz2=pygame.sprite.groupcollide(all_zombie3,all_bullet,t,True)
    if hitz2:
        zombie22.bell-=10.5
        scor+=100
    elif zombie22.bell<=0:
        zombie23.rect.y=2000
        t=True
    bellrender=belltext.render("%"+str(bell)+"attack",10,(0,0,0))
    Enerender=bellenemiy.render("%"+str(enbell)+"attack",10,(0,0,0))
    Enerender2=bellenemiy2.render("%"+str(enbell2)+"attack",10,(0,0,0))
    scorRender=scortext.render(str(scor)+"/7700",15,(0,0,0))
    windows.blit(scorRender,(700,20))
    windows.blit(bellrender,(player.rect.x-30,player.rect.y-40))
    windows.blit(Enerender,(100,10))
    windows.blit(Enerender2,(430,10))


class LevelMenu2:
    def __init__(self):
        #super().__init__()
        self.menu2=level_menu2
        self.rect=(menus_x,menus_y)
    def Run(self,windows):
        windows.blit(self.menu2,self.rect)

class LevelMenu3:
    def __init__(self):
        #super().__init__()
        self.menu3=level_menu3
        self.rect=(menus_x,menus_y)
    def Run(self,windows):
        windows.blit(self.menu3,self.rect)

class LevelMenu4:
    def __init__(self):
        #super().__init__()
        self.menu4=level_menu4
        self.rect=(menus_x,menus_y)
    def Run4(self,windows):
        windows.blit(self.menu4,self.rect)

def Menu_run2(Windows):
    all_level2=LevelMenu2()
    while True:
        for setting in pygame.event.get():
            if setting.type==pygame.QUIT:
                exit()
            elif setting.type==pygame.MOUSEBUTTONUP:
                if setting.button==1:
                   player.bullet1(all_player,all_bullet)
           
        all_level2.Run(Windows)
        all_player.update(Windows)
        player.shiled(Windows)
        #BULLET

        #Zombies
        all_zombie1.update(Windows)
        all_Zombie1.update(Windows)
        zombie.shiled(Windows,400,380,5)
        zombie22.shiled(Windows,100,380,5)
        
        collison2(Windows)

        all_star.update()
        all_star.draw(Windows)
        pygame.display.update()

def Menu_run3(Windows):
    all_level3=LevelMenu3()
    while True:
        for setting in pygame.event.get():
            if setting.type==pygame.QUIT:
                exit()
            elif setting.type==pygame.MOUSEBUTTONUP:
                if setting.button==1:
                    player.bullet1(all_player,all_bullet)

        all_level3.Run(Windows)
        all_player.update(Windows)
        player.shiled(Windows)
        #BULLET

        #ZOMBIES
        all_zombie2.update(Windows)
        all_Zombie3.update(Windows)   
        zombie.shiled(Windows,400,380,5)
        zombie22.shiled(Windows,100,380,5)   
        collison3(Windows)

        all_star.update()
        all_star.draw(Windows)
        pygame.display.update()

def Menu_run4(Windows):
    all_level4=LevelMenu4()
    while True:
        for setting in pygame.event.get():
            if setting.type==pygame.QUIT:
                exit()
            elif setting.type==pygame.MOUSEBUTTONUP:
                if setting.button==1:
                    player.bullet1(all_player,all_bullet)
                  
        all_level4.Run4(Windows)
        all_player.update(Windows)
        player.shiled(Windows)
        #BULLET

        #Zombies
        all_zombie3.update(Windows)
        all_Zombie4.update(Windows)
        zombie.shiled(Windows,400,380,5)
        zombie22.shiled(Windows,100,380,5)
        
        collison4(Windows)

        all_star.update()
        all_star.draw(Windows)
        pygame.display.update()

