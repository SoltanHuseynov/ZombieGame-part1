grass_x=0
grass_y=0


import pygame

class grass_setings(pygame.sprite.Sprite):
    def __init__(self,image,color):
        super().__init__()
        self.image=pygame.image.load(image)
        self.image.set_colorkey(color)
        self.rect=self.image.get_rect()
        self.rect.x=grass_x
        self.rect.y=grass_y
