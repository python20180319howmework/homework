import pygame
from random import randint
class BombSupply(pygame.sprite.Sprite):
    def __init__(self,bg_img):
        super().__init__()
        self.image=pygame.image.load('../images/bomb_supply.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=(randint(0,bg_img.get_width()-self.rect.width),\
                                      randint(-10*bg_img.get_height(),-5*bg_img.get_height()))
        self.speed=1
        self.mask=pygame.mask.from_surface(self.image)
        self.alive=True
        self.bg_img=bg_img

    def move(self):
        if self.rect.top>=self.bg_img.get_height():
            self.alive=False
        else:
            self.rect.top+=self.speed

    def reset(self):
        self.rect.left,self.rect.top=(randint(0,self.bg_img.get_width()-self.rect.width),\
                                      randint(-10*self.bg_img.get_height(),-5*self.bg_img.get_height()))
        self.alive=True




