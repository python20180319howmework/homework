import pygame
import random
class SmallEnemy(pygame.sprite.Sprite):
    enery =1
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/enemy1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width = bg_size.width
        self.height = bg_size.height
        self.destroy_img =[pygame.image.load('./images/enemy1_down1.png').convert_alpha(),\
                           pygame.image.load('./images/enemy1_down2.png').convert_alpha(),\
                           pygame.image.load('./images/enemy1_down3.png').convert_alpha(),\
                           pygame.image.load('./images/enemy1_down4.png').convert_alpha()]
        self.rect.left,self.rect.top =(random.randint(0,self.width-self.rect.width),\
                                       random.randint(-5*self.height,0))
        self.speed = 3
        self.enery=SmallEnemy.enery
        self.mask = pygame.mask.from_surface(self.image)
        self.alive = True
    def move(self):
        if self.rect.top >=self.height--self.rect.height-50:
            self.restart()
        else:
            self.rect.top +=self.speed

    def restart(self):
        self.alive = True
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-5 * self.height, 0))


class MidEnemy(pygame.sprite.Sprite):
    enery = 5
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/enemy2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width = bg_size.width
        self.height = bg_size.height
        self.destroy_img = [pygame.image.load('./images/enemy2_down1.png').convert_alpha(),\
                            pygame.image.load('./images/enemy2_down2.png').convert_alpha(),\
                            pygame.image.load('./images/enemy2_down3.png').convert_alpha(),\
                            pygame.image.load('./images/enemy2_down4.png').convert_alpha()]
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-15 * self.height, -8*self.height))
        self.speed = 2
        self.energy = MidEnemy.enery
        self.mask = pygame.mask.from_surface(self.image)
        self.alive = True

    def move(self):
        if self.rect.top >= self.height - -self.rect.height - 50:
            self.restart()
        else:
            self.rect.top += self.speed

    def restart(self):
        self.alive = True
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-15 * self.height, -8*self.height))
        self.enery = 5

class Bullet1(pygame.sprite.Sprite):
    enery=1
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/bomb_supply.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width = bg_size.width
        self.height = bg_size.height
        self.destroy_img = [pygame.image.load('./images/enemy2_down1.png').convert_alpha(), \
                            pygame.image.load('./images/enemy2_down2.png').convert_alpha(), \
                            pygame.image.load('./images/enemy2_down3.png').convert_alpha(), \
                            pygame.image.load('./images/enemy2_down4.png').convert_alpha()]
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-20 * self.height, -10*self.height))
        self.speed = 3
        self.mask = pygame.mask.from_surface(self.image)
        self.alive = True
        self.enery=Bullet1.enery
    def move(self):
        if self.rect.top >= self.height - -self.rect.height - 50:
            self.restart()
        else:
            self.rect.top += self.speed

    def restart(self):
        self.alive = True
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-20 * self.height, -10*self.height))
        self.enery=1
class BigEnemy(pygame.sprite.Sprite):
    enery = 10
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load('./images/enemy3_n1.png').convert_alpha()
        self.image2 = pygame.image.load('./images/enemy3_n2.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.width = bg_size.width
        self.height = bg_size.height
        self.destroy_img = [pygame.image.load('./images/enemy3_down1.png').convert_alpha(),\
                            pygame.image.load('./images/enemy3_down2.png').convert_alpha(),\
                            pygame.image.load('./images/enemy3_down3.png').convert_alpha(),\
                            pygame.image.load('./images/enemy3_down4.png').convert_alpha()]
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-20 * self.height, -10*self.height))
        self.speed = 1
        self.enery = BigEnemy.enery
        self.mask = pygame.mask.from_surface(self.image1)
        self.alive = True

    def move(self):
        if self.rect.top >= self.height - -self.rect.height - 50:
            self.restart()
        else:
            self.rect.top += self.speed

    def restart(self):
        self.alive = True
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-20 * self.height, -10*self.height))
        self.enery = 10