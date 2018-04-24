import pygame
import  random

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load('../images/bullet1.png').convert_alpha()
        self.image2 = pygame.image.load('../images/bullet2.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.rect.left, self.rect.top = pos
        self.speed =12
        self.alive=True
        self.mask = pygame.mask.from_surface(self.image1)
        self.mask = pygame.mask.from_surface(self.image2)
    def move(self):
        if self.rect.top < 0:
            self.alive=False
        else:
            self.rect.top -= self.speed
    def reset(self,pos):
        self.rect.left, self.rect.top = pos
        self.alive=True

class Bomb(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../images/bomb_supply.png').convert_alpha()
        self.rect = self.image.get_rect()
        # 位置
        self.width = bg_size.width
        self.height = bg_size.height
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-10 * self.height, -5 * self.height))
        self.speed = 5
        self.alive = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < 0:
            self.alive = False
            self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                             random.randint(-10 * self.height, -2 * self.height))
        else:
            self.rect.top -= self.speed