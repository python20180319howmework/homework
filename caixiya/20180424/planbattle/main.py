import pygame
from pygame.locals import  *
import plane
import enemyplane
import bullet

#数量
enemyplane1_num=15
enemyplane2_num=8
enemyplane3_num=5
bullet_num=5
bomb_num=5

# 创建指定个数的小型敌机 并加入组内
def add_small_enemy(group1, group2, num, bg_rect):
    for i  in range(num):
        each = enemyplane.EnemyPlane1(bg_rect)
        group1.add(each)
        group2.add(each)

# 创建指定个数的中型敌机 并加入组内
def add_mid_enemy(group1, group2, num, bg_rect):
    for i  in range(num):
        each = enemyplane.EnemyPlane2(bg_rect)
        group1.add(each)
        group2.add(each)

# 创建指定个数的大型敌机 并加入组内
def add_big_enemy(group1, group2, num, bg_rect):
    for i  in range(num):
        each = enemyplane.EnemyPlane3(bg_rect)
        group1.add(each)
        group2.add(each)

# 改变敌机组内敌机速度
def speed_increace(group, inc):
    for e in group:
        e.speed += inc

#提供补给炸弹
def add_bomb(group,num,bg_rect):
    for i in range(num):
        each=bullet.Bomb(bg_rect)
        group.add(each)


def main():
    # 初始化游戏
    pygame.init()
    # 加载背景音乐
    pygame.mixer.music.load("./sound/game_music.ogg")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)

    # 加载音效
    win_sound = pygame.mixer.Sound("./testsounds/winner.wav")
    win_sound.set_volume(0.5)
    use_bomb_sound = pygame.mixer.Sound("./sound/use_bomb.wav")
    win_sound.set_volume(0.5)
    myplane_down_sound = pygame.mixer.Sound("./sound/me_down.wav")
    myplane_down_sound.set_volume(0.3)
    # 游戏窗口
    screen = pygame.display.set_mode((480, 700))
    pygame.display.set_caption("飞机大战")
    # bg图片
    bg_img = pygame.image.load("./images/background.png").convert_alpha()
    width = bg_img.get_rect().width
    height = bg_img.get_rect().height
    #game over
    gameover_img = pygame.image.load("./images/gameover.png").convert_alpha()

    # 实例化我方飞机
    myplane = plane.MyPlane(bg_img.get_rect())

    #我方飞机3条命
    life_image = pygame.image.load('./images/life.png')
    life_rect = life_image.get_rect()
    life_num = 3

    # 敌机组
    enemyplanegroup = pygame.sprite.Group()
    # 小敌机组
    enemyplane1_group = pygame.sprite.Group()
    # 实例化小型机-->15个
    add_small_enemy(enemyplane1_group, enemyplanegroup, enemyplane1_num, bg_img.get_rect())

    # 中敌机组
    enemyplane2_group = pygame.sprite.Group()
    add_mid_enemy(enemyplane2_group, enemyplanegroup, enemyplane2_num, bg_img.get_rect())

    # 大敌机组
    enemyplane3_group = pygame.sprite.Group()
    add_big_enemy(enemyplane3_group, enemyplanegroup, enemyplane3_num, bg_img.get_rect())

    #补给炸弹组
    bomb_group=pygame.sprite.Group()
    add_bomb(bomb_group,bomb_num,bg_img.get_rect())



    #实例化子弹
    bullet_group=pygame.sprite.Group()
    bullets=[]
    for i in range(bullet_num):
        b = bullet.Bullet((myplane.rect.centerx,myplane.rect.centery))
        bullets.append(b)
        bullet_group.add(b)

    # 销毁索引
    enemyplane1_index = 0
    enemyplane2_index = 0
    enemyplane3_index = 0
    myplane_index = 0
    bullet_index = 0

    #控制图片切换速度
    delay = 0
    change_img = False
    # 设置刷新速度
    clock = pygame.time.Clock()
    #显示分数
    score=0
    # 等级
    level = 1
    #字体
    ft=pygame.font.Font("./font/myfont.ttf",24)
    # 暂停播放按钮
    pause_nor_img = pygame.image.load("./images/pause_nor.png")
    pause_pressed_img = pygame.image.load("./images/pause_pressed.png")
    resume_nor_img = pygame.image.load("./images/resume_nor.png")
    resume_pressed_img = pygame.image.load("./images/resume_pressed.png")
    pause_img = pause_nor_img
    pause_rect = pause_img.get_rect()
    pause_rect.left, pause_rect.top = (width - pause_rect.width - 5, 5)
    pause_flag = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(1)
            elif event.type == MOUSEBUTTONDOWN:
                # 点击鼠标左键 并在按钮区域
                if event.button == 1 and pause_rect.collidepoint(event.pos):
                    pause_flag = not pause_flag
            elif event.type == MOUSEMOTION:
                if pause_rect.collidepoint(event.pos):
                    if pause_flag:
                        # 暂停
                        pause_img = resume_pressed_img
                    else:
                        pause_img = pause_pressed_img
                else:
                    if pause_flag:
                        pause_img = resume_nor_img
                    else:
                        pause_img = pause_nor_img


        # 画图片
        screen.fill((255,255,255))
        screen.blit(bg_img, bg_img.get_rect())#画背景
        if not pause_flag:
            # 判断等级
            if level == 1 and score > 50000:
                level = 2
                # 多5个小敌机 2中敌机 1大敌机
                add_small_enemy(enemyplane1_group, enemyplanegroup, 5, bg_img.get_rect())
                add_mid_enemy(enemyplane2_group, enemyplanegroup, 2, bg_img.get_rect())
                add_big_enemy(enemyplane3_group, enemyplanegroup, 1, bg_img.get_rect())
                # 小敌机速度+2 中敌机速度加1
                speed_increace(enemyplane1_group, 2)
                speed_increace(enemyplane2_group, 1)
                #补给3个炸弹
                add_bomb(bomb_group,3,bg_img.get_rect())

            elif level == 2 and score > 150000:
                level = 3
                # 多5个小敌机 2中敌机 1大敌机
                add_small_enemy(enemyplane1_group, enemyplanegroup, 10, bg_img.get_rect())
                add_mid_enemy(enemyplane2_group, enemyplanegroup, 5, bg_img.get_rect())
                add_big_enemy(enemyplane3_group, enemyplanegroup, 2, bg_img.get_rect())
                # 小敌机速度+2 中敌机速度加1
                speed_increace(enemyplane1_group, 3)
                speed_increace(enemyplane2_group, 2)
                #补给5个炸弹
                add_bomb(bomb_group,5,bg_img.get_rect())

            # 频繁按键
            pressedkeys = pygame.key.get_pressed()
            if pressedkeys[K_LEFT] or pressedkeys[K_a]:
                myplane.move_left()
            elif pressedkeys[K_RIGHT] or pressedkeys[K_d]:
                myplane.move_right()
            elif pressedkeys[K_UP] or pressedkeys[K_w]:
                myplane.move_up()
            elif pressedkeys[K_DOWN] or pressedkeys[K_s]:
                myplane.move_down()


            # 绘制炸弹                                                                              
            for i in bomb_group:
                if i.alive:
                    i.move()
                    screen.blit(i.image, i.rect)
                    #检测我方飞机和炸弹是否碰撞
                    collide_bomb = pygame.sprite.spritecollide(myplane,bomb_group, False, \
                                                                pygame.sprite.collide_mask)
                    if collide_bomb:
                        use_bomb_sound.play(maxtime=500)
                        i.alive=False
                        for e in enemyplanegroup:
                            if e.alive and e.rect.top>0:
                                e.alive=False
            # 子弹重置
            if not delay % 10:
                bullets[bullet_index].reset((myplane.rect.centerx,myplane.rect.centery))
                bullet_index = (bullet_index + 1) % bullet_num
            # 绘制子弹
            for b in bullet_group:
                if b.alive:
                    b.move()
                    if delay % 4 == 0:
                        screen.blit(b.image1, b.rect)
                    else:
                        screen.blit(b.image2,b.rect)
                    # 子弹是否与敌机发生碰撞
                    blocklist = pygame.sprite.spritecollide(b, enemyplanegroup, False, pygame.sprite.collide_mask)
                    for bl in blocklist:
                        if bl in enemyplane1_group:
                            win_sound.play(maxtime=500)
                            score+=1000
                            bl.alive=False
                        else:
                            bl.energy-=1
                            if bl.energy==0:
                                if bl in enemyplane2_group:
                                    win_sound.play(maxtime=500)
                                    score+=5000
                                else:
                                    win_sound.play(maxtime=500)
                                    score+=10000
                                bl.alive=False
                        b.alive=False


            # 绘制敌机
            for e in enemyplane3_group:
                if e.alive:
                    e.move()
                    if delay % 4 == 0:
                        screen.blit(e.image1, e.rect)
                    else:
                        screen.blit(e.image2, e.rect)
                    #绘制血槽
                    pygame.draw.line(screen,(0,0,0),(e.rect.left,e.rect.top-5),\
                                 (e.rect.right,e.rect.top-5),2)
                    #余血
                    current_egy = e.energy / enemyplane.EnemyPlane3.energy
                    if current_egy < 0.2:
                        color_paint = (255, 0, 0)
                    else:
                        color_paint = (0, 255, 0)
                    pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top - 5), \
                                     (e.rect.left + e.rect.width * current_egy, e.rect.top - 5), 2)

                else:
                    screen.blit(e.destroy_image[enemyplane3_index], e.rect)
                    if delay % 3 == 0:
                        enemyplane3_index += 1
                        if enemyplane3_index == 6:
                            enemyplane3_index = 0
                            e.reset()

            for e in enemyplane2_group:
                if e.alive:
                    e.move()
                    screen.blit(e.image, e.rect)
                    # 绘制血槽
                    pygame.draw.line(screen, (0, 0, 0), (e.rect.left, e.rect.top - 5), \
                                     (e.rect.right, e.rect.top - 5), 2)
                    # 余血
                    current_egy = e.energy / enemyplane.EnemyPlane2.energy
                    if current_egy < 0.2:
                        color_paint = (255, 0, 0)
                    else:
                        color_paint = (0, 255, 0)
                    pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top - 5), \
                                     (e.rect.left + e.rect.width * current_egy, e.rect.top - 5), 2)
                else:
                    screen.blit(e.destroy_image[enemyplane2_index], e.rect)
                    if delay % 3 == 0:
                        enemyplane2_index += 1
                        if enemyplane2_index == 4:
                            enemyplane2_index = 0
                            e.reset()
            for e in enemyplane1_group:
                if e.alive:
                    e.move()
                    screen.blit(e.image, e.rect)
                else:
                    screen.blit(e.destroy_image[enemyplane1_index], e.rect)
                    if delay % 3 == 0:
                        enemyplane1_index += 1
                        if enemyplane1_index == 4:
                            enemyplane1_index = 0
                            e.reset()
        # 检测敌机是否撞击我方飞机
        collide_plane = pygame.sprite.spritecollide(myplane, enemyplanegroup, False, \
                                                                pygame.sprite.collide_mask)
        if collide_plane:
             # 发生碰撞
            for e in collide_plane:
                if e in enemyplane1_group:
                    myplane.energy-=1
                    e.alive = False
                elif e in enemyplane2_group:
                    myplane.energy-=3
                    e.alive=False
                elif e in enemyplane3_group:
                    myplane.energy-=5
                    e.alive=False
                if myplane.energy<=0:
                    myplane.alive=False

        #显示分数
        myrender = ft.render("Score:%d" % score, True, (234, 222, 56))
        screen.blit(myrender, (5,5))
        #显示等级
        myrender2 = ft.render("Level:%d" % level, True, (234, 222, 56))
        screen.blit(myrender2, (5, 30))

        # 绘制我方飞机生命
        for i in range(life_num):
            screen.blit(life_image, (width - 10 - (i + 1) * life_rect.width, \
                                     height - 10 - life_rect.height))
        #我方飞机
        if myplane.alive:
            if not change_img:
                screen.blit(myplane.image1, myplane.rect)  # 画我方飞机
            else:
                screen.blit(myplane.image2, myplane.rect)  # 画我方飞机
            # 绘制血槽
            pygame.draw.line(screen, (0, 0, 0), (myplane.rect.left, myplane.rect.top - 5), \
                                 (myplane.rect.right, myplane.rect.top - 5), 2)
            # 余血
            current_egy = myplane.energy / plane.MyPlane.energy
            if current_egy < 0.2:
                color_paint = (255, 0, 0)
            else:
                color_paint = (0, 255, 0)
            pygame.draw.line(screen, color_paint, (myplane.rect.left, myplane.rect.top - 5), \
                                 (myplane.rect.left + myplane.rect.width * current_egy, myplane.rect.top - 5), 2)

        else:
            myplane_down_sound.play(maxtime=500)
            screen.blit(myplane.destroy_image[myplane_index], myplane.rect)
            if not delay % 10 :
                myplane_index += 1
                if myplane_index == 4:
                    life_num -= 1
                    myplane_index = 0
                    myplane.reset(bg_img.get_rect())
                    myplane.energy=50
        if life_num == 0:
            myplane_down_sound.play(maxtime=500)
            screen.blit(gameover_img,myplane.rect)
            running=False

        # 绘制暂停开始
        screen.blit(pause_img, pause_rect)

        delay += 1
        if delay % 5 == 0:
            change_img = True
        else:
            change_img = False
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()