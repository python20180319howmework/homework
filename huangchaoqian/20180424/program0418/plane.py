import pygame


class Plane(pygame.sprite.Sprite):
    def __init__(self,bg_img):
        super().__init__()
        self.image1=pygame.image.load('../images/me1.png').convert_alpha()
        self.image2=pygame.image.load('../images/me2.png').convert_alpha()
        self.destroy_image=[pygame.image.load('../images/me_destroy_1.png').convert_alpha(),\
                            pygame.image.load('../images/me_destroy_2.png').convert_alpha(),\
                            pygame.image.load('../images/me_destroy_3.png').convert_alpha(),\
                            pygame.image.load('../images/me_destroy_4.png').convert_alpha()]
        self.mask=pygame.mask.from_surface(self.image1)
        self.speed=5
        self.rect=self.image1.get_rect()
        self.rect.left,self.rect.top=((bg_img.get_width()-self.rect.width)/2,\
                                      bg_img.get_height()-self.rect.height)
        self.bg_img=bg_img
        self.alive=True

    def move_up(self):
        if self.rect.top<=0:
            self.rect.top=0
        else:
            self.rect.top-=self.speed

    def move_down(self):
        if self.rect.bottom>=self.bg_img.get_height():
            self.rect.bottom=self.bg_img.get_height()
        else:
            self.rect.bottom+=self.speed

    def move_left(self):
        if self.rect.left<=0:
            self.rect.left=0
        else:
            self.rect.left-=self.speed

    def move_right(self):
        if self.rect.right>=self.bg_img.get_width():
            self.rect.right=self.bg_img.get_width()
        else:
            self.rect.right+=self.speed







