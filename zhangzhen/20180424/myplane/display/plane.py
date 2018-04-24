#作者：zhangzhen
#日期：18-4-19
#内容：
"""
    创建飞机
    实现碰撞的方法 spritecollide

"""

import pygame


class OurPlane(pygame.sprite.Sprite):

    def __init__(self, bg_size):
        super(OurPlane, self).__init__()
        # 确定我方飞机图片
        self.image_one = pygame.image.load("../image/me1.png")
        self.image_two = pygame.image.load("../image/me2.png")
        # 获取我方飞机的位置
        self.rect = self.image_one.get_rect()
        # 背景图片的大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 获取飞机图像的非透明区域
        self.mask = pygame.mask.from_surface(self.image_one)
        # 定义飞机初始化位置，
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 60)
        # 设置飞机移动速度
        self.speed = 10
        # 设置飞机存活状态
        self.active = True
        # 加载飞机损毁图片
        self.destroy_images = []
        self.destroy_images.extend(
            [
                pygame.image.load("../image/me_destroy_1.png"),
                pygame.image.load("../image/me_destroy_2.png"),
                pygame.image.load("../image/me_destroy_3.png"),
                pygame.image.load("../image/me_destroy_4.png")
            ]
        )

    def move_up(self):
        """
        飞机向上移动的操作函数，
        """
        if self.rect.top > 0:  # 如果飞机没有移动出背景区域
            self.rect.top -= self.speed
        else:  # 如果即将移动出背景区域，则及时纠正为背景边缘位置
            self.rect.top = 0

    def move_down(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def move_left(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def move_right(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        # 初始化飞机
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 60)
        self.active = True