import pygame
from pygame.locals import *
import random

class EnemyPlane1(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 图片
        self.image = pygame.image.load('./images/enemy1.png').convert_alpha()
        self.rect = self.image.get_rect()
        # 撞击图片
        self.destroy_image = [pygame.image.load("./images/enemy1_down1.png").convert_alpha(), \
                              pygame.image.load("./images/enemy1_down2.png").convert_alpha(), \
                              pygame.image.load("./images/enemy1_down3.png").convert_alpha(), \
                              pygame.image.load("./images/enemy1_down4.png").convert_alpha()]
        #位置
        self.width=bg_size.width
        self.height=bg_size.height
        self.rect.left, self.rect.top =(random.randint(0,self.width-self.rect.width),\
                                        random.randint(-5*self.height,0))
        # 获取图片非透明区域
        self.mask = pygame.mask.from_surface(self.image)
        # 速度
        self.speed = 3
        # 状态
        self.alive = True

    def move(self):
        if self.rect.bottom >self.height:
            self.reset()
        else:
            self.rect.top += self.speed
    def reset(self):
        self.alive = True
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-5 * self.height, 0))

class EnemyPlane2(pygame.sprite.Sprite):
    energy=10
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 图片
        self.image = pygame.image.load("./images/enemy2.png").convert_alpha()
        self.rect = self.image.get_rect()
        # 撞击图片
        self.destroy_image = [pygame.image.load("./images/enemy2_down1.png").convert_alpha(), \
                              pygame.image.load("./images/enemy2_down2.png").convert_alpha(), \
                              pygame.image.load("./images/enemy2_down3.png").convert_alpha(), \
                              pygame.image.load("./images/enemy2_down4.png").convert_alpha()]
        #位置
        self.width = bg_size.width
        self.height = bg_size.height
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-10 * self.height, -5*self.height))
        # 获取图片非透明区域
        self.mask = pygame.mask.from_surface(self.image)
        # 速度
        self.speed = 2
        #能量
        self.energy=EnemyPlane2.energy
        # 状态
        self.alive = True
    def move(self):
        if self.rect.bottom > self.height:
            self.reset()
        else:
            self.rect.top += self.speed
    def reset(self):
        self.alive = True
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-10 * self.height, -5 * self.height))
        self.energy=EnemyPlane2.energy

class EnemyPlane3(pygame.sprite.Sprite):
    energy=15
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 图片
        self.image1 = pygame.image.load('./images/enemy3_n1.png').convert_alpha()
        self.image2 = pygame.image.load("./images/enemy3_n2.png")
        self.rect = self.image1.get_rect()
        # 撞击图片
        self.destroy_image = [pygame.image.load("./images/enemy3_down1.png").convert_alpha(), \
                              pygame.image.load("./images/enemy3_down2.png").convert_alpha(), \
                              pygame.image.load("./images/enemy3_down3.png").convert_alpha(), \
                              pygame.image.load("./images/enemy3_down4.png").convert_alpha(), \
                              pygame.image.load("./images/enemy3_down5.png").convert_alpha(), \
                              pygame.image.load("./images/enemy3_down6.png").convert_alpha(), ]
        #位置
        self.width = bg_size.width
        self.height = bg_size.height
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-15* self.height, -10*self.height))
        #速度
        self.speed = 1
        #能量
        self.energy=EnemyPlane3.energy
        # 状态
        self.alive = True
        # 获取图片非透明区域
        self.mask = pygame.mask.from_surface(self.image1)
        self.mask = pygame.mask.from_surface(self.image2)

    def move(self):
        if self.rect.bottom > self.height:
            self.reset()
        else:
            self.rect.top += self.speed
    def reset(self):
        self.alive=True
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-15 * self.height, -10*self.height))
        self.energy=EnemyPlane3.energy