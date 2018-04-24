import pygame
from random import randint
class Enemy(pygame.sprite.Sprite):
    def __init__(self,img_path,arg,bg_img,speed,energy):
        pygame.sprite.Sprite.__init__(self)
        self.energy=energy
        self.image=pygame.image.load(img_path).convert_alpha()
        self.mask=pygame.mask.from_surface(self.image)
        self.destroy_small_image=[pygame.image.load('../images/enemy1_down1.png').convert_alpha(),\
                                  pygame.image.load('../images/enemy1_down2.png').convert_alpha(),\
                                  pygame.image.load('../images/enemy1_down3.png').convert_alpha(),\
                                  pygame.image.load('../images/enemy1_down4.png').convert_alpha()]
        self.destroy_mid_image=[pygame.image.load('../images/enemy2_down1.png').convert_alpha(),\
                                pygame.image.load('../images/enemy2_down2.png').convert_alpha(),\
                                pygame.image.load('../images/enemy2_down3.png').convert_alpha(),\
                                pygame.image.load('../images/enemy2_down4.png').convert_alpha()]
        self.destroy_large_image=[pygame.image.load('../images/enemy3_down1.png').convert_alpha(),\
                                  pygame.image.load('../images/enemy3_down2.png').convert_alpha(),\
                                  pygame.image.load('../images/enemy3_down3.png').convert_alpha(),\
                                  pygame.image.load('../images/enemy3_down4.png').convert_alpha(),\
                                  pygame.image.load('../images/enemy3_down5.png').convert_alpha(),\
                                  pygame.image.load('../images/enemy3_down6.png').convert_alpha()]
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=(randint(0,bg_img.get_width()-self.rect.width),\
                                      randint(-arg*bg_img.get_height(),-arg/2*bg_img.get_height()))
        self.bg_img=bg_img
        self.speed=speed
        self.alive=True

    def move(self):
        if self.rect.top>=self.bg_img.get_height():
            self.alive=False
        else:
            self.rect.top+=self.speed

    def reset(self,arg1,arg2,energy):
        self.rect.left,self.rect.top=(randint(0,self.bg_img.get_width()-self.rect.width),\
                                      randint(-arg1*self.bg_img.get_height(),-arg2*self.bg_img.get_height()))
        self.alive=True
        self.energy=energy




