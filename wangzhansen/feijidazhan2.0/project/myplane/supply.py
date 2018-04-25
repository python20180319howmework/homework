
import pygame
from random import *



class Bomb_Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./images/bomb_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size.width, bg_size.height
        #self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = randint(0, 400),-100
        self.speed = 5
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top > self.height:
            self.active = False
        else:

            self.rect.top += self.speed

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100