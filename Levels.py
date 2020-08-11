import pygame
from pygame.sprite import Sprite
import os
from enum import Enum
import Level_menu
import MenuSetting

file=os.getcwd()

level_1=[pygame.image.load(file+"\\levels\\level_on1.jpg"),
          pygame.image.load(file+"\\levels\\level_off1.jpg")]

level_2=[pygame.image.load(file+"\\levels\\level_on2.jpg"),
         pygame.image.load(file+"\\levels\\level_off2.jpg")]

level_3=[pygame.image.load(file+"\\levels\\level_on3.jpg"),
         pygame.image.load(file+"\\levels\\level_off3.jpg")]

level_4=[pygame.image.load(file+"\\levels\\level_on4.png"),
         pygame.image.load(file+"\\levels\\level_off4.png")]

level_5=[pygame.image.load(file+"\\levels\\level_on5.png"),
         pygame.image.load(file+"\\levels\\level_off5.png")]

home=[pygame.image.load(file+"\\levels\\home\\home_on.png"),
      pygame.image.load(file+"\\levels\\home\\home_off.png")]

level2_x=10
level2_y=10

class Level1:
    def __init__(self,levelPosition,go):
        self.mouse_click=False
        self.level_go=go
        level_button1=level_1[0]
        level_button2=level_1[1]
        self.images=[level_button1,level_button2]
        self.rects=[level_button1.get_rect(center=levelPosition),
                    level_button2.get_rect(center=levelPosition)]
    @property
    def image(self):
        return self.images[1] if self.mouse_click else self.images[0]
    @property
    def rect(self):
        return self.rects[1] if self.mouse_click  else self.rects[0]
    def update(self,mouse_up,mouse_go):
        if self.rect.collidepoint(mouse_up):
            self.mouse_click=True
            if mouse_go:return self.level_go
        else:self.mouse_click=False
    def Run(self,Windows):
        Windows.blit(self.image,self.rect)

class Level2:
    def __init__(self,levelPosition,go):
        self.mouse_click=False
        self.level_go=go
        level_button1=level_2[0]
        level_button2=level_2[1]
        self.images=[level_button1,level_button2]
        self.rects=[level_button1.get_rect(center=levelPosition),
                    level_button2.get_rect(center=levelPosition)]
    @property
    def image(self):
        return self.images[1] if self.mouse_click else self.images[0]
    @property
    def rect(self):
        return self.rects[1] if self.mouse_click  else self.rects[0]
    def update(self,mouse_up,mouse_go):
        if self.rect.collidepoint(mouse_up):
            self.mouse_click=True
            if mouse_go:
                return self.level_go
        else:self.mouse_click=False
    def Run2(self,Windows):
        Windows.blit(self.image,self.rect)

class Level3:
    def __init__(self,levelPosition,go):
        self.mouse_click=False
        self.level_go=go
        level_button1=level_3[0]
        level_button2=level_3[1]
        self.images=[level_button1,level_button2]
        self.rects=[level_button1.get_rect(center=levelPosition),
                    level_button2.get_rect(center=levelPosition)]
    @property
    def image(self):
        return self.images[1] if self.mouse_click else self.images[0]
    @property
    def rect(self):
        return self.rects[1] if self.mouse_click  else self.rects[0]
    def update(self,mouse_up,mouse_go):
        if self.rect.collidepoint(mouse_up):
            self.mouse_click=True
            if mouse_go:return self.level_go
        else:self.mouse_click=False
    def Run3(self,Windows):
        Windows.blit(self.image,self.rect)

class Level4:
    def __init__(self,levelPosition,go=None):
        self.mouse_click=False
        self.level_go=go
        level_button1=level_4[0]
        level_button2=level_4[1]
        self.images=[level_button1,level_button2]
        self.rects=[level_button1.get_rect(center=levelPosition),
                    level_button2.get_rect(center=levelPosition)]
    @property
    def image(self):
        return self.images[1] if self.mouse_click else self.images[0]
    @property
    def rect(self):
        return self.rects[1] if self.mouse_click  else self.rects[0]
    def update(self,mouse_up,mouse_go):
        if self.rect.collidepoint(mouse_up):
            self.mouse_click=True
            if mouse_go:return self.level_go
        else:self.mouse_click=False
    def Run4(self,Windows):
        Windows.blit(self.image,self.rect)


class Home:
    def __init__(self,levelPosition,go):
        self.mouse_click=False
        self.level_go=go
        home_button1=home[0]
        home_button2=home[1]
        self.images=[home_button1,home_button2]
        self.rects=[home_button1.get_rect(center=levelPosition),
                    home_button2.get_rect(center=levelPosition)]
    @property
    def image(self):
        return self.images[1] if self.mouse_click else self.images[0]
    @property
    def rect(self):
        return self.rects[1] if self.mouse_click  else self.rects[0]
    def update(self,mouse_up,mouse_go):
        if self.rect.collidepoint(mouse_up):
            self.mouse_click=True
            if mouse_go:return self.level_go
        else:self.mouse_click=False
    def Run6(self,Windows5):
        Windows5.blit(self.image,self.rect)
class LevelStatusGo(Enum):
    LevelGo1=1
    LevelGo2=2
    LevelGo3=3
    LevelGo4=4
    menuHome=6




def Run_Levels(windows):
    all_level1=Level1((level2_x*20,level2_y*11),LevelStatusGo.LevelGo1)
    all_level2=Level2((level2_x*45,level2_y*11),LevelStatusGo.LevelGo2)
    all_level3=Level3((level2_x*70,level2_y*11),LevelStatusGo.LevelGo3)
    all_level4=Level4((level2_x*20,level2_y*30),LevelStatusGo.LevelGo4)
    #all_level5=Level5((level2_x*45,level2_y*30))
    all_home=Home((level2_x*10,level2_y*50),LevelStatusGo.menuHome)
    while True:
        Mouse_full=False
        for event_mouse in pygame.event.get():
            if event_mouse.type==pygame.QUIT:
                exit()
            if event_mouse.type==pygame.MOUSEBUTTONUP:
                if event_mouse.button==1:
                   Mouse_full=True
        windows.fill((214,234,248))
        insertLevel1=all_level1.update(pygame.mouse.get_pos(),Mouse_full)
        if insertLevel1:
            return Mouse_full
        all_level1.Run(windows)
        insertLevel2=all_level2.update(pygame.mouse.get_pos(),Mouse_full)
        if insertLevel2:
            return Level_menu.Menu_run2(windows)
        all_level2.Run2(windows)

        insertLevel3=all_level3.update(pygame.mouse.get_pos(),Mouse_full)
        if insertLevel3:
            return Level_menu.Menu_run3(windows)
        all_level3.Run3(windows)

        insertLevel4=all_level4.update(pygame.mouse.get_pos(),Mouse_full)
        if insertLevel4:
            return Level_menu.Menu_run4(windows)
        all_level4.Run4(windows)    

        inserthome=all_home.update(pygame.mouse.get_pos(),Mouse_full)
        if inserthome:
            MenuSetting.main(windows)
        all_home.Run6(windows)

        pygame.display.update()
