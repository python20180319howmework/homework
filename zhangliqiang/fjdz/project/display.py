'''
作者:zlq
日期:18-4-17
'''

import  pygame
import  sys
import  bullet
import plane
import enemy
import supply
from  pygame.locals import  *


from random import *

pygame.init()
pygame.mixer.init()
bg_size = width, height = 800,1000

Sdiji_num = 15
Zdiji_num = 10
Ddiji_num = 5
Bul_num = 5


def add_group(group1,group2,eny):
    group1.add(eny)
    group2.add(eny)

def add_small_enemy(group1,group2, num,bg_rect):
    for i in range(num):
        each = enemy.SmallEnemy(bg_rect)
        group1.add(each)
        group2.add(each)
def add_mid_enemy(group1,group2,num,bg_rect):
    for i in range(num):
        each = enemy.MidEnemy(bg_rect)
        group1.add(each)
        group2.add(each)
def add_big_enemy(group1,group2, num, bg_rect):
    for i in range(num):
        each = enemy.BigEnemy(bg_rect)
        group1.add(each)
        group2.add(each)
def speed_increace(group,inc):
    for e in group:
        e.speed += inc


def main():
    pygame.init()
    screen = pygame.display.set_mode((800,1000))
    pygame.display.set_caption("飞机大战")
    pygame.mixer.music.load('../sound/game_music.ogg')
    pygame.mixer.music.play(2)
    win_sound = pygame.mixer.Sound("../testsounds/winner.wav")
    win_sound.set_volume(0.7)
    bullet_sound = pygame.mixer.Sound("../sound/bullet.wav")
    bullet_sound.set_volume(0.5)
    boom_img = pygame.image.load("../images/yzd1.png").convert_alpha()
    width = boom_img.get_rect().width
    height = boom_img.get_rect().height
    bomb_sound = pygame.mixer.Sound("../sound/boom.wav")

    boom_rect = boom_img.get_rect()
    boom_rect.left, boom_rect.top = (50, 50)


    bg_img = pygame.image.load("../images/bg1.jpg").convert_alpha()
    width = bg_img.get_rect().width
    height = bg_img.get_rect().height
    myplane = plane.MyPlane(bg_img.get_rect())


    #控制图片切换速度
    delay = 0
    change_img = False

    #定义敌机组
    enemies_group = pygame.sprite.Group()
    smallEny_group = pygame.sprite.Group()

    add_small_enemy(smallEny_group,enemies_group,Sdiji_num,bg_img.get_rect())

    midEny_group = pygame.sprite.Group()

    add_mid_enemy(midEny_group,enemies_group,Zdiji_num,bg_img.get_rect())
    bigEny_group = pygame.sprite.Group()

    add_big_enemy(bigEny_group,enemies_group,Ddiji_num,bg_img.get_rect())
    #敌机索引
    small_index = 0
    mid_index = 0
    big_index =0
    me_index = 0
    bullet_index = 0
    #实例化子弹对象

    bullet_group = pygame.sprite.Group()
    bulletlist = []
    for i in range(Bul_num):
        b = bullet.Bullet(myplane.rect.midtop)
        bullet_group.add(b)
        bulletlist.append(b)

    clock = pygame.time.Clock()

    score = 0
    # font对象
    fnt = pygame.font.Font("../font/myfont.ttf", 34)

    #是否暂停游戏
    pause_nor_img = pygame.image.load("../images/pause_nor.png")
    pause_pressed_img = pygame.image.load("../images/pause_pressed.png")
    resume_nor_img = pygame.image.load("../images/resume_nor.png")
    resume_pressed_img = pygame.image.load("../images/resume_pressed.png")
    pause_img = pause_nor_img
    pause_rect = pause_img.get_rect()
    pause_rect.left,pause_rect.top = (width-pause_rect.width -5,5)
    pause_flag = False


    level = 1

    bomb_img = pygame.image.load("../images/bomb.png").convert_alpha()
    bomb_rect = bomb_img.get_rect()
    bomb_rect.left,bomb_rect.top =(5,height-bomb_rect.height-5)
    bom_num = 3
    bomb_supply = supply.Bomb_Supply(bg_size)
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 10 * 1000)
    fnt2 = pygame.font.Font("../font/myfont.ttf",48)
    gameover_font = pygame.font.Font("../font/myfont.ttf", 48)
    again_image = pygame.image.load("../images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("../images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()



    running =True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(1)
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and pause_rect.collidepoint(event.pos):
                    pause_flag = not pause_flag
            elif event.type == MOUSEMOTION:
                if pause_rect.collidepoint(event.pos):
                    if pause_flag:
                        pause_img = resume_pressed_img
                    else:
                        pause_img = pause_pressed_img
                else:
                    if pause_flag:
                        pause_img = resume_nor_img
                    else:
                        pause_img = pause_nor_img
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:



                    if bom_num:
                        bom_num -= 1
                        bomb_sound.play()
                        screen.blit(boom_img, boom_rect)

                        for e in enemies_group:

                            if e.alive and e.rect.top > 0:
                                e.alive = False







            elif event.type == SUPPLY_TIME:

                if choice([True, False]):
                    bomb_supply.reset()

        screen.fill((255,255,255))
        screen.blit(bg_img,bg_img.get_rect())
        if not pause_flag:
            if level == 1 and score > 100000:
                level = 2
                add_small_enemy(smallEny_group,enemies_group,5,bg_img.get_rect())
                add_mid_enemy(midEny_group,enemies_group,2,bg_img.get_rect())
                add_big_enemy(bigEny_group,enemies_group,1,bg_img.get_rect())
                speed_increace(smallEny_group,2)
                speed_increace(midEny_group,1)
            elif level == 2 and score > 500000:
                level = 3
                add_small_enemy(smallEny_group, enemies_group, 5, bg_img.get_rect())
                add_mid_enemy(midEny_group, enemies_group, 2, bg_img.get_rect())
                add_big_enemy(bigEny_group, enemies_group, 1, bg_img.get_rect())

                speed_increace(smallEny_group, 2)
                speed_increace(midEny_group, 1)
            elif level == 3 and score > 1000000:
                level = 4
                add_small_enemy(smallEny_group, enemies_group, 5, bg_img.get_rect())
                add_mid_enemy(midEny_group, enemies_group, 2, bg_img.get_rect())
                add_big_enemy(bigEny_group, enemies_group, 1, bg_img.get_rect())

                speed_increace(smallEny_group, 2)
                speed_increace(midEny_group, 1)

            pressedkeys = pygame.key.get_pressed()
            if pressedkeys[K_LEFT]:
                myplane.move_left()
            elif pressedkeys[K_RIGHT]:
                myplane.move_right()
            elif pressedkeys[K_UP]:
                myplane.move_up()
            elif pressedkeys[K_DOWN]:
                myplane.move_down()
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, myplane):

                    if bom_num < 30:
                        bom_num += 1
                    bomb_supply.active = False


            if not delay % 18:
                bulletlist[bullet_index].reset(myplane.rect.midtop)
                bullet_index = (bullet_index + 1) % Bul_num
            for d in bullet_group:
                if d.alive:
                    d.move()
                    screen.blit(d.image, d.rect)
                    colleny = pygame.sprite.spritecollide(d, enemies_group, False, pygame.sprite.collide_mask)
                    for e in colleny:
                        if e in smallEny_group:
                            e.energy -= 1
                            score += 1000
                            e.alive = False
                        else:
                            e.energy -= 1
                            if e.energy == 0:
                                if e in midEny_group:
                                    score += 10000
                                else:
                                    score += 5000
                                e.alive = False
                        d.alive = False
            for e in bigEny_group:
                if e.alive:
                    e.move()
                    if delay % 4 == 0:
                        screen.blit(e.image1,e.rect)
                    else:
                        screen.blit(e.image2,e.rect)
                    pygame.draw.line(screen,(0,0,0),(e.rect.left,e.rect.top-5),\
                                     (e.rect.right,e.rect.top-5),2)
                    current_egy = e.energy / enemy.BigEnemy.energy
                    if current_egy < 0.2:
                        color_paint = (255,0,0)
                    else:
                        color_paint = (0,255,0)
                    pygame.draw.line(screen,color_paint,(e.rect.left,e.rect.top-5),\
                                     (e.rect.left + e.rect.width * current_egy,e.rect.top - 5),2)
                else:
                    screen.blit(e.destroy_image[big_index],e.rect)
                    if delay % 3 == 0:
                        big_index  += 1
                        if big_index == 6:
                            big_index = 0
                            e.reset()
            for e in midEny_group:
                if e.alive:
                    e.move()
                    screen.blit(e.image,e.rect)

                    pygame.draw.line(screen, (0, 0, 0), (e.rect.left, e.rect.top - 5), \
                                     (e.rect.right, e.rect.top - 5), 2)
                    current_egy = e.energy / enemy.MidEnemy.energy
                    if current_egy < 0.2:
                        color_paint = (255, 0, 0)
                    else:
                        color_paint = (0, 255, 0)
                    pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top - 5), \
                                     (e.rect.left + e.rect.width * current_egy, e.rect.top - 5), 2)

                else:
                    screen.blit(e.destroy_image[mid_index],e.rect)
                    if delay %3 == 0:
                        mid_index  += 1
                        if mid_index == 4:
                            mid_index = 0
                            e.reset()
            for e in smallEny_group:
                if e.alive:
                    e.move()
                    screen.blit(e.image, e.rect)
                    pygame.draw.line(screen, (0, 0, 0), (e.rect.left, e.rect.top - 5), \
                                     (e.rect.right, e.rect.top - 5), 2)
                    current_egy = e.energy / enemy.SmallEnemy.energy
                    if current_egy < 0.2:
                        color_paint = (255, 0, 0)
                    else:
                        color_paint = (0, 255, 0)
                    pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top - 5), \
                                     (e.rect.left + e.rect.width * current_egy, e.rect.top - 5), 2)
                else:
                    e.reset()

        #检测敌机是否撞击我方飞机
        collide_plane = pygame.sprite.spritecollide(myplane, enemies_group, False,\
                                                pygame.sprite.collide_mask)
        if collide_plane:
            for e in collide_plane:
                e.alive = False
                myplane.alive = False
        myrender = fnt.render("Score:%d" % score, True, (234, 222, 56))

        screen.blit(myrender, (5,5))
        myrender = fnt.render("level:%d"% level,True,(234,222,56))
        screen.blit(myrender,(width-myrender.get_rect().width-5, height-myrender.get_rect().height-5))
        if bom_num > 0:
            screen.blit(bomb_img,bomb_rect)
            myrender = fnt2.render("x %d"% bom_num,True,(234,222,56))
            screen.blit(myrender,(bomb_rect.right+2,bomb_rect.top))



        if myplane.alive:
            if not change_img:
                screen.blit(myplane.image1, myplane.rect)
            else:
                screen.blit(myplane.image2, myplane.rect)
        else:
            screen.blit(myplane.destroy_images[me_index],myplane.rect)
            if not delay % 10 :
                me_index += 1
                if me_index ==4:
                    running = False

        screen.blit(pause_img,pause_rect)
        delay += 1
        if delay %5 == 0:
            change_img = True
        else:
            change_img =False



        pygame.display.update()
        clock.tick(60)
if __name__ == '__main__':
    main()