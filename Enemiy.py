import pygame
import os
file=os.getcwd()
import random
pygame.init()


zombie_left=[pygame.image.load(file+"\\enemiy\\zombie\\go_0.png"),pygame.image.load(file+"\\enemiy\\zombie\\go_1.png"),
            pygame.image.load(file+"\\enemiy\\zombie\\go_2.png"),pygame.image.load(file+"\\enemiy\\zombie\\go_3.png"),
            pygame.image.load(file+"\\enemiy\\zombie\\go_4.png"),pygame.image.load(file+"\\enemiy\\zombie\\go_5.png"),
            pygame.image.load(file+"\\enemiy\\zombie\\go_6.png"),pygame.image.load(file+"\\enemiy\\zombie\\go_7.png"),
            pygame.image.load(file+"\\enemiy\\zombie\\go_8.png"),pygame.image.load(file+"\\enemiy\\zombie\\go_9.png"),
            pygame.image.load(file+"\\enemiy\\zombie\\go_10.png")]

zombie_right=[pygame.image.load(file+"\\enemiy\\go_right0.png"),pygame.image.load(file+"\\enemiy\\go_right1.png"),
              pygame.image.load(file+"\\enemiy\\go_right2.png"),pygame.image.load(file+"\\enemiy\\go_right3.png"),
              pygame.image.load(file+"\\enemiy\\go_right4.png"),pygame.image.load(file+"\\enemiy\\go_right5.png"),
              pygame.image.load(file+"\\enemiy\\go_right6.png"),pygame.image.load(file+"\\enemiy\\go_right7.png"),
              pygame.image.load(file+"\\enemiy\\go_right8.png"),pygame.image.load(file+"\\enemiy\\go_right9.png"),
              pygame.image.load(file+"\\enemiy\\go_right10.png")]

zombie_death=[pygame.image.load(file+"\\enemiy\\death\\die_1.png"),pygame.image.load(file+"\\enemiy\\death\\die_2.png"),
              pygame.image.load(file+"\\enemiy\\death\\die_3.png"),pygame.image.load(file+"\\enemiy\\death\\die_4.png"),
              pygame.image.load(file+"\\enemiy\\death\\die_5.png"),pygame.image.load(file+"\\enemiy\\death\\die_6.png"),
              pygame.image.load(file+"\\enemiy\\death\\die_7.png"),pygame.image.load(file+"\\enemiy\\death\\die_8.png")]


class enemiy2(pygame.sprite.Sprite):
    def __init__(self,x,y,zombieW,zombieH):
        super(). __init__()
        self.index=0
        self.indexX=0
        self.attackINDEX=0
        self.Image=zombie_right[0]
        self.rect=self.Image.get_rect()
        self.rect.x=x+random.randrange(20,50)
        self.rect.y=y+10
        self.run=random.randint(3,5)
        self.width=zombieW
        self.height=zombieH
        self.radius=2
        self.speed=random.randint(1,4)
        self.bell=100
    def update(self,win64):
        self.move()
        if self.index +1 >=len(zombie_left):
            self.index=0
        if self.run >0:
            win64.blit(pygame.transform.scale(zombie_right[self.index//2],(self.width,self.height)),(self.rect.x,self.rect.y))
            self.index+=1   
        else:
            win64.blit(pygame.transform.scale(zombie_left[self.index//2],(self.width,self.height)),(self.rect.x,self.rect.y))
            self.index+=1
            
    def move(self):
        if self.run >0:
            if self.rect.x <950:
                self.rect.x +=self.speed
            else:
                self.run =self.run *-1
                self.rect.x +=self.speed
                self.index=0
        else:
            if self.rect.x >100:
                self.rect.x +=self.run
            else:
                self.run =self.run *-1
                self.rect.x +=self.run
                self.index=0
    def shiled(self,win1212,x,y,l):
        if self.bell <0:
            self.bell=0
        bar_lenght=100
        bar_height=10
        fill=(self.bell/l)*bar_height
        fill_win=pygame.Rect(self.rect.x-x,self.rect.y-y,fill,bar_height)
        pygame.draw.rect(win1212,(0,0,0),fill_win)



zombie2_right=[pygame.image.load(file+"\\enemiy\\zombie2\\Run1.png"),pygame.image.load(file+"\\enemiy\\zombie2\\Run2.png"),
                pygame.image.load(file+"\\enemiy\\zombie2\\Run3.png"),pygame.image.load(file+"\\enemiy\\zombie2\\Run4.png"),
                pygame.image.load(file+"\\enemiy\\zombie2\\Run5.png"),pygame.image.load(file+"\\enemiy\\zombie2\\Run6.png"),
                pygame.image.load(file+"\\enemiy\\zombie2\\Run6.png"),pygame.image.load(file+"\\enemiy\\zombie2\\Run7.png"),
                pygame.image.load(file+"\\enemiy\\zombie2\\Run8.png"),pygame.image.load(file+"\\enemiy\\zombie2\\Run9.png"),
                pygame.image.load(file+"\\enemiy\\zombie2\\Run10.png")]

zombie2_left=[pygame.image.load(file+"\\enemiy\\zombie2\\zombieleft\\Run1.png"),pygame.image.load(file+"\\enemiy\\zombie2\\zombieleft\\Run2.png"),
              pygame.image.load(file+"\\enemiy\\zombie2\\zombieleft\\Run3.png"),pygame.image.load(file+"\\enemiy\\zombie2\\zombieleft\\Run4.png"),
              pygame.image.load(file+"\\enemiy\\zombie2\\zombieleft\\Run5.png"),pygame.image.load(file+"\\enemiy\\zombie2\\zombieleft\\Run6.png")]

class Enemiy3(pygame.sprite.Sprite):
    def __init__(self,zombiW,zombiH,y):
        super().__init__()
        self.index=0
        self.Image=zombie2_right[0]
        self.rect=self.Image.get_rect()
        self.rect.x=random.randrange(950,1300)
        self.rect.y=y+10
        self.W=zombiW
        self.H=zombiH
        self.speedx=random.randrange(1,3)
        self.bell=100
    def update(self,Windows):
        if self.index+1>=len(zombie2_left):
            self.index=0
        Windows.blit(pygame.transform.scale(zombie2_left[int(self.index)],(self.W,self.H)),(self.rect.x,self.rect.y))
        self.index+=0.5
        self.rect.x-=self.speedx
        if self.rect.x<0:
            self.rect.x=random.randrange(950,1300)
    def shiled(self,win1212,x,y,l):
        if self.bell <0:
            self.bell=0
        bar_lenght=100
        bar_height=10
        fill=(self.bell/l)*bar_height
        fill_win=pygame.Rect(x,self.rect.y-y,fill,bar_height)
        pygame.draw.rect(win1212,(111,111,111),fill_win)

