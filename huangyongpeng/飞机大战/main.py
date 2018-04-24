import pygame
from pygame.locals import *
import plane
import enemy
import bullet
#定义敌机函数
def add_small_enemy(group1,group2,num,bg_rect):
    for i in range(num):
        each =enemy.SmallEnemy(bg_rect)
        group1.add(each)
        group2.add(each)
def add_mid_enemy(group1,group2,num,bg_rect):
    for i in range(num):
        each = enemy.MidEnemy(bg_rect)
        group1.add(each)
        group2.add(each)
def add_big_enemy(group1,group2,num,bg_rect):
    for i in range(num):
        each = enemy.BigEnemy(bg_rect)
        group1.add(each)
        group2.add(each)
def add_bullet_supply(group1,group2,num,bg_rect):
    for i in range(num):
        each =enemy.Bullet1(bg_rect)
        group1.add(each)
        group2.add(each)
def speed_increat(group,s):
    for i in group:
        i.speed +=s
def main():
    #初始化游戏
    pygame.init()
    #游戏窗口
    screen=pygame.display.set_mode((480,700))
    pygame.display.set_caption("飞机大战")
    #bg图片
    bg_img=pygame.image.load('./images/background.png').convert_alpha()
    #结束的图片
    gg_img=pygame.image.load('./images/gameover.png').convert_alpha()
    gg_rect = gg_img.get_rect()
    #暂停/开始的图片
    pause1_img = pygame.image.load('./images/pause_nor.png').convert_alpha()
    pause2_img = pygame.image.load('./images/pause_pressed.png').convert_alpha()
    pause3_img = pygame.image.load('./images/resume_nor.png').convert_alpha()
    pause4_img = pygame.image.load('./images/resume_pressed.png').convert_alpha()
    pause_img = pause1_img
    pause_rect = pause_img.get_rect()
    pause_rect.left,pause_rect.top = ((bg_img.get_rect().width-pause_rect.width-5),5)
    pause_flag = False
    #实例自己的飞机
    myplane=plane.Myplane(bg_img.get_rect())
    #实例敌方的飞机
    group_small=pygame.sprite.Group()
    group_mid=pygame.sprite.Group()
    group_big=pygame.sprite.Group()
    group_all=pygame.sprite.Group()
    add_small_enemy(group_small,group_all,10,bg_img.get_rect())
    add_mid_enemy(group_mid,group_all,5,bg_img.get_rect())
    add_big_enemy(group_big,group_all,1,bg_img.get_rect())
    #group2_small = pygame.sprite.Group()
    group_supply = pygame.sprite.Group()
    add_bullet_supply(group_supply,group_all,5,bg_img.get_rect())
  #  for i in range(10):
  #      small = enemy.SmallEnemy(bg_img.get_rect())
  #      group_small.add(small)
   #     group_all.add(small)
   # for i in range(30):
   #     small = enemy.SmallEnemy(bg_img.get_rect())
   #     group2_small.add(small)
   #     group_all.add(small)
   # for i in range(5):
    #    mid = enemy.MidEnemy(bg_img.get_rect())
    #    group_mid.add(mid)
    #    group_all.add(mid)
   # for i in range(2):
      #  big = enemy.BigEnemy(bg_img.get_rect())
     #   group_big.add(big)
    #    group_all.add((big))
   # hh = group_small
    #实例化子弹对象
    bullet_group = pygame.sprite.Group()
    bulletlist = []
    for i in range(5):
        b = bullet.Bullet(myplane.rect.midtop)
        bullet_group.add(b)
        bulletlist.append(b)
    level = 1
    #设计炸弹
    bomb_img = pygame.image.load('./images/bomb.png').convert_alpha()
    bomb_rect = bomb_img.get_rect()
    bomb_rect.left,bomb_rect.top = (10,bg_img.get_rect().height-bomb_rect.height-20)
    bomb_num = 3
    fnt2 = pygame.font.Font('./font/myfont.ttf', 48)
    #设计补给
   # group_supply = pygame.sprite.Group()

   # for  i in range(5):
    #    each = enemy.Bullet1(bg_img.get_rect())
     #   group_supply.add(each)
     #设置索引
    big_index = 0
    small_index = 0
    mid_index = 0
    bullet_index = 0
    myplane_index = 0
    bullet_index2=0
    #定义飞机生命数
    life = 3
    #设置字体
    score = 0
    fnt = pygame.font.Font('./font/myfont.ttf',24)
    fnt3 = pygame.font.Font('./font/myfont.ttf', 48)
    #设置背景音乐
    pygame.mixer.init()
    bg_music = pygame.mixer.music.load('./testsounds/bg_music.ogg')
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)
    #音效
    win_sound = pygame.mixer.Sound('./testsounds/winner.wav')
    win_sound.set_volume(0.7)
    laugh_sound = pygame.mixer.Sound('./testsounds/laugh.wav')
    laugh_sound.set_volume(1)
    loser_sound = pygame.mixer.Sound('./testsounds/loser.wav')
    loser_sound.set_volume(1)
    #控制图片切换速度
    delay = 0
    change_img = False
    running = True
    clock=pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit(1)
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and pause_rect.collidepoint(event.pos):
                    pause_flag = not pause_flag
            elif event.type == MOUSEMOTION:
                if pause_rect.collidepoint(event.pos):
                    if pause_flag :
                        pause_img = pause4_img
                    else:
                        pause_img = pause2_img
                else:
                    if pause_flag:
                        pause_img = pause3_img
                    else:
                        pause_img = pause1_img
            elif event.type ==KEYDOWN:
                if event.key ==K_SPACE:
                    for  i in group_all:
                        if bomb_num >0:
                            if i.alive and i.rect.top >0:
                                i.alive = False

                    bomb_num -=1


        # 填充颜色
        screen.fill((255, 255, 255))
        # 显示背景图片
        screen.blit(bg_img, bg_img.get_rect())
        if not pause_flag:
            #设置等级
            if level == 1 and score >50000:
                level = 2
                add_small_enemy(group_small, group_all, 10, bg_img.get_rect())
                add_mid_enemy(group_mid, group_all, 5, bg_img.get_rect())
                add_big_enemy(group_big, group_all, 1, bg_img.get_rect())
                speed_increat(group_small,2)
                speed_increat(group_mid,1)
            elif level == 2 and score >150000:
                level =3
                add_small_enemy(group_small, group_all, 10, bg_img.get_rect())
                add_mid_enemy(group_mid, group_all, 5, bg_img.get_rect())
                add_big_enemy(group_big, group_all, 1, bg_img.get_rect())
                speed_increat(group_small,2)
                speed_increat(group_mid,1)
            #频繁按键
            pressedkeys=pygame.key.get_pressed()
            if pressedkeys[K_LEFT]:
                myplane.move_left()
            if pressedkeys[K_RIGHT]:
                myplane.move_right()
            if pressedkeys[K_UP]:
                myplane.move_on()
            if pressedkeys[K_DOWN]:
                myplane.move_down()



            #重置子弹
            if not delay % 20 :
                bulletlist[bullet_index].restart(myplane.rect.midtop)
                bullet_index=(bullet_index+1)%5
            #设置子弹的图片
            for  i in bullet_group:
                if i.alive:
                    i.move()

                    screen.blit(i.image,i.rect)
                    # 检测子弹打到敌机
                    colloy2 = pygame.sprite.spritecollide(i,group_all,False,pygame.sprite.collide_mask)
                    for b in colloy2:

                        if b in group_small:
                            score +=1000
                            b.alive = False
                        elif b in group_supply:
                            pass
                        else:
                            b.enery -=1
                            if b.enery == 0:
                                if b in group_mid:
                                    score += 5000
                                    b.alive = False
                                else:
                                    score +=10000
                                    b.alive = False

                            i.alive = False
            #显示分数的图片
            myrender=fnt.render('Score : %s'%score,True,(230,56,56))
            screen.blit(myrender,myrender.get_rect())
            myrender1 = fnt3.render('Level : %s'%level,True,(230,56,56))
            screen.blit(myrender1,(bg_img.get_rect().width-myrender1.get_rect().width-5,bg_img.get_rect().height-myrender1.get_rect().height-20))
            #显示敌方的飞机的图片
            for i in group_big:
                i.move()
                if i.alive:
                    if delay % 10 == 0:
                        screen.blit(i.image1, i.rect)
                    else:
                        screen.blit(i.image2,i.rect)
                    pygame.draw.line(screen,(0,0,0),(i.rect.left,i.rect.top-5),(i.rect.right,i.rect.top-5),2)
                    curret_eny = i.enery/enemy.BigEnemy.enery
                    if curret_eny <= 0.2:
                        curret_paint=(255,0,0)
                    else:
                        curret_paint=(0,255,0)
                    pygame.draw.line(screen,curret_paint,(i.rect.left,i.rect.top-5),(i.rect.left+i.rect.width*curret_eny,i.rect.top-5),2)
                else:
                    if delay % 4 == 0:
                        screen.blit(i.destroy_img[big_index], i.rect)
                        big_index += 1
                        if big_index == 4:
                            big_index = 0
                            i.restart()
            for i in group_mid:
                i.move()
                if i.alive:
                    screen.blit(i.image, i.rect)
                    pygame.draw.line(screen, (0, 0, 0), (i.rect.left, i.rect.top - 5), (i.rect.left+i.rect.width*curret_eny,\
                                                                                        i.rect.top - 5), 2)
                    curret_eny = i.enery / enemy.MidEnemy.enery
                    if curret_eny <= 0.2:
                        curret_paint = (255, 0, 0)
                    else:
                        curret_paint = (0, 255, 0)
                    pygame.draw.line(screen, curret_paint, (i.rect.left, i.rect.top - 5),
                                     (i.rect.left + i.rect.width * curret_eny, i.rect.top - 5), 2)
                else:
                    if delay % 4 == 0:
                        screen.blit(i.destroy_img[mid_index], i.rect)
                        mid_index += 1
                        if mid_index == 4:
                            mid_index = 0
                            i.restart()

            for i in group_small:

                if i.alive:
                    i.move()
                    screen.blit(i.image,i.rect)
                else:
                    if delay % 4 ==0:
                        screen.blit(i.destroy_img[small_index],i.rect)
                        small_index +=1
                        if small_index ==4:
                            small_index=0
                            i.restart()
            #检测敌机撞到我机
            colloy = pygame.sprite.spritecollide(myplane,group_all,False,pygame.sprite.collide_mask)
            for i in colloy:
                i.alive = False
                myplane.alive = False
                loser_sound.play()
              #  if life>0:
               #     life -=1
                #else:
                    #myplane.alive =False

            #显示补给的图片
            for i in group_supply:

                if i.alive:
                    i.move()
                    screen.blit(i.image,i.rect)
                else:
                    #if delay % 4 ==0:
                     #   screen.blit(i.destroy_img[bullet_index2],i.rect)
                      #  bullet_index2 +=1
                       # if bullet_index2 ==4:
                        #    bullet_index2=0
                    i.restart()

                    #screen.blit(i.image,i.rect)
           # colloy1 = pygame.sprite.spritecollide(myplane, group_supply, False, pygame.sprite.collide_mask)

                #else:
                 #  if delay %200==0:
                  #      screen.blit(i.image,i.rect)
                   # i.restart()

           # if  b in colloy1:
            #    b.alive = False

                #b.restart()
                   # b.restart()
                       # b.restart()


        #判断飞机的生命
        if life==0:
            gg_rect.left,gg_rect.top=(bg_img.get_rect().width*0.5,bg_img.get_rect().height)
            screen.blit(gg_img,gg_rect)

        if bomb_num >0:
            screen.blit(bomb_img,bomb_rect)

            myrender3 = fnt2.render('x%s'%bomb_num,True,(230,56,56))
            screen.blit(myrender3,(bomb_rect.right+2,bomb_rect.top))
        #显示自己飞机的图片
        if myplane.alive:
            if not change_img:
                screen.blit(myplane.image1,myplane.rect)
            else:
                screen.blit(myplane.image2,myplane.rect)
        else:
            screen.blit(myplane.destory_image[myplane_index],myplane.rect)

            if delay % 10 == 0:
                myplane_index += 1
                if myplane_index == 3:
                    print("hhhhhhh")
                    life -=1
                    myplane_index==0
                    myplane.restart(bg_img.get_rect())

        #更新图片
        delay +=1
        if delay % 5 ==0:
            change_img = True
        else:
            change_img = False
        screen.blit(pause_img,pause_rect)
        pygame.display.update()
        clock.tick(60)
if __name__ == '__main__':
    main()