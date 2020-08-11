import pygame
import os
from pygame.sprite import Sprite
from enum import Enum
import random
file=os.getcwd()
import Levels
image_menu=file+"\\menu\\bg_sky.png"
music_click=file+"\\menu\\soung\\clicksoung.wav"
menu_music1=file+"\\menu\\soung\\menu1.wav"
menu_music2=file+"\\menu\\soung\\menu2.mp3"

pygame.mixer.init()
menu=pygame.image.load(image_menu)
menu_w=900
menu_h=600
start_button=[pygame.image.load(file+"\\menu\\start1.png"),
              pygame.image.load(file+"\\menu\\start2.png")]

about_button=[pygame.image.load(file+"\\menu\\about1.png"),
              pygame.image.load(file+"\\menu\\about2.png")]
exit_button=[pygame.image.load(file+"\\menu\\exit1.png"),
              pygame.image.load(file+"\\menu\\exit2.png")]

cloud=[pygame.image.load(file+"\\menu\\appcloud\\Cloud.png"),
       pygame.image.load(file+"\\menu\\appcloud\\Cloud2.png")]
class Menu(Sprite):
    def __init__(self):
        super().__init__()
        self.image=menu
        self.image=pygame.transform.scale(self.image,(menu_w,menu_h))
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
    def update(self):
        #self.rect.x-=1
        pass


cloudX=-200
cloudX2=menu_w+50
cloudxcor=1
cloudxcor2=1
sin=20
def Cloud(Windows):
    global cloudX,cloudxcor,cloudX2,cloudxcor2
    cloudY1=random.randrange(1,3)
    cloudY2=100
    cloudspeed=1
    x=random.randrange(-300,-250)
    x1=random.randrange(100,150)
    if cloudX <x or cloudX>menu_w+x1:
        cloudxcor*=-1
    cloudX+=cloudspeed*cloudxcor
    if cloudX2>menu_w+x1 or cloudX2<-450:
        cloudxcor2*=-1
    cloudX2-=cloudspeed*cloudxcor2
    image=cloud[0]
    image2=cloud[1]
    for i in range(random.randrange(1,7)):
       Windows.blit(image,(cloudX,cloudY1))
    for s in range(random.randrange(1,3)):
       Windows.blit(image2,(cloudX2,cloudY2))



class Snow(Sprite):
    def __init__(self):
        super().__init__()
        self.image_copy=pygame.image.load(file+"\\menu\\snow\\snow.png")
        self.image=self.image_copy.copy()
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(menu_w-self.rect.width)
        self.rect.y=random.randrange(-50,-10)
        self.speedy=random.randrange(1,4)
        self.speedx=random.randrange(-5,5)
        self.R=0
        self.R_speed=random.randrange(-1,5)
        self.R_update=pygame.time.get_ticks()
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.y >menu_h:
            self.rect.x=random.randrange(menu_w-self.rect.width)
            self.rect.y=random.randrange(-50,-10)
            self.speedy=random.randrange(1,4)
        self.Radius()
    def Radius(self):
        new=pygame.time.get_ticks()
        new=self.R_update
        if new>-50:
            self.R=(self.R+self.R_speed)%360
            new_image=pygame.transform.rotate(self.image_copy,self.R)
            new_center=self.rect.center
            self.image=new_image
            self.rect=self.image.get_rect()
            self.rect.center=new_center

all_snow=pygame.sprite.Group()

for i in range(random.randrange(20,50)):
    snow=Snow()
    all_snow.add(snow)


#start Button
class Start:
    def __init__(self,center_position,action):
        self.mouse=False
        self.start_action=action
        button1=start_button[0]
        button2=start_button[1]
        self.images=[button1,button2]
        self.rects=[button1.get_rect(center=center_position),
                    button2.get_rect(center=center_position)]
    @property
    def image(self):
        return self.images[1] if self.mouse else self.images[0]
    @property
    def rect(self):
        return self.rects[1] if self.mouse else self.rects[0]
    def update(self,mouse_pos,start_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse=True
            if start_up:
                return self.start_action
        else:
            self.mouse=False
    def draw(self, wind64):
        wind64.blit(self.image,self.rect)
       
class About:
    def __init__(self,center_position):
        self.mouse1=False
        button_about1=about_button[0]
        button_about2=about_button[1]
        self.images=[button_about1,button_about2]
        self.rects=[button_about1.get_rect(center=center_position),
                    button_about2.get_rect(center=center_position)]
    @property
    def image(self):
        return self.images[1] if self.mouse1 else self.images[0]
    @property
    def rect(self):
        return self.rects[1] if self.mouse1 else self.rects[0]
    def update(self,mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.mouse1=True
        else:
            self.mouse1=False
    def draw(self, wind64):
        wind64.blit(self.image,self.rect)

class Exit:
    def __init__(self,center_position,action=None):
        self.mouse_exit=False
        self.exitAction=action
        button_exit1=exit_button[0]
        button_exit2=exit_button[1]
        self.images=[button_exit1,button_exit2]
        self.rects=[button_exit1.get_rect(center=center_position),
                    button_exit2.get_rect(center=center_position)]
    @property
    def image(self):
        return self.images[1] if self.mouse_exit else self.images[0]
    @property
    def rect(self):
        return self.rects[1] if self.mouse_exit else self.rects[0]
    def update(self,mouse_pos,mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_exit=True
            if mouse_up:
                return self.exitAction
        else:
            self.mouse_exit=False
    def draw(self, wind32):
        wind32.blit(self.image,self.rect)
    
all_menu=pygame.sprite.Group()

class GameStatus(Enum):
    QUIT=1
    START=2

def Menu_soung():
    Intiger=random.randint(1,2)
    pygame.mixer.music.load(menu_music1)
    pygame.mixer.music.load(menu_music2)
    pygame.mixer.music.load(music_click)
   
pngicon=pygame.image.load(file+"\\menu\\zzz.png")
#0014
pygame.display.set_caption("zombie part:I")
def main(windows):
    run=False
    pygame.init()
    main_menu=Menu()
    all_menu.add(main_menu)
    main_start=Start((menu_w/2,menu_h/2),GameStatus.START)
    main_about=About((menu_w/2,menu_h/2+60))
    main_exit=Exit((menu_w/2,menu_h/2+120),GameStatus.QUIT)
    while True:
        mouse_exit=False
        for menu_setting in pygame.event.get():
            if menu_setting.type==pygame.QUIT:
                exit()
            if menu_setting.type==pygame.MOUSEBUTTONDOWN:
                if menu_setting.button==1:
                    mouse_exit=True
        all_menu.update()
        all_menu.draw(windows)
        
        #starting game Levels windows
        starting=main_start.update(pygame.mouse.get_pos(),mouse_exit)
        if starting:
            return Levels.Run_Levels(windows)
        main_start.draw(windows)

        main_about.update(pygame.mouse.get_pos())
        main_about.draw(windows)
        
        #exiting windows breka
        exiting=main_exit.update(pygame.mouse.get_pos(),mouse_exit)
        if exiting:
            exit()
        main_exit.draw(windows)
        Cloud(windows)
        all_snow.update()
        all_snow.draw(windows)
        pygame.display.set_icon(pngicon)
        pygame.display.update()
