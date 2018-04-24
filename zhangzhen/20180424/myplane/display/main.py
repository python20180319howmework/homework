#作者：zhangzhen
#日期：18-4-23
#内容：
import sys
import pygame
from pygame.locals import *
from plane import OurPlane
from enemy import SmallEnemy,MidEnemy,BigEnemy
from bullet import Bullet


bg_size = 480, 700  # 初始化游戏
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("打飞机游戏")
pygame.mixer.init()  # 初始化混音

# 背景音乐
pygame.mixer.music.load("../sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)

# 子弹音乐
bullet_sound = pygame.mixer.Sound("../sound/bullet.wav")
bullet_sound.set_volume(0.8)

# 我方飞机的音乐
me_down_sound = pygame.mixer.Sound("../sound/me_down.wav")
me_down_sound.set_volume(1)

# 敌方飞机的音乐
enemy1_down_sound = pygame.mixer.Sound("../sound/enemy1_down.wav")
enemy1_down_sound.set_volume(1)

enemy2_down_sound = pygame.mixer.Sound("../sound/enemy2_down.wav")
enemy2_down_sound.set_volume(1)

enemy3_down_sound = pygame.mixer.Sound("../sound/enemy3_down.wav")
enemy3_down_sound.set_volume(1)


get_bullet_sound = pygame.mixer.Sound("../sound/get_bullet.wav")
get_bullet_sound.set_volume(1)

big_enemy_flying_sound = pygame.mixer.Sound("../sound/supply.wav")
big_enemy_flying_sound.set_volume(1)

background = pygame.image.load("../image/background.png")  # 加载背景图片,并设置为不透明

# 我方飞机
our_plane = OurPlane(bg_size)
def add_small_enemies(group1, group2, num):
    """
    添加小型敌机
    """
    for i in range(num):
        small_enemy = SmallEnemy(bg_size)
        group1.add(small_enemy)
        group2.add(small_enemy)
def add_mid_enemies(group1, group2, num):
    """
    添加中型敌机
    """
    for i in range(num):
        mid_enemy = MidEnemy(bg_size)
        group1.add(mid_enemy)
        group2.add(mid_enemy)

def add_big_enemies(group1, group2, num):
    """
    添加大型敌机
    """
    for i in range(num):
        big_enemy = BigEnemy(bg_size)
        group1.add(big_enemy)
        group2.add(big_enemy)
def add2_small_enemies(group1, group2, num,background_rect):
    """
    添加小型敌机
    """
    for i in range(num):
        each = SmallEnemy(background_rect)
        group1.add(each)
        group2.add(each)
def add2_mid_enemies(group1, group2, num,background_rect):
    """
    添加中型敌机
    """
    for i in range(num):
        each = MidEnemy(background_rect)
        group1.add(each)
        group2.add(each)
def add2_big_enemies(group1, group2, num,background_rect):
    """
    添加大型敌机
    """
    for i in range(num):
        each = BigEnemy(background_rect)
        group1.add(each)
        group2.add(each)
def speed_increace(group,inc):
    for e in group:
        e.speed += inc
def main():
    pygame.init()
    pygame.mixer.music.play(-1)  #  -1 表示无限循环
    running = True
    switch_image = False
    delay = 60

    # 生成敌方飞机组
    enemies = pygame.sprite.Group()
    # 敌方小型飞机组
    small_enemies = pygame.sprite.Group()
    # 敌方中型飞机组
    mid_enemies = pygame.sprite.Group()
    # 敌方大型飞机组
    big_enemies = pygame.sprite.Group()

    # 实例化敌方小型飞机
    add_small_enemies(small_enemies, enemies, 4)
    # 实例化敌方中型飞机
    add_mid_enemies(mid_enemies, enemies, 4)
    add_big_enemies(big_enemies, enemies, 4)

    # 定义子弹, 各种敌机和我方敌机的索引
    bullet_index = 0
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    # 定义子弹实例化个数
    bullet1 = []
    bullet_num = 15
    for i in range(bullet_num):
        bullet1.append(Bullet(our_plane.rect.midtop))
    # 绘制背景的宽度和高度
    width = background.get_rect().width
    height = background.get_rect().height

    # 显示分数
    score = 0
    # font对象
    fnt = pygame.font.Font("../font/myfont.ttf", 40)

    # 暂停播放按钮
    pause_nor_img = pygame.image.load("../image/pause_nor.png")
    pause_pressed_img = pygame.image.load("../image/pause_pressed.png")
    resume_nor_img = pygame.image.load("../image/resume_nor.png")
    resume_pressed_img = pygame.image.load("../image/resume_pressed.png")
    pause_img = pause_nor_img
    pause_rect = pause_img.get_rect()
    pause_rect.left, pause_rect.top = (width - pause_rect.width - 5, 5)
    pause_flag = False

    #设置等级
    level = 1
    # 炸弹
    bomb_img = pygame.image.load("../image/bomb.png").convert_alpha()
    bomb_rect = bomb_img.get_rect()
    bomb_rect.left, bomb_rect.top = (5, height - bomb_rect.height - 5)
    bom_num = 3
    fnt2 = pygame.font.Font("../font/myfont.ttf",40)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:  # QUIT事件，程序退出
                pygame.quit()
                sys.exit()
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

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    for e in enemies:
                        if e.active and e.rect.top >0:
                            e.active = False
                    bom_num -= 1
        # 绘制背景图
        screen.fill((255,255,255))
        screen.blit(background, (0, 0))
        #判断等级
        if level == 1 and score > 50000:
            level = 2
            # 多5个小敌机 2中敌机 1大敌机
            add2_small_enemies(small_enemies, enemies, 5,background.get_rect)
            add2_mid_enemies(mid_enemies, enemies, 2, background.get_rect())
            add2_big_enemies(big_enemies, enemies, 1, background.get_rect())
            # 小敌机速度+2 中敌机速度加1
            speed_increace(small_enemies, 2)
            speed_increace(mid_enemies, 1)
        elif level == 2 and score > 150000:
            level = 3
            # 多10个小敌机 5中敌机 2大敌机
            add2_small_enemies(small_enemies, enemies, 10, background.get_rect())
            add2_mid_enemies(mid_enemies, enemies, 5, background.get_rect())
            add2_big_enemies(big_enemies, enemies, 2, background.get_rect())
            # 小敌机速度+3 中敌机速度加2
            speed_increace(small_enemies, 3)
            speed_increace(mid_enemies, 2)
        # 喷气式的飞机就涉及到帧数
        clock = pygame.time.Clock()
        clock.tick(60)
        if delay == 0:
            delay = 60
        delay -= 1

        # 绘制我方飞机的两种不同的形式
        if not delay % 3:
            switch_image = not switch_image

        if not pause_flag:
            #绘制敌机
            for each in small_enemies:
                if each.active:
                    # 随机循环输出小飞机敌机
                    for e in small_enemies:
                        e.move()
                        screen.blit(e.image, e.rect)
                        # 绘制血槽
                        pygame.draw.line(screen, (0, 0, 0), (e.rect.left, e.rect.top - 5),(e.rect.right, e.rect.top - 5), 2)

                        # 剩余血量
                        current_egy = e.energy / SmallEnemy.energy
                        if current_egy < 0.3:
                            color_paint = (255, 0, 0)
                        else:
                            color_paint = (0, 255, 0)
                        pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top - 5),(e.rect.left + e.rect.width * current_egy, e.rect.top - 5), 2)
                else:
                    if e1_destroy_index == 0:
                        enemy1_down_sound.play()
                    screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                    e1_destroy_index = (e1_destroy_index + 1) % 4
                    if e1_destroy_index == 0:
                        each.reset()
            for each in mid_enemies:
                if each.active:
                    # 随机循环输出中飞机敌机
                    for e in mid_enemies:
                        e.move()
                        screen.blit(e.image, e.rect)
                        # 绘制血槽
                        pygame.draw.line(screen, (0, 0, 0), (e.rect.left, e.rect.top - 5),(e.rect.right, e.rect.top - 5), 2)
                        # 剩余血量
                        current_egy = e.energy / MidEnemy.energy
                        if current_egy < 0.3:
                            color_paint = (255, 0, 0)
                        else:
                            color_paint = (0, 255, 0)
                        pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top - 5),(e.rect.left + e.rect.width * current_egy, e.rect.top - 5), 2)
                else:
                    if e2_destroy_index == 0:
                        enemy2_down_sound.play()
                    screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                    e2_destroy_index = (e2_destroy_index + 1) % 4
                    if e2_destroy_index == 0:
                        each.reset()
            for each in big_enemies:
                if each.active:
                    # 随机循环输出中飞机敌机
                    for e in big_enemies:
                        big_enemy_flying_sound.play()
                        e.move()
                        if delay % 4 == 0:
                            screen.blit(e.image1, e.rect)
                        else:
                            screen.blit(e.image2, e.rect)
                        # 绘制血槽
                        pygame.draw.line(screen, (0, 0, 0), (e.rect.left, e.rect.top - 5),(e.rect.right, e.rect.top - 5), 2)
                        # 剩余血量
                        current_egy = e.energy / BigEnemy.energy
                        if current_egy < 0.3:
                            color_paint = (255, 0, 0)
                        else:
                            color_paint = (0, 255, 0)
                        pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top - 5),(e.rect.left + e.rect.width * current_egy, e.rect.top - 5), 2)
                else:
                    if e3_destroy_index == 0:
                        enemy3_down_sound.play()
                    screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                    e3_destroy_index = (e3_destroy_index + 1) % 4
                    if e3_destroy_index == 0:
                        each.reset()

            # 获得用户所有的键盘输入序列(如果用户通过键盘发出“向上”的指令,其他类似)
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[K_UP]:
                our_plane.move_up()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                our_plane.move_down()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                our_plane.move_left()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                our_plane.move_right()
            # 当我方飞机存活状态, 正常展示
            if our_plane.active:
                if switch_image:
                    screen.blit(our_plane.image_one, our_plane.rect)
                else:
                    screen.blit(our_plane.image_two, our_plane.rect)


                if not (delay % 10):  # 每十帧发射一颗移动的子弹
                    bullet_sound.play()
                    bullets = bullet1

                    bullets[bullet_index].reset(our_plane.rect.midtop)
                    bullet_index = (bullet_index + 1) % bullet_num

                for b in bullet1:
                    if b.active:
                        b.move()
                        screen.blit(b.image, b.rect)
                        enemies_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                        for e in enemies_hit:
                            if e in small_enemies:
                                score += 1000
                                e.active = False
                            else:
                                e.energy -= 1
                                if e.energy == 0:
                                    if e in mid_enemies:
                                        score += 5000
                                    else:
                                        score += 10000
                                    e.active = False
                                b.active = False


            else:
                if not (delay % 3):
                    screen.blit(our_plane.destroy_images[me_destroy_index], our_plane.rect)
                    me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        me_down_sound.play()
                        our_plane.reset()

        # 实现的碰撞
        enemies_down = pygame.sprite.spritecollide(our_plane, enemies, False, pygame.sprite.collide_mask)
        if enemies_down:
            our_plane.active = False
            for row in enemies:
                row.active = False

        if our_plane.active:
            if not switch_image:
                screen.blit(our_plane.image_one, our_plane.rect)
            else:
                screen.blit(our_plane.image_two, our_plane.rect)

        # 绘制暂停开始
        screen.blit(pause_img, pause_rect)

        # 显示分数
        myrender = fnt.render("Score:%d" % score, True, (100, 100, 100))
        screen.blit(myrender, (5,5))

        # 显示等级
        myrender = fnt.render("Level:%d" % level, True, (100, 100, 100))
        screen.blit(myrender, (width - myrender.get_rect().width - 5, height - myrender.get_rect().height - 5))

        # 显示炸弹
        if bom_num > 0:
            screen.blit(bomb_img, bomb_rect)
            myrender = fnt2.render("x %d" % bom_num, True, (255, 0, 0))
            screen.blit(myrender, (bomb_rect.right + 2, bomb_rect.top))

        # 绘制图像并输出到屏幕上面
        pygame.display.flip()

if __name__ == '__main__':

    main()
