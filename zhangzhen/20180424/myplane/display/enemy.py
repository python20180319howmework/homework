#作者：zhangzhen
#日期：18-4-19
#内容：
"""
    定义敌机
"""

from random import randint

import pygame


class SmallEnemy(pygame.sprite.Sprite):
    """
    定义小飞机敌人
    """
    energy = 3
    def __init__(self, bg_size):
        super(SmallEnemy, self).__init__()
        self.image = pygame.image.load("../image/enemy1.png")
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 获取飞机图像的非透明区域
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 1
        # 定义敌机出现的位置
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width),  randint(-5 * self.height, 0),
        )
        self.active = True
        self.energy = SmallEnemy.energy
        # 加载飞机损毁图片
        self.destroy_images = []
        self.destroy_images.extend(
            [
                pygame.image.load("../image/enemy1_down1.png"),
                pygame.image.load("../image/enemy1_down2.png"),
                pygame.image.load("../image/enemy1_down3.png"),
                pygame.image.load("../image/enemy1_down4.png")
            ]
        )

    def move(self):
        """
        定义敌机的移动函数

        """
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        当敌机向下移动出屏幕时敌机死亡

        """
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width), randint(-5 * self.height, 0))
        self.active = True

class MidEnemy(pygame.sprite.Sprite):
    """
    定义中飞机敌人
    """
    energy = 5
    def __init__(self, bg_size):
        super(MidEnemy, self).__init__()
        self.image = pygame.image.load("../image/enemy2.png")
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 获取飞机图像的非透明区域
        self.mask = pygame.mask.from_surface(self.image)
        self.speed =1
        # 定义敌机出现的位置
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width),  randint(-10 * self.height, -5*self.height),
        )
        self.active = True
        self.energy = MidEnemy.energy
        # 加载飞机损毁图片
        self.destroy_images = []
        self.destroy_images.extend(
            [
                pygame.image.load("../image/enemy2_down1.png"),
                pygame.image.load("../image/enemy2_down2.png"),
                pygame.image.load("../image/enemy2_down3.png"),
                pygame.image.load("../image/enemy2_down4.png")
            ]
        )

    def move(self):
        """
        定义敌机

        """
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        当敌机向下移动出屏幕时敌机死亡

        """
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width), randint(-10 * self.height, -5*self.height))
        self.active = True
        self.energy = MidEnemy.energy

class BigEnemy(pygame.sprite.Sprite):
    """
    定义大飞机敌人
    """
    energy = 10
    def __init__(self, bg_size):
        super(BigEnemy, self).__init__()
        self.image1 = pygame.image.load("../image/enemy3_n1.png")
        self.image2 = pygame.image.load("../image/enemy3_n2.png")
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 获取飞机图像的非透明区域
        self.mask = pygame.mask.from_surface(self.image1)
        self.speed = 1
        # 定义敌机出现的位置
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width),  randint(-15 * self.height, -10*self.height),
        )
        self.active = True
        self.energy = BigEnemy.energy
        # 加载飞机损毁图片
        self.destroy_images = []
        self.destroy_images.extend(
            [
                pygame.image.load("../image/enemy3_down1.png"),
                pygame.image.load("../image/enemy3_down2.png"),
                pygame.image.load("../image/enemy3_down3.png"),
                pygame.image.load("../image/enemy3_down4.png"),
                pygame.image.load("../image/enemy3_down5.png"),
                pygame.image.load("../image/enemy3_down6.png")
            ]
        )

    def move(self):
        """
        定义敌机的移动函数

        """
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        当敌机向下移动出屏幕时敌机死亡

        """
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width), randint(-15 * self.height, -10*self.height))
        self.active = True
        self.energy = BigEnemy.energy