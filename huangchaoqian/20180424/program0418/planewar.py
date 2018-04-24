import pygame
from pygame.locals import *
import plane
import bullet
import enemy_plane
import bomb_supply

def add_group(group1,group2,any):
    group1.add(any)
    group2.add(any)

def speed_increase(group,inc):
    for i in group:
        i.speed+=inc

def main():
    pygame.init()
    pygame.display.set_caption('Plane War')
    screen=pygame.display.set_mode((616,900))
    #背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('../testsounds/bg_music.ogg')
    pygame.mixer.music.play(-1)

    bg_img=pygame.image.load('../images/background.png').convert_alpha()
    gameover_img=pygame.image.load('../images/gameover.png').convert_alpha()
    gameagain_img=pygame.image.load('../images/again.png').convert_alpha()

    level=1
    score=0
    myfont=pygame.font.Font('../font/myfont.ttf',24)
    #炸弹
    bomb_img=pygame.image.load('../images/bomb.png').convert_alpha()
    bomb_rect=bomb_img.get_rect()
    bomb_rect.left,bomb_rect.top=(5,bg_img.get_height()-bomb_rect.height-5)
    bom_num=3

    b_supply=bomb_supply.BombSupply(bg_img)

    p=plane.Plane(bg_img)

    #子弹精灵组
    bulletlist=[]
    b_group=pygame.sprite.Group()
    for i in range(5):
        mybullet=bullet.Bullet(p.rect.midtop)
        b_group.add(mybullet)
        bulletlist.append(mybullet)
    #敌机精灵组
    enemy_group=pygame.sprite.Group()
    small_group=pygame.sprite.Group()
    for s in range(15):
        s=enemy_plane.Enemy('../images/enemy1.png',5,bg_img,3,1)
        add_group(enemy_group,small_group,s)
    mid_group=pygame.sprite.Group()
    for m in range(10):
        m=enemy_plane.Enemy('../images/enemy2.png',10,bg_img,2,10)
        add_group(enemy_group,mid_group,m)
    large_group=pygame.sprite.Group()
    for i in range(5):
        l=enemy_plane.Enemy('../images/enemy3_n1.png',10,bg_img,1,20)
        add_group(enemy_group,large_group,l)

    pause_nor_img=pygame.image.load('../images/pause_nor.png')
    pause_pressed_img=pygame.image.load('../images/pause_pressed.png')
    resume_nor_img=pygame.image.load('../images/resume_nor.png')
    resume_pressed_img=pygame.image.load('../images/resume_pressed.png')
    pause_img=pause_nor_img
    pause_rect=pause_img.get_rect()
    pause_rect.left,pause_rect.top=(bg_img.get_width()-pause_rect.width-5,5)
    pause_flag=False

    p_index=0
    mid_index=0
    large_index=0
    b_index=0
    clock=pygame.time.Clock()
    chang_img=True
    delay=0
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==MOUSEBUTTONDOWN:
                #点击鼠标左键,并在按钮区域
                if event.button==1 and pause_rect.collidepoint(event.pos):
                    pause_flag=not pause_flag
            elif event.type==MOUSEMOTION:
                if pause_rect.collidepoint(event.pos):
                    #暂停
                    if pause_flag:
                        pause_img=resume_pressed_img
                    else:
                        pause_img=pause_pressed_img
                else:
                    if pause_flag:
                        pause_img=resume_nor_img
                    else:
                        pause_img=pause_nor_img
            elif event.type==KEYDOWN:
                if event.key==K_SPACE:
                    if bom_num>0:
                        for e in enemy_group:
                            if e.alive and e.rect.bottom>0:
                                e.alive=False
                                if e in small_group:
                                    score+=100
                                elif e in mid_group:
                                    score+=300
                                else:
                                    score+=500
                        bom_num-=1
        pressed_keys=pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            p.move_left()
        if pressed_keys[K_RIGHT]:
            p.move_right()
        if pressed_keys[K_UP]:
            p.move_up()
        if pressed_keys[K_DOWN]:
            p.move_down()

        screen.fill((255,255,255))
        screen.blit(bg_img,bg_img.get_rect())
        #描绘暂停
        screen.blit(pause_img,pause_rect)
        #渲染字体,显示分数
        mytext=myfont.render('Score:%d' % score,True,(255,0,0),(255,255,255))
        screen.blit(mytext,mytext.get_rect())
        #显示等级
        mytext=myfont.render('Level:%d' % level,True,(0,0,255),(255,255,255))
        screen.blit(mytext,(bg_img.get_width()-mytext.get_rect().width-5,\
                            bg_img.get_height()-mytext.get_rect().height-5))
        #显示炸弹
        if bom_num>0:
            screen.blit(bomb_img,bomb_rect)
            mytext=myfont.render('X %d' % bom_num,True,(255,0,0),(255,255,255))
            screen.blit(mytext,(bomb_rect.right+2,bomb_rect.top+20))
        if not pause_flag:
            if level==1 and score>2000:
                level=2
                speed_increase(small_group,2)
                speed_increase(mid_group,1)
            elif level==2 and score>5000:
                level=3
                speed_increase(small_group,3)
                speed_increase(mid_group,2)
            #描绘炸弹补给包
            if b_supply.alive:
                b_supply.move()
                screen.blit(b_supply.image,b_supply.rect)
                blocksupply=pygame.sprite.collide_rect(b_supply,p)
                if blocksupply:
                    bom_num+=1
                    b_supply.alive=False
            else:
                b_supply.reset()
            #描绘子弹
            if delay%15==0:
                bulletlist[b_index].reset(p.rect.midtop)
                b_index=(b_index+1)%5

            for i in bulletlist:
                if i.alive:
                    i.move()
                    screen.blit(i.image,i.rect)
                    #检测子弹与敌机碰撞
                    blocklist=pygame.sprite.spritecollide(i,enemy_group,False,pygame.sprite.collide_mask)
                    for e in blocklist:
                        if e in small_group:
                            score+=100
                            e.alive=False
                        else:
                            e.energy-=1
                            if e.energy==0:
                                if e in mid_group:
                                    score+=300
                                else:
                                    score+=500
                                e.alive=False#????
                        i.alive=False
                else:
                    i.reset(p.rect.midtop)
            #描绘敌机
            for i in mid_group:
                if i.alive:
                    i.move()
                    screen.blit(i.image,i.rect)
                    pygame.draw.line(screen,(0,0,0),(i.rect.left,i.rect.top-5),\
                                     (i.rect.right,i.rect.top-5),2)
                    current_energy=i.energy/10
                    if current_energy<0.2:
                        color_paint=(255,0,0)
                    else:
                        color_paint=(0,255,0)
                    pygame.draw.line(screen,color_paint,(i.rect.left,i.rect.top-5),\
                                     (i.rect.left+i.rect.width*current_energy,i.rect.top-5),2)
                else:
                    screen.blit(i.destroy_mid_image[mid_index],i.rect)
                    if delay%3==0:
                        mid_index+=1
                        if mid_index==4:
                            mid_index=0
                            i.reset(10,5,10)

            for i in small_group:
                if i.alive:
                    i.move()
                    screen.blit(i.image,i.rect)
                else:
                    i.reset(5,0,1)

            for i in large_group:
                if i.alive:
                    i.move()
                    screen.blit(i.image,i.rect)
                    pygame.draw.line(screen,(0,0,0),(i.rect.left,i.rect.top-5),\
                                     (i.rect.right,i.rect.top-5))
                    current_energy=i.energy/20
                    if current_energy<0.2:
                        color_paint=(255,0,0)
                    else:
                        color_paint=(0,255,0)
                    pygame.draw.line(screen,color_paint,(i.rect.left,i.rect.top-5),\
                                     (i.rect.left+i.rect.width*current_energy,i.rect.top-5),2)
                else:
                    screen.blit(i.destroy_large_image[large_index],i.rect)
                    if delay%3==0:
                        large_index+=1
                        if large_index==6:
                            large_index=0
                            i.reset(15,10,20)
        #检测我方飞机与敌方飞机碰撞
        blocklist2=pygame.sprite.spritecollide(p,enemy_group,False,pygame.sprite.collide_mask)
        for i in blocklist2:
            i.alive=False
            p.alive=False

        #描绘我方飞机
        if p.alive:
            if chang_img:
                screen.blit(p.image1,p.rect)
            else:
                screen.blit(p.image2,p.rect)
        else:
            screen.blit(p.destroy_image[p_index],p.rect)
            if delay%10==0:
                p_index+=1
                if p_index==4:
                    p_index=0

            screen.blit(gameagain_img,((bg_img.get_width()-gameagain_img.get_width())/2,\
                        bg_img.get_height()/2))
            screen.blit(gameover_img,((bg_img.get_width()-gameover_img.get_width())/2,\
                        bg_img.get_height()/2+60))

        delay+=1
        if delay%5==0:
            chang_img=False
        else:
            chang_img=True

        pygame.display.update()
        clock.tick(30)
    pygame.quit()

if __name__ == '__main__':
    main()
