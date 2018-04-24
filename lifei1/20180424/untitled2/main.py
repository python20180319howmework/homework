import pygame
from pygame.locals import  *
import plane
import enemy
import bullet

SMALL_ENEMY_NUM = 15
MID_ENEMY_NUM = 10
BIG_ENEMY_NUM = 5
BULLET_NUM = 5
# 将敌机加入组中
def add_group(group1, group2, eny):
    group1.add(eny)
    group2.add(eny)

def main():
    # 初始化游戏
    pygame.init()
    # 游戏窗口
    screen = pygame.display.set_mode((480, 700))
    # bg图片
    bg_img = pygame.image.load("./images/timg.jpg").convert_alpha()

    # 标题
    pygame.display.set_caption("飞机大战--Bata")

    # 实例化我方飞机
    myplane = plane.MyPlane(bg_img.get_rect())
    #控制图片切换速度
    delay = 0
    change_img = False
    image3 = pygame.image.load("./images/life.png").convert_alpha()
    rect = image3.get_rect()
    num=3
    # 敌机组
    enemies_group = pygame.sprite.Group()
    # 小敌机组
    smallEny_group = pygame.sprite.Group()
    # 实例化小型机-->15个
    for i in range(SMALL_ENEMY_NUM):
        small = enemy.SmallEnemy(bg_img.get_rect())
        add_group(enemies_group, smallEny_group, small)
    # 中敌机组
    midEny_group = pygame.sprite.Group()
    for i in range(MID_ENEMY_NUM):
        small = enemy.MidEnemy(bg_img.get_rect())
        add_group(enemies_group, midEny_group, small)

    # 大敌机组
    bigEny_group = pygame.sprite.Group()
    for i in range(BIG_ENEMY_NUM):
        small = enemy.BigEnemy(bg_img.get_rect())
        add_group(enemies_group, bigEny_group, small)
    #炸弹组
    zhadan_group=pygame.sprite.Group()
    for i in range(2):
        small=enemy.Zhadan(bg_img.get_rect())
        zhadan_group.add(small)
    #火力组
    zhidan_group=pygame.sprite.Group()
    for i in range(1):
        small=enemy.Zhidan(bg_img.get_rect())
        zhidan_group.add(small)
    # 销毁索引
    mid_index = 0
    big_index = 0
    me_index = 0
    bullet_index = 0

   # print(myplane.rect.width)
    print(myplane.rect.left)
    print(myplane.rect.top)
    print(myplane.rect.midtop)

    # 实例化子弹对象
    bullet_group = pygame.sprite.Group()
    bulletlist = []
    for i in range(BULLET_NUM):
        b = bullet.Bullet(myplane.rect.left,myplane.rect.top)
        bullet_group.add(b)
        bulletlist.append(b)
    bullet_group1 = pygame.sprite.Group()
    bulletlist1=[]
    for i in range(BULLET_NUM):
        b1=bullet.Bullet1(myplane.rect.left,myplane.rect.top)
        bullet_group1.add(b1)
        bulletlist1.append(b1)
    # 设置刷新速度
    clock = pygame.time.Clock()

    # 显示分数
    score = 0
    # font对象
    fnt = pygame.font.Font('./font/myfont.ttf', 24)

    # 背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load("./sound/game_music.ogg")
    pygame.mixer.music.play(-1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(1)
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
        # 画背景图片
        screen.fill((255,255,255))
        screen.blit(bg_img, bg_img.get_rect())
        # 子弹重置
        if not delay % 10:
            bulletlist[bullet_index].reset(myplane.rect.midtop)
            bullet_index = (bullet_index + 1) % BULLET_NUM

        # 绘制子弹
        for d in bullet_group:
            if d.alive:
                d.move()
                screen.blit(d.image, (d.rect.left,d.rect.top))
                # 子弹是否与敌机发生碰撞
                colleny = pygame.sprite.spritecollide(d, enemies_group, False, pygame.sprite.collide_mask)
                for e in colleny:
                    if e in smallEny_group:
                        score += 1000
                        e.alive = False
                    else:
                        e.energy -= 1
                        if e.energy == 0:
                            if e in bigEny_group:
                                score += 10000
                            else:
                                score += 5000
                            e.alive = False
                    d.alive = False

        # 绘制敌机
        for e in bigEny_group:
            if e.alive:
                e.move()
                if delay % 4 == 0:
                    screen.blit(e.image1, e.rect)
                else:
                    screen.blit(e.image2, e.rect)
                # 绘制血槽
                pygame.draw.line(screen, (0,0,0), (e.rect.left, e.rect.top-5), \
                                 (e.rect.right, e.rect.top-5), 2)
                # 余血
                current_egy = e.energy / enemy.BigEnemy.energy
                if current_egy < 0.2:
                    color_paint = (255, 0, 0)
                else:
                    color_paint = (0, 255, 0)
                pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top - 5), \
                                 (e.rect.left + e.rect.width * current_egy, e.rect.top - 5), 2)

            else:
                screen.blit(e.destroy_image[big_index], e.rect)
                if delay % 3 == 0:
                    big_index += 1
                    if big_index == 6:
                        big_index = 0
                        e.reset()

        for e in midEny_group:
            if e.alive:
                e.move()
                screen.blit(e.image, e.rect)
                # 绘制血槽
                pygame.draw.line(screen, (0, 0, 0), (e.rect.left, e.rect.top - 5), \
                                 (e.rect.right, e.rect.top - 5), 2)
                # 余血
                current_egy = e.energy / enemy.MidEnemy.energy
                if current_egy < 0.2:
                    color_paint = (255,0,0)
                else:
                    color_paint = (0,255,0)
                pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top - 5), \
                                 (e.rect.left+e.rect.width * current_egy, e.rect.top - 5), 2)
            else:
                screen.blit(e.destroy_image[mid_index], e.rect)
                if delay % 3 == 0:
                    mid_index += 1
                    if mid_index == 4:
                        mid_index = 0
                        e.reset()
        for e in smallEny_group:
            if e.alive:
                e.move()
                screen.blit(e.image, e.rect)
            else:
                e.reset()
       # screen.blit(b1.image, b1.rect)
        #绘制炸弹
        for e in zhadan_group:
            if e.alive:
                e.move()
                screen.blit(e.image1,e.rect)
            else:
                e.reset()
        #绘制火力
        for e in zhidan_group:
            if e.alive:
                e.move()

                screen.blit(e.image1,e.rect)
            else:
                e.reset()
        #画生命
        for i in range(num):

            screen.blit(image3,(480-10-(i+1)*rect.width,\
                                        700-10-rect.height))
        # 检测敌机是否撞击我方飞机
        collide_plane = pygame.sprite.spritecollide(myplane, enemies_group, False, \
                                    pygame.sprite.collide_mask)
        if collide_plane:
            # 发生碰撞
           # myplane.live-=1
            for e in collide_plane:
                e.alive = False
                if e in smallEny_group:
                    myplane.engy-=40
                if e in midEny_group:
                    myplane.engy-=6
                if e in bigEny_group:
                    myplane.engy-=12
        if myplane.engy<=0:

            myplane.engy=120
            num-=1
        if num==0:
            myplane.alive=False
        myrender = fnt.render("Score:%d" % score, True, (234, 222, 56))
        # 显示文字
        #检测与炸弹发生碰撞
        num1=0
        collide_zhadan=pygame.sprite.spritecollide(myplane, zhadan_group, False, \
                                    pygame.sprite.collide_mask)
        if collide_zhadan:
            for e in collide_zhadan:
                e.alive=False
            for e in enemies_group:
                e.alive=False
        collide_zhidan=pygame.sprite.spritecollide(myplane, zhidan_group, False, \
                                    pygame.sprite.collide_mask)
        if collide_zhidan:
            num1=1
            for e in collide_zhidan:
                e.alive=False

                for i in bulletlist:
                    i.speed+=10

                if not delay % 10:
                    bulletlist1[bullet_index].reset(myplane.rect.midtop)
                    bullet_index = (bullet_index + 1) % BULLET_NUM

                                    # 绘制子弹
                for d in bullet_group1:
                    if d.alive:
                        d.move()
                        screen.blit(d.image, (d.rect.left,d.rect.top))
                                        # 子弹是否与敌机发生碰撞
                        colleny = pygame.sprite.spritecollide(d, enemies_group, False, pygame.sprite.collide_mask)
                        for e in colleny:
                            if e in smallEny_group:
                                score += 1000
                                e.alive = False
                            else:
                                e.energy -= 1
                                if e.energy == 0:
                                    if e in bigEny_group:
                                        score += 10000
                                    else:
                                        score += 5000
                                    e.alive = False
                                d.alive = False


        screen.blit(myrender, myrender.get_rect())
      #
        if myplane.alive:
            if not change_img:
                screen.blit(myplane.image1, myplane.rect)
            else:
                screen.blit(myplane.image2, myplane.rect)
        else:
            # 销毁
            screen.blit(myplane.destroy_images[me_index], myplane.rect)
            if not delay % 10:
                me_index += 1
                if me_index == 4:
                    running = False
        delay += 1
        if delay % 5 == 0:
            change_img = True
        else:
            change_img = False
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()