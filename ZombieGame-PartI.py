
#windows setting
windows_width=900
windows_height=600

#background
sky=(117,248,250)
#0012
import os
file=os.getcwd()
grass_image=file+"\\level_menu\\grass.jpg"
#fsdfds
zombieX=800
zombieY=400
zombieW=50
zombieH=100

#0001
import Grass
grass=Grass.grass_setings(grass_image,sky)

import Enemiy
zombie=Enemiy.enemiy2(zombieX,zombieY,zombieW,zombieH)
zom=Enemiy.Enemiy3(zombieW,zombieH,zombieY)

import time

#7676
import pygame
pygame.init()

fbs=pygame.time.Clock()
#0018
windows=pygame.display.set_mode((windows_width,windows_height))

import Player
player=Player.PlayerAnime()

import Home
homeHole=Home.Stars()

import bullet
#BULLET=bullet.Bullet()

#0100
all_grass=pygame.sprite.Group()
all_player=pygame.sprite.Group()
all_bullet1=pygame.sprite.Group()
all_zombie=pygame.sprite.Group()
all_zombie2=pygame.sprite.Group()
all_hole=pygame.sprite.Group()

all_grass.add(grass)
all_hole.add(homeHole)
all_player.add(player)
all_zombie.add(zombie)

pngicon=pygame.image.load(file+"\\menu\\zzz.png")
#0014

import Level_menu


attack=[True,False]
def event_update():
    for quit in pygame.event.get():
        if quit.type==pygame.QUIT:
            exit()
        elif quit.type==pygame.MOUSEBUTTONUP:
            if quit.button==1:
              player.bullet1(all_bullet1,all_player)
      

import MenuSetting
MenuSetting.main(windows)
import random


#zombie-liter
for i in range(5,14):
    zombie2=Enemiy.Enemiy3(zombieW,zombieH,zombieY)
    all_zombie2.add(zombie2)


#scor
scortext=pygame.font.SysFont("comicsansms",30)
belltext=pygame.font.SysFont("comicsansms",15)
bellenemiy=pygame.font.SysFont("comicsansms",15)
bellenemiy2=pygame.font.SysFont("comicsansms",15)

scor=0
bell=100
enbell=100
enbell2=100
T=False
def collison():
    global scor,bell,enbell,enbell2,scortext,belltext,bellenemiy,T
    hit=pygame.sprite.groupcollide(all_zombie,all_bullet1,False,True)
    if hit:
        zombie.bell-=1.5
        scor+=10
        enbell-=1.5
    elif zombie.bell <=0:
        zombie.rect.y=2000
    hit2=pygame.sprite.spritecollide(player,all_zombie,False)
    if hit2:
        player.bell-=0.1
        bell-=0.1
    elif player.bell <=0:
        player.rect.x=-2000
        player.rect.y-=10
    #2
    hitz1=pygame.sprite.groupcollide(all_zombie2,all_bullet1,T,True)
    if hitz1:
        zom.bell-=5
        scor+=20
        enbell2-=5
    elif zom.bell <=0:
        T=True
        zombie2.rect.y=2000
    hitz2=pygame.sprite.spritecollide(player,all_zombie2,False)
    if hitz2:
        player.bell-=0.1
        bell-=0.1
    elif player.bell <=0:
        player.rect.x=-2000
        player.rect.y-=10
    elif scor==1230:
        Level_menu.Menu_run2(windows)

    bellrender=belltext.render("%"+str(bell)+"attack",10,(0,0,0))
    scorRender=scortext.render(str(scor)+"/1230",15,(0,0,0))
    Enerender=bellenemiy.render("%"+str(enbell)+"attack",10,(0,0,0))
    Enerender2=bellenemiy2.render("%"+str(enbell)+"attack",10,(0,0,0))
    windows.blit(scorRender,(700,20))
    windows.blit(bellrender,(player.rect.x-30,player.rect.y-40))
    windows.blit(Enerender,(zombie.rect.x-30,zombie.rect.y-40))
    windows.blit(Enerender2,(100,10))


pygame.display.set_caption("zombie part:I")

while True:
    FBS=random.randrange(35,40)
    #0020aaa
    windows.fill(sky)
    event_update()
    #0025a
    fbs.tick(FBS)
    #009   
    all_grass.update()
    #903
    all_grass.draw(windows)
    #enemiy
    all_zombie.update(windows)
    all_zombie2.update(windows)
   
    #PLAYER AND BULLET
    all_player.update(windows)
    #BELL
    player.shiled(windows)
    zombie.shiled(windows,40,20,10)
    zom.shiled(windows,100,380,5)

    all_hole.update()

    collison()

    all_hole.draw(windows)
    pygame.display.set_icon(pngicon)

    pygame.display.update()


