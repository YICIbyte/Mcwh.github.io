import pygame, os, sys, random, math, threading
# 安全创建任意层级文件夹
from pathlib import Path
pygame.init()
folders = ("./assets/buttonSound/",
           "./assets/fishGame/bgImg/",
           "./assets/fishGame/bgMusic/",
           "./assets/fishGame/enemyFish/",
           "./assets/fishGame/explosionImg/",
           "./assets/fishGame/skillImg/",
           "./assets/fishGame/gameImg/",
           "./assets/fishGame/iconImg/",
           "./assets/fishGame/myFish/bullet1/",
           "./assets/fishGame/myFish/bullet2/",
           "./assets/fishGame/myFish/bullet3/",
           "./assets/fishGame/myFish/img/",
           "./assets/fishGame/sound/bulletSound/",
           "./assets/fishGame/sound/eatSound/",
           "./assets/fishGame/sound/explosionSound/",
           "./assets/fishGame/sound/skillSound/",
           "./assets/greeting/bgImg/", # 祝福背景图片
           "./assets/greeting/cake/bottom/flower/",
           "./assets/greeting/cake/bottom/flowers/",
           "./assets/greeting/cake/top/star/",
           "./assets/greeting/cake/bottom/pearl/",
           "./assets/greeting/cake/center/wheat/",
           "./assets/greeting/cake/creamFlower/",
           "./assets/greeting/cake/left/",
           "./assets/greeting/cake/right/",
           "./assets/greeting/iconImg/",
           "./assets/greeting/photo/", # 合照展示
           "./assets/hall/bgImg/", # 大厅背景图
           "./assets/greeting/cake/bottom/balm/",
           "./assets/happyBirthday/icoImg/",
           "./assets/iconImg/",
           "./assets/mouseImg/",
           "./assets/font/",
           "./assets/music/iconImg/",
           "./assets/music/image/",
           "./assets/music/memory/",
           "./assets/music/music/",
           "./assets/password/imgNo/",
           "./assets/password/imgYes/",
           "./assets/password/memory/",
           "./assets/returnKey/img/",
           "./assets/greeting/music/",
           "./assets/greeting/bottomFlower/",
           "./assets/greeting/cake/fruits/",
           "./assets/car/",
           "./assets/greeting/cake/bottom/ribbon/",
           )
for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

FPS = 240
pygame.mixer.init()
def Sound_load(path):
    try:
        Sound = pygame.mixer.Sound(path + os.listdir(path)[0])
    except:
        # print("加载音乐失败")
        class music:
            def __init__(self):
                pass
            def play(self, *args, **kwargs):
                pass
            def stop(self, *args, **kwargs): # 停止播放
                pass
        Sound = music()
        # print("加载音乐失败"+path)
    return Sound
pygame.font.init()

try:
    FONT_PATH = folders[32] + os.listdir(folders[32])[0]
except:
    FONT_PATH = "C:/Windows/Fonts/simkai.ttf"
pygame.display.set_caption("黄宇涛生日小程序")
# WIDTH, HEIGHT = (1440, 900)
WIDTH, HEIGHT = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
try:
    icon = pygame.image.load(folders[30] + os.listdir(folders[30])[0])
    pygame.display.set_icon(icon)
except:
    pass
try:
    # 应用自定义光标
    pygame.mouse.set_cursor(pygame.cursors.Cursor((5, 5), pygame.transform.scale(pygame.image.load(folders[31] + os.listdir(folders[31])[0]).convert_alpha(), (30, 35))))
except:
    pass

音乐总和_number = 0
numbers = 0
音乐按钮总和 = []
load_music_name = "正在做准备工作..."
load_music_line = 0
类资源加载yn = False
#深紫色
PURPLE = (158, 95, 217)
#浅紫色
LILAC = (209, 179, 219)
#黑色
BLACK = (0, 0, 0)
#红色
RED = (255, 0, 0)
#白色
WHITE = (255, 255, 255)
#粉色
PINK = (255, 192, 203)
#黄色
YELLOW = (255, 255, 0)
#灰色
GRAY = (128, 128, 128)
# 蓝色
BLUE = (100, 128, 200)
# 紫色
VIOLET = (255, 0, 255)

# 音乐高度
音乐高度 = 60

音乐总和_name = []

def ClassThread():
    global 音乐区_class, color_music, music_panel, \
        music_control, load_music_name, load_music_line, \
        音乐总和_name, 加载画面s, 类资源加载yn, \
        clock1, clock2, clock3, unlock, button_1, \
        button_2, button_3, button_4, letter, 音乐总和_number, \
        对象总和_number, 音乐总和_number, 滑条s, \
        left_control_button, center_control_button, right_control_button, \
        password, numbers, adjust_volume, playback_mode, change_bg, \
        playback_mode_up, change_bg_up, adjust_volume_up, cake, my_fish_1, my_fish_2, my_fish_3\
        , enemy_fish_Group, enemy_fish_path_list, my_fish_Group, game_screen\
        , fish_icon_list, my_fish_name_list, game_number_list, action_game, mouse_stay_time\
        , mouse_pos_center, skill_list, skill_Group, explosion_Group, eat_muaic, button_music, bg_fish_music\
        , explosion_music, skill_music, bullet_music, choose_fish_Group, player_setting_1, player_setting_2, player_setting_3,\
        game_difficult, game_speak, game_win, game_bgimg, ballon_Group, birthday_music, flower_list, photo_greeting_Group, \
        point_move_Group, eye_1, eye_2, eye_3, eye_4

    # 创建选择鱼精灵组
    choose_fish_Group = pygame.sprite.Group()

    # 创建彩球精灵组
    point_move_Group = pygame.sprite.Group()

    try:
        game_bgimg = pygame.transform.scale(pygame.image.load(folders[6] + os.listdir(folders[6])[0]), (width, height))
    except:
        game_bgimg = pygame.Surface((width, height))
        game_bgimg.fill((135, 206, 235))

    # 游戏胜利对象
    game_win = GameWin()

    # 游戏说明对象
    game_speak = GameSpeak()

    # 游戏难度对象
    game_difficult = GameDifficult()

    button_music = Sound_load(folders[0]) # 加载按钮音效

    bg_fish_music = Sound_load(folders[2]) # 加载鱼背景音乐

    explosion_music = Sound_load(folders[14]) # 加载爆炸音效

    skill_music = Sound_load(folders[15]) # 加载技能音效

    bullet_music = Sound_load(folders[12]) # 加载子弹音效

    eat_muaic = Sound_load(folders[13]) # 加载吃鱼音效

    birthday_music = Sound_load(folders[41]) # 加载生日音乐

    音乐总和_number = 0

    mouse_pos_center = pygame.mouse.get_pos()
    mouse_stay_time = pygame.time.get_ticks()

    music_path = folders[36]
    for path in os.listdir(music_path):
        音乐总和_name.append(music_path + path)
        音乐总和_number += 1

    password = Password()

    # 眼球
    eye_1 = Eye((width * 0.4, height * 0.2))
    eye_2 = Eye((width * 0.6, height * 0.2))

    clock1 = Clock("year", width * 0.3125)

    clock2 = Clock("moon", width * 0.5)

    clock3 = Clock("day", width * 0.6875)

    unlock = Unlock()

    # 听音乐
    try:
        button_1 = Button(pygame.image.load(folders[33] + os.listdir(folders[33])[0]), width * 0.225, height * 0.75, width * 0.2, height // 6)
    except:
        button_1 = Button(pygame.Surface((200, 100)), width * 0.225, height * 0.75, width * 0.2, height // 6)
        button_1.icon.fill(YELLOW)

    # 祝福
    try:
        button_2 = Button(pygame.image.load(folders[25] + os.listdir(folders[25])[0]), width * 0.5, height * 0.65, width * 0.2, height // 6)
    except:
        button_2 = Button(pygame.Surface((200, 100)), width * 0.5, height * 0.65, width * 0.2, height // 6)
        button_2.icon.fill(YELLOW)

    # 玩游戏
    try:
        button_3 = Button(pygame.image.load(folders[7] + os.listdir(folders[7])[0]), width * 0.775, height * 0.75, width * 0.2, height // 6)
    except:
        button_3 = Button(pygame.Surface((200, 100)), width * 0.775, height * 0.75, width * 0.2, height // 6)
        button_3.icon.fill(YELLOW)

    # 信封
    try:
        button_4 = Button(pygame.image.load(folders[29] + os.listdir(folders[29])[0]), width * 0.08, 400 * bili, 150 * bili, 100 * bili)
    except:
        button_4 = Button(pygame.Surface((200, 100)), width * 0.08, 400 * bili, 150 * bili, 100 * bili)
        button_4.icon.fill(YELLOW)

    letter = Letter(width / 2, 25 * bili)

    music_panel = Music_Panel(滑条())

    music_control = Music_Control()

    left_control_button = Left_Control_Button(music_control.rect_progressBar.left + music_control.rect_button.width * 0.1, music_control.rect_button.height * 0.55, music_control.rect_button.width * 0.2, music_control.rect_button.width * 0.15)

    center_control_button = Center_Control_Button(music_control.rect_button.width / 2, music_control.rect_button.height * 0.55, music_control.rect_button.width * 0.25, music_control.rect_button.width * 0.15)

    right_control_button = Right_Control_Button(music_control.rect_progressBar.right - music_control.rect_button.width * 0.1, music_control.rect_button.height * 0.55, music_control.rect_button.width * 0.2, music_control.rect_button.width * 0.15)

    adjust_volume = AdjustVolume()

    playback_mode = PlaybackMode()

    change_bg = ChangeBg()

    playback_mode_up = PlaybackModeUP()

    change_bg_up = ChangeBgUP()

    adjust_volume_up = AdjustVolumeUP()

    cake = Cake()

    photo_greeting_Group = pygame.sprite.Group()

    if len(os.listdir(folders[26])) >= 6:
        photo_greeting_Group.add(PhotoGreeting((kuangjia.rect.width/6, kuangjia.rect.height*0.15), -20, folders[26] + os.listdir(folders[26])[0]))
        photo_greeting_Group.add(PhotoGreeting((kuangjia.rect.width/6*5, kuangjia.rect.height*0.15), 20, folders[26] + os.listdir(folders[26])[1]))
        photo_greeting_Group.add(PhotoGreeting((kuangjia.rect.width/6, kuangjia.rect.height*0.5), 20, folders[26] + os.listdir(folders[26])[2]))
        photo_greeting_Group.add(PhotoGreeting((kuangjia.rect.width/6*5, kuangjia.rect.height*0.5), -20, folders[26] + os.listdir(folders[26])[3]))
        photo_greeting_Group.add(PhotoGreeting((kuangjia.rect.width/6, kuangjia.rect.height*0.85), -20, folders[26] + os.listdir(folders[26])[4]))
        photo_greeting_Group.add(PhotoGreeting((kuangjia.rect.width/6*5, kuangjia.rect.height*0.85), 20, folders[26] + os.listdir(folders[26])[5]))

    flower_list = []
    for i in range(30):
        flower_list.append(BottomFlower(kuangjia.rect.width / 30 * i + 20*bili))

    ballon_Group = pygame.sprite.Group()

    # 游戏初始画面  游戏1
    game_screen = GameScreen()

    # 游戏模式列表  游戏1
    game_number_list = []

    name_mode_list = ["单人模式", "双人模式", "三人模式"]
    for i in range(1, len(name_mode_list)+1):
        game_number_list.append(GameNumber((width / 2, height / 5 * i + i * 45 * bili), i, name_mode_list[i-1]))
    # 开始游戏按钮  游戏2
    action_game = GameNumber((width / 2, height * 0.8), 4, "开始游戏")

    # 敌鱼组
    enemy_fish_Group = pygame.sprite.Group()

    # 敌鱼路径列表
    enemy_fish_path_list = []
    enemy_fish_path = folders[3]
    if len(os.listdir(enemy_fish_path)) > 0:
        for i in os.listdir(enemy_fish_path):
            enemy_fish_path_list.append(enemy_fish_path + i)
    else:
        enemy_fish_path_list.append("None")

    # 我鱼组
    my_fish_Group = pygame.sprite.Group()

    # 获取我鱼图标列表
    fish_icon_list = os.listdir(folders[11])

    # 我鱼名称列表
    my_fish_name_list = []

    # 加载技能列表
    skill_list = ["体重", "移速", "生命+1", "子弹时间", "填满子弹"]

    # 技能精灵组
    skill_Group = pygame.sprite.Group()

    # 爆炸精灵组
    explosion_Group = pygame.sprite.Group()

    类资源加载yn = True
    # 添加音乐按钮对象到音乐按钮总和列表中
    for i in range(len(音乐总和_name)):
        if i % 2 == 0:
            color_music = (240, 240, 240)
        else:
            color_music = (255, 255, 255)
        numbers += 1
        音乐按钮总和.append(Music_Pay_Button(音乐总和_name[i], (音乐高度 * i + 45) * bili, color_music, 音乐高度 * bili)) # 45是初始第一个音乐按钮的top坐标
        load_music_name = "加载音乐：" + 音乐总和_name[i]
        load_music_line = numbers / 音乐总和_number

class 框架:
    def __init__(self):
        global height, width, bili
        if HEIGHT * 1.6 > WIDTH:
            height = WIDTH * 0.625
            width = WIDTH
            self.image = pygame.Surface((width, width * 0.625))
        else:
            height = HEIGHT
            width = HEIGHT * 1.6
            self.image = pygame.Surface((height * 1.6, height))
        bili = height / 900
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.image.fill((0, 0, 0))
    def update(self):
        pass

kuangjia = 框架()

class 加载画面:
    def __init__(self):
        self.size = (width * 0.7, height * 0.07)
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(width / 2, height * 0.8))
        self.bg_color = (80, 255, 80)
        self.font_text = pygame.font.SysFont("kaiti", round(30* bili))
        self.font_schedule = pygame.font.SysFont("kaiti", round(40* bili))
        self.font_color = (255, 255, 255)
        self.load_color = (255, 255, 80)

        self.w = 0
        self.h = 0
        self.clock_进度条_1 = pygame.time.get_ticks()
        self.clock_加载中_1 = pygame.time.get_ticks()

        self.music_numbers = None
        self.module_image = self.font_text.render("以及组件资源", True, self.load_color)
        self.module_rect = self.module_image.get_rect(center=(width / 2, self.rect.bottom + self.rect.height * 1.7))

        self.text_load = None
        self.schedule_load = None

        self.radius = round(10 * bili)

        # 加载图片随加载而移动
        try:
            image_car_old = pygame.image.load(folders[44] + os.listdir(folders[44])[0])
            w = width / 10
            self.image_car = pygame.transform.scale(image_car_old,(w, image_car_old.get_height() * w / image_car_old.get_width()))
        except:
            self.image_car = pygame.Surface((0, 0))
        self.rect_car = self.image_car.get_rect()
        self.rect_car.bottom = self.rect.top
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if 当前关卡() == 1 and event.button == 1:
                if not button_last.is_mouse_over() and load_music_name == "加载完成":
                    button_music.play()
                    切换关卡(2)

    def update(self):
        global 类资源加载yn, load_music_name, load_music_line
        self.w = load_music_line * self.rect.width
        self.w = max(0, min(self.w, self.rect.width))
        self.h += 5
        self.h = max(0, min(self.h, self.rect.height))
        # 刷新图片随加载进度而移动
        self.rect_car.right = self.w + self.rect.x

        self.text_load = self.font_text.render(load_music_name, True, self.load_color)
        self.schedule_load = self.font_schedule.render("加载进度：" + str(int(load_music_line * 100)) + "%", True, self.font_color)
        # 最后判断是否加载完成
        if 类资源加载yn == True and 音乐总和_number == 0:
            if load_music_line < 1:
                load_music_line += 0.01
            else:
                load_music_line = 1
        if load_music_line == 1:
            load_music_name = "加载完成"
            self.music_numbers = self.font_text.render("音乐文件：" + str(音乐总和_number) + "个", True, self.load_color)
    def draw(self):
        self.image.fill((0, 0, 0, 0))
        if load_music_line == 1:
            kuangjia.image.blit(self.music_numbers, ((width - self.music_numbers.get_width()) / 2, self.rect.bottom + self.rect.height))
            kuangjia.image.blit(self.module_image, ((width - self.module_rect.width) / 2, self.rect.bottom + self.rect.height * 1.7))
        kuangjia.image.blit(self.text_load, ((width - self.text_load.get_width()) / 2, self.rect.bottom + self.rect.height * 0.4))
        kuangjia.image.blit(self.schedule_load, ((width - self.schedule_load.get_width()) / 2, self.rect.top - self.rect.height))
        pygame.draw.rect(self.image, (50, 50, 50), (0, 0, self.rect.width, self.rect.height), border_radius=self.radius)
        pygame.draw.rect(self.image, self.bg_color, (0, (self.rect.height - self.h) / 2, self.w, self.h), 0, border_radius=self.radius)
        kuangjia.image.blit(self.image_car, self.rect_car)
        kuangjia.image.blit(self.image, self.rect)

# 一开局就需要加载画面
加载画面s = 加载画面()

# 加载眼球类
class Eye:
    def __init__(self, center):
        self.size = (100*bili, 100*bili)
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = center)

        # 两种切换的颜色
        self.color_y = BLUE
        self.color_n = WHITE
        self.color = self.color_y
        # 眼睛半径
        self.radius = round(self.rect.width/4)
        self.eye_centerx = self.rect.height/2
        self.eye_centery = self.rect.height/2
        self.pos = None
    def update(self):
        self.pos = pygame.mouse.get_pos()
        # x距离
        x_distance = self.pos[0] - self.rect.centerx - kuangjia.rect.left
        # y距离
        y_distance = self.pos[1] - self.rect.centery - kuangjia.rect.top
        # 两点间的距离
        r_distance = (x_distance ** 2 + y_distance ** 2) ** 0.5
        # 如果鼠标距离眼球中心小于等于眼球半径，眼球中心就是鼠标坐标
        # 否则，眼球中心就是鼠标坐标与眼球中心的单位向量乘以眼球半径
        if r_distance < self.rect.width / 4:
            self.eye_centerx = self.rect.width / 2 + x_distance
            self.eye_centery = self.rect.height / 2 + y_distance
            # 换颜色
            self.color = self.color_y
        else:
            # 计算鼠标坐标与眼球中心的位置
            self.eye_centerx = self.rect.width / 2 + x_distance / r_distance * self.rect.width / 4
            self.eye_centery = self.rect.height / 2 + y_distance / r_distance * self.rect.width / 4
            # 换颜色
            self.color = self.color_n
    def draw(self):
        """# 眼球背景色
        self.image.fill(BLACK)"""
        # 更新眼球底色
        pygame.draw.circle(self.image, PINK, (round(self.rect.width/2), round(self.rect.height/2)), self.rect.width/2)
        # 更新眼球中心
        pygame.draw.circle(self.image, self.color, (round(self.eye_centerx), round(self.eye_centery)), self.radius)
        # 绘制眼球
        kuangjia.image.blit(self.image, self.rect)

class Clock:
    def __init__(self, types, center_x):
        self.center_x = center_x
        self.image = pygame.Surface((height // 6, height // 6))
        self.rect = self.image.get_rect()
        self.item_height = self.rect.width  # 150

        self.inplace = 0  # 当前窗口顶部的x坐标
        self.place = 0  # 鼠标坐标x
        self.last_inplace = 0  # 记录上一次窗口顶部的x坐标
        self.可滑动 = False
        self.tuple = []


        if types == "year":
            if password.password == "200668":
                self.inplace = (2006 - 1999) * self.item_height * -1
                self.last_inplace = self.inplace
            for i in range(1999, 2050):
                self.tuple.append(i)
        elif types == "moon":
            if password.password == "200668":
                self.inplace = (6 - 1) * self.item_height * -1
                self.last_inplace = self.inplace
            for i in range(1, 13):
                self.tuple.append(i)
        elif types == "day":
            if password.password == "200668":
                self.inplace = (8 - 1) * self.item_height * -1
                self.last_inplace = self.inplace
            for i in range(1, 32):
                self.tuple.append(i)

        self.font_max = round(70 * self.rect.width / 150)
        self.font_min = round(10 * self.rect.width / 150)
        self.font_color = (255, 128, 200)

        self.线条_w = self.item_height * 0.6
        self.线条_h = self.item_height / 10

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if clock1.is_mouse_over():
                    clock1.place = clock1.mouse_pos[1]
                    clock1.可滑动 = True
                elif clock2.is_mouse_over():
                    clock2.place = clock2.mouse_pos[1]
                    clock2.可滑动 = True
                elif clock3.is_mouse_over():
                    clock3.place = clock3.mouse_pos[1]
                    clock3.可滑动 = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clock1.校准精度()
                clock1.可滑动 = False
                # 滑动结束时，更新last_inplace为当前位置
                clock1.last_inplace = clock1.inplace
                clock2.校准精度()
                clock2.可滑动 = False
                clock2.last_inplace = clock2.inplace
                clock3.校准精度()
                clock3.可滑动 = False
                clock3.last_inplace = clock3.inplace
                if (clock1.return_value() == 2006 and clock2.return_value() == 6 and clock3.return_value() == 8 and unlock.is_mouse_over()):
                    try:
                        unlock.image_lock = pygame.transform.scale(pygame.image.load(folders[38] + os.listdir(folders[38])[0]), unlock.size_lock)
                    except:
                        unlock.image_lock = pygame.Surface(unlock.size_lock)
                        unlock.image_lock.fill((255, 0, 255))
                    unlock.unlock = True
                    button_music.play()
                    切换关卡(3)

    def update(self):
        self.滑动()
        self.is_mouse_over()
        self.rect.center = (self.center_x, height / 2)

    def draw(self):
        self.image.fill(BLUE)
        self.font_change()
        kuangjia.image.blit(self.image, self.rect)

    def font_change(self):
        if self.可滑动 or self.is_mouse_over():
            self.font_color = (255, 0, 0)
        else:
            self.font_color = (255, 128, 200)
        # 计算当前可见区域的数字范围
        self.visible_start = abs(self.inplace) // self.item_height
        self.visible_end = self.visible_start + 3  # 显示中心位置前后几个数字

        self.visible_end = min(self.visible_end, len(self.tuple))
        # 计算每个可见数字的位置并渲染
        for i in range(self.visible_start, self.visible_end):
            # 计算数字的中心位置（相对于显示窗口）
            self.number_center_y = (i * self.item_height) + self.item_height // 2 + self.inplace
            # 计算数字到窗口中心的距离
            self.distance_to_center = abs(self.number_center_y - self.item_height // 2)

            self.font_size = max(self.font_min, min(self.font_max - (self.distance_to_center // 2), self.font_max))
            self.font = pygame.font.SysFont("kaiti", self.font_size)
            # 渲染数字
            self.tuple_text = str(self.tuple[i])
            self.text_surface = self.font.render(self.tuple_text, True, (255, 128, 200))
            self.text_rect = self.text_surface.get_rect(center=(self.item_height // 2, self.number_center_y))
            # 绘制数字
            self.image.blit(self.text_surface, self.text_rect)
            pygame.draw.rect(self.image, self.font_color, (((self.item_height - self.线条_w) // 2,
                                                            self.number_center_y - self.item_height // 2 - self.线条_h // 2),
                                                           (self.线条_w, self.线条_h)), 0,
                             border_radius=round(self.线条_h))
        pygame.draw.rect(self.image, self.font_color, (((self.item_height - self.线条_w) // 2,
                                                        self.number_center_y + self.item_height // 2 - self.线条_h // 2),
                                                       (self.线条_w, self.线条_h)), 0, border_radius=round(self.线条_h))

    def is_mouse_over(self):
        self.mouse_pos = list(pygame.mouse.get_pos())
        self.mouse_pos[0] -= kuangjia.rect.left
        self.mouse_pos[1] -= kuangjia.rect.top
        return self.rect.collidepoint(self.mouse_pos)

    def 校准精度(self):
        if self.可滑动:
            self.inplace = round(self.inplace / self.item_height) * self.item_height

    def 滑动(self):
        if self.可滑动:
            self.new_position = self.last_inplace + self.mouse_pos[1] - self.place
            # 当前窗口顶部的x坐标
            self.inplace = max(-self.item_height * (len(self.tuple) - 1), min(self.new_position, 0))

    def return_value(self):
        return self.tuple[abs(self.inplace) // self.item_height]

    def 重置(self):
        self.inplace = 0
        self.last_inplace = 0  # 记录上一次滑动结束时的位置
        self.可滑动 = False

class Password:
    def __init__(self):
        self.mouse_pos = None
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(width * 0.2, height * 0.6))
        self.color = (255, 128, 200)
        self.password = None
        def load_password():
            try:
                with open(folders[39]+"password.dll", "r", encoding="utf-8") as f:
                    self.password = f.read().strip("\n")
                    f.close()
            except:
                self.password = "False"
        load_password()
        if self.password == "200668":
            self.yn = True
            self.inClorSRCALPHA = 255
        else:
            self.yn = False
            self.inClorSRCALPHA = 0
    def save_password(self, pwd):
        try:
            with open(folders[39]+"password.dll", "w", encoding="utf-8") as f:
                f.write(pwd)
        except:
            pass
    def is_mouse_over(self):
        self.mouse_pos = list(pygame.mouse.get_pos())
        self.mouse_pos[0] -= kuangjia.rect.left
        self.mouse_pos[1] -= kuangjia.rect.top
        return self.rect.collidepoint(self.mouse_pos)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.is_mouse_over():
            if event.button == 1:
                self.yn = not self.yn
                button_music.play()
    def update(self):
        if self.is_mouse_over():
            self.color = (255, 0, 0)
        else:
            self.color = (100, 128, 200)
    def draw(self):
        pygame.draw.circle(self.image, self.color, (self.rect.width // 2, self.rect.height // 2), self.rect.width / 2, 3)
        pygame.draw.circle(self.image, (255, 128, 200, self.inClorSRCALPHA), (self.rect.width // 2, self.rect.height // 2), self.rect.width * 0.3)
        if self.yn:
            self.inClorSRCALPHA = 255
        else:
            self.inClorSRCALPHA = 0
        kuangjia.image.blit(self.image, self.rect)

class Unlock:
    def __init__(self):
        self.size = (width * 0.2, width * 0.1)
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(width / 2, height / 1.3))
        self.color = (255, 128, 200)
        pygame.draw.rect(self.image, self.color, (0, 0, self.size[0], self.size[1]), border_radius=round(10 * bili))
        self.size_lock = (self.rect.width * 0.5, self.rect.height * 0.9)
        try:
            self.no_load_lock = pygame.transform.scale(pygame.image.load(folders[37] + os.listdir(folders[37])[0]), self.size_lock)
        except:
            self.no_load_lock = pygame.Surface(self.size_lock)
            self.no_load_lock.fill((255, 255, 255, 128))
        try:
            self.yes_load_lock = pygame.transform.scale(pygame.image.load(folders[38] + os.listdir(folders[38])[0]), self.size_lock)
        except:
            self.yes_load_lock = pygame.Surface(self.size_lock)
            self.yes_load_lock.fill((255, 255, 255, 128))
        # 设置初始状态为no_lock
        try:
            with open(folders[39]+"password.dll", "r", encoding="utf-8") as f:
                self.password = f.read().strip("\n").strip(" ")
                f.close()
                if self.password == "200668":
                    self.unlock = True
                    self.image_lock = self.yes_load_lock
                else:
                    self.unlock = False
                    self.image_lock = self.no_load_lock
        except:
            self.password = "False"
            self.unlock = False
            self.image_lock = self.no_load_lock
        self.rect_lock = self.image_lock.get_rect(center=(self.rect.width / 2, self.rect.height / 2))
    def update(self):
        if self.unlock:
            self.image_lock = self.yes_load_lock
        else:
            self.image_lock = self.no_load_lock
        if self.is_mouse_over():
            self.color = (255, 0, 0)
        else:
            self.color = BLUE

    def draw(self):
        pygame.draw.rect(self.image, self.color, ((0, 0), self.size), border_radius=round(10 * bili))
        self.image.blit(self.image_lock, self.rect_lock)
        kuangjia.image.blit(self.image, self.rect)

    def is_mouse_over(self):
        mouse_pos = list(pygame.mouse.get_pos())
        mouse_pos[0] -= kuangjia.rect.left
        mouse_pos[1] -= kuangjia.rect.top
        return self.rect.collidepoint(mouse_pos)

class Letter:
    def __init__(self, x, y):
        self.width = width * 0.4
        self.height = 0
        self.height_max = height * 0.9
        self.image = pygame.Surface((self.width, self.height))
        self.image_copy = self.image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.bg_color = YELLOW
        self.font = pygame.font.SysFont("kaiti", round(22 * bili))

        self.font_color = (80, 10, 150)
        self.font_color_change_speed = 2
        self.font_srcalpha_change_speed = 15

        self.time_lock = pygame.time.get_ticks()
        # 读取文字
        self.letters = ("祝福语寿星黄宇涛：咳咳！头一次以这样的方式给你庆生，恭喜啊，20岁生日快乐！祝你长命百岁、百毒不侵、百福不减、家财万贯。"
                        "估摸着认识有7年多了吧，平日里有大大小小的矛盾，打游戏玩的菜经常把你惹生气，话说还是很感谢你的，虽然平时老损我，"
                        "但在重要时刻还是很力挺我的，学习上对我也有很大的帮助，和你做朋友我很开心。好话坏话今天先说到这儿，剩下的槽点和"
                        "祝福留着明年生日接着唠。你喜欢音乐，也很喜欢周杰伦，所以我就给你做了一个音乐播放器，里面我放了一些他出名的歌曲保存"
                        "在里面，给你准备的独一份的生日惊喜，希望你能喜欢，现在快去许愿吧！今年所有离谱愿望全都成真。"
                        "署名：卢佳成日期：2026 年 6 月 8 日")
        self.letters = self.letters.replace(" ", "").replace("\n", "")
        # 初始化文字位置
        self.text_页边距 = 30 * bili
        self.char = self.font.size(self.letters[0])[0]
        self.text_x = (self.width - self.char) / 2 - self.char
        self.text_y = 45 * bili
        self.text_h = 40 * bili
        self.letter_rect_char = []
        for i in range(len(self.letters)):
            self.char = self.font.size(self.letters[i])[0]
            # 判断是否超过页边距
            if self.text_x > self.rect.width - self.text_页边距:
                self.text_x = self.text_页边距
                self.text_y += self.text_h

            # 存储文字位置
            self.letter_rect_char.append([self.letters[i], self.text_x, self.text_y, 0, [255, 255, 255]])
            # 设置下一个文字x的位置
            self.text_x += self.char

            # 段落换行
            if ((self.letters[i - 1] == "涛") and (self.letters[i] == "：")
                or (self.letters[i - 1] == "心") and (self.letters[i] == "。")):
                self.text_x = self.char * 2 + self.text_页边距
                self.text_y += self.text_h + (10 * bili)
            # 名字前空格
            elif (self.letters[i - 1] == "名") and (self.letters[i] == "："):
                self.text_x += self.char
            # 祝福语空格
            elif (self.letters[i - 2] == "祝") and (self.letters[i - 1] == "福") and (self.letters[i] == "语"):
                self.text_x = self.text_页边距
                self.text_y += self.text_h + (25 * bili)
            # 署名
            elif (self.letters[i - 1] == "真") and (self.letters[i] == "。"):
                self.text_x = self.width * 0.6
                self.text_y = self.height_max * 0.9
            # 日期
            elif (self.letters[i - 1] == "佳") and (self.letters[i] == "成"):
                self.text_x = self.width * 0.6
                self.text_y += self.text_h

        self.get_clock_yn = True
        self.get_clock_time = pygame.time.get_ticks()

        self.book_update_yn = False
        self.book_speed = -4 * bili

    def update(self):
        self.height += self.book_speed
        self.height = max(0, min(self.height, self.height_max))
        self.image = pygame.transform.scale(self.image_copy, (self.width, self.height))

    def draw(self):
        self.image.fill(self.bg_color)
        self.get_clock()
        kuangjia.image.blit(self.image, self.rect)

    def get_clock(self):
        if self.get_clock_yn == True:
            self.get_clock_yn = False
            self.get_clock_time = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.get_clock_time > 1200:
            self.text_color_change()

    # 重置颜色透明度
    def reset_color_alpha(self):
        # self.get_clock_yn = True
        for i in range(len(self.letter_rect_char)):
            self.letter_rect_char[i][3] = 0
            self.letter_rect_char[i][4] = [255, 255, 255]

    def text_color_change(self):
        # 遍历每个字符
        for i in range(len(self.letter_rect_char)):
            # 单个文字加载
            self.text = self.font.render(self.letter_rect_char[i][0], True, self.letter_rect_char[i][4])

            # 文字透明度变化
            if i == 0:
                self.letter_rect_char[i][3] += self.font_srcalpha_change_speed
                self.letter_rect_char[i][3] = max(0, min(self.letter_rect_char[i][3], 255))
            elif self.letter_rect_char[i - 1][3] > 30:
                self.letter_rect_char[i][3] += self.font_srcalpha_change_speed
                self.letter_rect_char[i][3] = max(0, min(self.letter_rect_char[i][3], 255))

            # 文字颜色变化
            if self.letter_rect_char[i][3] == 255:

                self.letter_rect_char[i][4][1] -= self.font_color_change_speed
                self.letter_rect_char[i][4][1] = max(self.font_color[1], min(self.letter_rect_char[i][4][1], 255))

                if self.letter_rect_char[i][4][1] == self.font_color[1]:
                    self.letter_rect_char[i][4][0] -= self.font_color_change_speed
                self.letter_rect_char[i][4][0] = max(self.font_color[0], min(self.letter_rect_char[i][4][0], 255))

                if self.letter_rect_char[i][4][0] == self.font_color[0]:
                    self.letter_rect_char[i][4][2] -= self.font_color_change_speed
                self.letter_rect_char[i][4][2] = max(self.font_color[2], min(self.letter_rect_char[i][4][2], 255))

            # 加载文字透明度
            self.text.set_alpha(self.letter_rect_char[i][3])

            # 定位文字位置
            self.text_rect = self.text.get_rect(left=self.letter_rect_char[i][1], top=self.letter_rect_char[i][2])
            # 将文字绘制到图片上
            self.image.blit(self.text, self.text_rect)
            # 文字颜色随鼠标位置变化， 并且文字透明度为255时才变化
            if self.is_mouse_over() and self.letter_rect_char[i][3] == 255:
                self.letter_rect_char[i][4][0] = 255
                self.letter_rect_char[i][4][1] = 255
                self.letter_rect_char[i][4][2] = 255
                # self.letter_rect_char[i][3] = 0

    # 判断鼠标位置是否在文字上
    def is_mouse_over(self):
        # 获取鼠标位置并改为列表形式，方便后续校准
        self.mouse_pos = list(pygame.mouse.get_pos())
        # 校准鼠标位置到文字矩形框内
        self.mouse_pos[0] -= (self.rect.left + kuangjia.rect.left)
        self.mouse_pos[1] -= (self.rect.top + kuangjia.rect.top)
        # 返回鼠标位置是否在文字上的布尔值
        return self.text_rect.collidepoint(self.mouse_pos)

    def 重置(self):
        self.reset_color_alpha()
        self.height = 0
        self.book_speed = -5 * bili
        self.book_update_yn = False

class Underline:
    def __init__(self):
        self.line_width = 0

    def is_mouse_over(self):
        self.mouse_pos = list(pygame.mouse.get_pos())
        self.mouse_pos[0] -= kuangjia.rect.left
        self.mouse_pos[1] -= kuangjia.rect.top
        return self.rect.collidepoint(self.mouse_pos)

    def under_line(self):
        if self.is_mouse_over():
            self.line_width += 8
        else:
            self.line_width -= 5
        self.line_width = max(0, min(self.line_width, self.width))

class Button(Underline, pygame.sprite.Sprite):
    def __init__(self, icon, center_x, center_y, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.icon = icon
        self.icon = pygame.transform.scale(self.icon, (self.width, self.height))
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(center_x, center_y))

        self.yn_button = False

    def handle_event_last(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and button_last.is_mouse_over() and adjust_volume_up.pulley.yn == False and music_panel.滑条s.yn == False:
                if clock1.return_value() != 2006 or clock2.return_value() != 6 or clock3.return_value() != 8:
                    unlock.unlock = False
                else:
                    unlock.unlock = True
                button_music.play()
                返回关卡()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if letter.book_update_yn == False and 当前关卡() == 3:
                    if button_1.is_mouse_over():
                        button_1.yn_button = True

                        button_music.play()
                        # 音乐暂停()
                        切换关卡(4)

                    elif button_2.is_mouse_over() and letter.book_update_yn == False:
                        button_2.yn_button = True

                        button_music.play()
                        切换关卡(5)

                    elif button_3.is_mouse_over() and letter.book_update_yn == False:
                        button_3.yn_button = True

                        button_music.play()
                        切换关卡(6)

                if button_4.is_mouse_over():

                    button_music.play()

                    letter.book_update_yn = not letter.book_update_yn
                    letter.book_speed *= -1
                    if letter.book_speed > 0:
                        letter.reset_color_alpha()

    def update(self):
        self.image.fill((0, 0, 0, 0))
        self.image.blit(self.icon, (0, 0))
        self.under_line()
        pygame.draw.rect(self.image, (255, 0, 0),
                         ((self.width - self.line_width) / 2, self.height - 10 * bili, self.line_width, 10 * bili), border_radius=4)
        kuangjia.image.blit(self.image, self.rect)

class PointMove(pygame.sprite.Sprite):
    def __init__(self, x, y, speedx, speedy):
        super().__init__()
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.size = (round(10 * bili), round(10 * bili))
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        pygame.draw.circle(self.image, self.color, (self.rect.width/2, self.rect.height/2), int(self.size[0]/2))

    def update(self):
        self.x += self.speedx
        # 如果在按钮上就停止y轴移动，并且按钮的y轴位置要大于点的y轴位置
        if not ((self.rect.colliderect(button_1.rect) and self.rect.y < button_1.rect.top)
                or (self.rect.colliderect(button_2.rect) and self.rect.y < button_2.rect.top)
                or (self.rect.colliderect(button_3.rect) and self.rect.y < button_3.rect.top)
                or (self.rect.colliderect(button_4.rect) and self.rect.y < button_4.rect.top)):
            self.y += self.speedy
        """if not ((self.rect.colliderect(button_1.rect))
                or (self.rect.colliderect(button_2.rect))
                or (self.rect.colliderect(button_3.rect))
                or (self.rect.colliderect(button_4.rect))):
            self.y += self.speedy"""
        # 自杀的4个条件
        if self.is_mouse_over() or self.x > width + self.rect.width/2 or self.x < - self.rect.width/2 or self.y > height + self.rect.height/2:
            self.kill()
        self.rect.center = (self.x, self.y)
    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= kuangjia.rect.left
        pos[1] -= kuangjia.rect.top
        return self.rect.collidepoint(pos)

# 一开局就需要加载的按钮
try:
    button_last = Button(pygame.image.load(folders[40] + os.listdir(folders[40])[0]), 80 * bili, 80 * bili, 100 * bili, 100 * bili)
except:
    button_last = Button(pygame.Surface((200, 100)), 80 * bili, 80 * bili, 100 * bili, 100 * bili)
    button_last.icon.fill(YELLOW)

class Music_Panel:
    def __init__(self, 滑条s):
        self.当前播放音乐 = None
        self.当前播放音乐名称 = None
        self.width = width * 0.74
        self.height = 860 * bili
        self.font_pay = pygame.font.SysFont("kaiti", round(30 * bili))
        self.music_action = self.font_pay.render("正在播放：", True, (0, 0, 0))

        self.音乐名字滑动 = False
        self.name = None
        self.name_x = None
        self.name_y = None
        self.name_speed_x = None
        self.name_speed_y = None
        self.name_text = None
        self.font_name = None
        self.name_target_place = None

        self.image_panel = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect_panel = self.image_panel.get_rect()
        self.rect_panel.x, self.rect_panel.y = width * 0.25, 20 * bili
        self.color_panel = (255, 255, 255, 0)

        self.image_area = pygame.Surface((self.width, self.height * 0.85), pygame.SRCALPHA)
        self.rect_area = self.image_area.get_rect()
        self.rect_area.x, self.rect_area.y = 0, 0
        self.music_number = 5

        self.image_music_container = pygame.Surface(
            (self.width, (音乐总和_number * 音乐高度 + 90 * bili)), pygame.SRCALPHA) # 90 * bili为“到底了”的空间
        self.rect_music_container = self.image_music_container.get_rect()
        self.rect_music_container.x = 0
        self.rect_music_container.y = 0
        self.color_music_container = (0, 0, 0, 0)

        self.font_到底了 = pygame.font.Font(FONT_PATH, round(30 * bili))
        self.music_end_text = self.font_到底了.render("到底了~~~", True, LILAC)
        self.rect_music_end_text = self.music_end_text.get_rect()
        try:
            self.rect_music_end_text.center = (self.rect_music_container.centerx, round((self.rect_music_container.height - 45 * bili)))
        except:
            self.rect_music_end_text.center = (self.rect_music_container.centerx, round(45 * bili))

        self.滑条s = 滑条s
        self.滑动_area_speed = 0
        self.color_area = (255, 255, 255, 0)
        self.image_pay = pygame.Surface((self.width, self.height * 0.13), pygame.SRCALPHA)
        self.rect_pay = self.image_pay.get_rect()
        self.rect_pay.x = 0
        self.rect_pay.bottom = self.rect_panel.height

        self.color_pay = (255, 255, 255, 0)

    def handle_event(self, event):
        if self.滑条s.rect.height < self.rect_area.height:
            self.滑条s.handle_event(event)
            try:
                if event.type == pygame.MOUSEBUTTONDOWN and self.is_mouse_over_area():
                    if event.button == 4:
                        self.滑条s.fill += self.滑条s.fill_speed * 10
                        self.上滑动()
                    elif event.button == 5:
                        self.下滑动()
                        self.滑条s.fill += self.滑条s.fill_speed * 10
            except:
                pass

    def 滑条移动位置(self):
        if self.滑条s.rect.height < self.rect_area.height:
            self.rect_music_container.top += self.滑动_area_speed
            self.image_area.blit(self.滑条s.image, self.滑条s.rect)
            self.滑条s.rect.top = (self.rect_music_container.y * (self.rect_area.height / self.rect_music_container.height)) * -1
            if self.滑条s.yn:
                self.rect_music_container.y = self.滑条s.container_copy_y - (pygame.mouse.get_pos()[1] - self.滑条s.posy) * (self.rect_music_container.height / self.rect_area.height)
            self.rect_music_container.top = max(self.rect_area.height - self.rect_music_container.height, min(self.rect_music_container.top, 0))
        else:
            self.rect_music_container.y = 0

    def 上滑动(self):
        self.滑动_area_speed = 50

    def 下滑动(self):
        self.滑动_area_speed = -50

    def 不滑动(self):
        self.滑动_area_speed = 0

    def 调音量(self):
        try:
            self.当前播放音乐.set_volume(adjust_volume_up.pulley.Sound / 100)
        except:
            pass

    def update(self):
        # global 音乐按钮总和
        self.滑条s.update()
        self.调音量()
        self.image_panel.fill(self.color_panel)
        self.image_area.fill(self.color_area)
        self.image_music_container.fill(self.color_music_container)
        self.image_pay.fill(self.color_pay)

        pygame.draw.rect(self.image_area, (255, 255, 255), (0, 0, self.rect_area.width, self.rect_area.height), border_radius=30)
        # 绘制音乐按钮
        for i in 音乐按钮总和:
            # 如果音乐按钮在可见范围内
            if (self.rect_music_container.top + i.rect_item.top < self.rect_area.height) and (self.rect_music_container.top + i.rect_item.bottom) > 0:
                # 音乐是否可操作
                i.update()
                self.image_music_container.blit(i.image_item, i.rect_item)

        # 绘制到底了文字
        self.image_music_container.blit(self.music_end_text, self.rect_music_end_text)

        pygame.draw.rect(self.image_pay, (255, 255, 255), (0, 0, self.rect_pay.width, self.rect_pay.height),
                         border_radius=30)

        self.image_area.blit(self.image_music_container, self.rect_music_container)

        self.滑条移动位置()
        self.image_pay.blit(self.music_action, (30 * bili, (self.rect_pay.height - self.music_action.get_height()) / 2))
        self.image_panel.blit(self.image_area, self.rect_area)
        self.image_panel.blit(self.image_pay, self.rect_pay)
        if self.音乐名字滑动:
            self.滑动名字()
        # 是否滑动？
        try:
            音乐按钮总和[0].是否正在播放()
        except:
            pass
        kuangjia.image.blit(self.image_panel, self.rect_panel)

    def is_mouse_over_area(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.relative_pos = (
            self.mouse_pos[0] - self.rect_panel.x - kuangjia.rect.left,
            self.mouse_pos[1] - self.rect_panel.y - kuangjia.rect.top
        )
        return self.rect_area.collidepoint(self.relative_pos)

    def 滑动名字(self):
        self.image_panel.blit(self.name_text, (self.name_x, self.name_y))
        self.name_x += self.name_speed_x
        if self.name_x > self.name_target_place[0]:
            self.name_x = self.name_target_place[0]
            self.name_speed_x = 0

        if self.name_y > self.name_target_place[1]:
            self.name_y -= self.name_speed_y
            self.name_y = max(self.name_target_place[1], self.name_y)
        elif self.name_y <= self.name_target_place[1]:
            self.name_y += self.name_speed_y
            self.name_y = min(self.name_y, self.name_target_place[1])

    def 获取要移动的数据(self, name, name_x, name_y, name_speed_x, name_speed_y, font_name, name_target_place,
                         name_text):
        self.name = name
        self.name_x = name_x
        self.name_y = name_y
        self.font_name = font_name
        self.name_speed_x = name_speed_x
        self.name_speed_y = name_speed_y
        self.name_text = name_text
        self.name_target_place = name_target_place
        self.音乐名字滑动 = True

    def 无法播放(self):
        self.当前播放音乐名称 = "该文件损坏或无法打开"

    def 可以播放(self):
        pass

class 滑条:
    def __init__(self):
        self.music_area_width = width * 0.74  # width * 0.74为music_area的宽度
        self.music_area_height = 860 * 0.85 * bili  # 860 * bili * 0.85为music_area的高度
        self.音乐加文字高度 = (音乐总和_number * 音乐高度 + 70 * bili + 15 * bili)  # 15 * bili为第一首歌与顶部的位置
        # self.音乐加文字高度 = 音乐按钮总和[-1].rect_item.bottom + 70 * bili
        self.width = 20 * bili
        self.height = (self.music_area_height / self.音乐加文字高度) * self.music_area_height

        # 60 * bili为单个音乐的高度
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.right = self.music_area_width - 3 * bili
        self.rect.top = 0
        self.color = PURPLE
        self.fill_max = 255
        self.fill_min = 0
        self.fill = self.fill_min
        self.fill_speed = 3

        self.yn = False

        self.posy = 0
        self.container_copy_y = 0  # 记录滑动条启用时音乐瞬时位置

    def update(self):

        self.rect.y = max(0, min(self.rect.y, music_panel.rect_area.height - self.rect.height))

        if self.is_mouse_over() or self.yn:
            self.fill += self.fill_speed
        else:
            self.fill -= self.fill_speed
        self.fill = max(self.fill_min, min(self.fill, self.fill_max))
        pygame.draw.rect(self.image, (self.color[0], self.color[1], self.color[2], self.fill),
                         (0, 0, self.width, self.height), border_radius=round(15 * bili))

    def is_mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        pos = (
            mouse_pos[0] - (music_panel.rect_panel.x + music_panel.rect_area.x + kuangjia.rect.left),
            mouse_pos[1] - (music_panel.rect_panel.y + music_panel.rect_area.y + kuangjia.rect.top)
        )
        return self.rect.collidepoint(pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_mouse_over() and event.button == 1:
                self.posy = pygame.mouse.get_pos()[1]
                self.container_copy_y = music_panel.rect_music_container.y
                self.yn = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.yn = False

class Music_Control:
    def __init__(self):
        self.width = width * 0.23
        self.height = height * 0.777
        self.corner_radius = 30

        self.image_control = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect_control = self.image_control.get_rect()
        self.rect_control = self.image_control.get_rect()
        self.rect_control.left = width * 0.01
        self.rect_control.bottom = height * 0.975

        self.image_button = pygame.Surface((self.width, self.height * 0.3754), pygame.SRCALPHA)
        self.rect_button = self.image_button.get_rect()
        self.rect_button.x = 0
        self.rect_button.y = 0

        self.image_progressBar = pygame.Surface((self.rect_button.width * 0.8187, self.rect_button.width * 0.024),
                                                pygame.SRCALPHA)
        self.rect_progressBar = self.image_progressBar.get_rect()
        self.rect_progressBar.centerx = self.rect_button.centerx
        self.rect_progressBar.top = self.rect_button.height * 0.15
        self.probar_color = PURPLE
        self.probar_font = pygame.font.SysFont("kaiti", round(10 * bili))

        self.image_bgimg = pygame.Surface((self.width, self.height * 0.6), pygame.SRCALPHA)
        self.rect_bgimg = self.image_bgimg.get_rect()
        self.bgimg_list = []
        self.img_path = folders[34]
        for path in os.listdir(self.img_path):
            try:
                self.bgimg_list.append(pygame.transform.scale(pygame.image.load(self.img_path + path), self.image_bgimg.get_size()))
            except:
                pass

        # self.type_play = "顺序播放"
        # 加载音乐壁纸
        self.load_bgimg()
        # 加载播放模式
        self.load_play_mode()
        # 2. 创建圆角遮罩（白色圆角矩形，透明背景）
        self.mask = radius_image(self.corner_radius, self.rect_bgimg)

        self.rect_bgimg.x = 0
        self.rect_bgimg.bottom = self.height

        self.seconds = 0
        self.minutes = 0
        self.sec = 0
        self.总时长 = 1
        self.image_all_text = self.probar_font.render("00:00", True, (0, 0, 0))
        self.rect_all_text = self.image_all_text.get_rect()
        self.rect_all_text.right = self.rect_progressBar.right
        self.rect_all_text.top = self.rect_progressBar.bottom * 1.13
        # 播放状态
        self.progress = 0.0  # 播放进度（0-1.0）
        self.current_time = 0.0
        self.image_current_text = self.probar_font.render(f"{self.总时长}", True, (0, 0, 0))
        self.rect_current_text = self.image_current_text.get_rect()
        self.rect_current_text.left = self.rect_progressBar.left
        self.rect_current_text.top = self.rect_progressBar.bottom + 10

        self.无异常音乐名称 = None
        self.装饰线宽 = self.rect_button.width * 0.9

    def load_bgimg(self):
        try:
            with open(folders[35]+"save_img.dll", "r", encoding="utf-8") as f:
                self.bgimg_number = int(f.read().strip("\n").strip(" "))
                if (self.bgimg_number < 0) or (self.bgimg_number >= len(self.bgimg_list)):
                    self.bgimg_number = 0
                self.bgimg = self.bgimg_list[self.bgimg_number]
                f.close()
        except:
            try:
                # 没有文档数据时读取第一张壁纸
                self.bgimg = self.bgimg_list[0]
            except:
                # 壁纸集合没有壁纸时读取空白壁纸
                self.bgimg = pygame.Surface(self.image_bgimg.get_size(), pygame.SRCALPHA)
                self.bgimg.fill((255, 255, 255))


    def save_bgimg(self, number):
        try:
            with open(folders[35]+"save_img.dll", "w", encoding="utf-8") as f:
                f.write(str(number))
        except:
            pass

    def load_play_mode(self):
        try:
            with open(folders[35]+"play_mode.dll", "r", encoding="utf-8") as f:
                self.type_play = f.read().strip("\n").strip(" ")
                if (self.type_play != "顺序播放" and self.type_play != "随机播放" and self.type_play != "循环播放"):
                    self.type_play = "随机播放"
                f.close()
        except:
            self.type_play = "顺序播放" # 没有文件就默认顺序播放模式

    def save_play_mode(self):
        try:
            with open(folders[35]+"play_mode.dll", "w", encoding="utf-8") as f:
                f.write(self.type_play)
        except:
            pass

    def update(self):
        self.update_progress()

    def draw_button(self):
        self.image_button.fill((0, 0, 0, 0))
        self.image_progressBar.fill((0, 0, 0, 0))
        self.image_current_text = self.probar_font.render(
            f"{int(self.current_time) // 60:02d}:{int(self.current_time) % 60:02d}", True, (0, 0, 0))
        pygame.draw.rect(self.image_progressBar, (230, 230, 230),
                         (0, 0, self.rect_progressBar.width, self.rect_progressBar.height), border_radius=2)
        pygame.draw.rect(self.image_progressBar, self.probar_color,
                         (0, 0, self.rect_progressBar.width * self.progress, self.rect_progressBar.height),
                         border_radius=2)
        pygame.draw.rect(self.image_button, (255, 255, 255), (0, 0, self.rect_button.width, self.rect_button.height),
                         border_radius=self.corner_radius)

        pygame.draw.rect(self.image_button, LILAC,
                         (self.rect_button.width * 0.05, self.rect_button.height * 0.38, self.装饰线宽,
                          2), border_radius=50)

        self.image_button.blit(self.image_all_text, self.rect_all_text)
        self.image_button.blit(self.image_current_text, self.rect_current_text)
        self.image_button.blit(self.image_progressBar, self.rect_progressBar)

    def set_change_bgimg(self, number):
        self.bgimg = self.bgimg_list[number]

    def get_bgimg_number(self):
        return self.bgimg_list.index(self.bgimg)

    def draw_bgimg(self):
        pygame.draw.rect(self.image_bgimg, (255, 255, 255, 255), (0, 0, self.rect_bgimg.width, self.rect_bgimg.height),
                         border_radius=self.corner_radius)
        self.image_bgimg.blit(self.bgimg, (0, 0))
        self.image_bgimg.blit(self.mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def draw_control(self):
        self.image_control.fill((0, 0, 0, 0))
        self.image_control.blit(self.image_button, self.rect_button)
        self.image_control.blit(self.image_bgimg, self.rect_bgimg)
        kuangjia.image.blit(self.image_control, self.rect_control)

    def update_progress(self):
        if center_control_button.is_playing:
            # 播放时间
            self.current_time = (pygame.time.get_ticks() - center_control_button.start_time) / 1000  # 转换为秒
            self.progress = min(self.current_time / self.总时长, 1.0)  # 防止超过100%

        # 播放结束自动重置进度条
        if self.progress >= 1.0:
            # 先提前设置为1，避免遇到无法播放的音乐导致进度分母为0
            self.总时长 = 1
            self.自动播放下一首()
            center_control_button.start_time = pygame.time.get_ticks()
            self.progress = 0.0
            self.current_time = 0.0

    def 自动播放下一首(self):
        if self.type_play == "顺序播放":
            try:
                index = self.获取当前音乐索引()
                index += 1
                if index >= len(音乐按钮总和):
                    index = 0
                音乐按钮总和[index].play(音乐按钮总和[index].music_name, 音乐按钮总和[index].music_play,
                                         音乐按钮总和[index].rect_item,
                                         音乐按钮总和[index].text_rect, 音乐按钮总和[index].font_music_name)
                self.总时长 = music_panel.当前播放音乐.get_length()
            except:
                center_control_button.无法播放()
        elif self.type_play == "随机播放":
            try:
                index = random.choice(range(len(音乐按钮总和)))
                音乐按钮总和[index].play(音乐按钮总和[index].music_name, 音乐按钮总和[index].music_play,
                                         音乐按钮总和[index].rect_item,
                                         音乐按钮总和[index].text_rect, 音乐按钮总和[index].font_music_name)
                self.总时长 = music_panel.当前播放音乐.get_length()
            except:
                center_control_button.无法播放()
        elif self.type_play == "循环播放":
            try:
                index = self.获取当前音乐索引()
                音乐按钮总和[index].play(音乐按钮总和[index].music_name, 音乐按钮总和[index].music_play,
                                         音乐按钮总和[index].rect_item,
                                         音乐按钮总和[index].text_rect, 音乐按钮总和[index].font_music_name)
                self.总时长 = music_panel.当前播放音乐.get_length()
            except:
                center_control_button.无法播放()

    def 获取当前音乐索引(self):
        for i in 音乐按钮总和:
            if i.music_name == music_panel.无异常音乐名称:
                return 音乐按钮总和.index(i)

    def set_播放模式(self, type_play):
        self.type_play = type_play

    def handle_event(self, event):
        pass

    def 可以播放(self):
        self.总时长 = music_panel.当前播放音乐.get_length()
        self.image_all_text = self.probar_font.render(self.format_time(self.总时长), True, (0, 0, 0))
        self.progress = 0.0

    def 无法播放(self):
        self.is_playing = False
        self.current_time = 0
        self.progress = 0
        self.总时长 = 1
        self.image_all_text = self.probar_font.render("00:00", True, (0, 0, 0))

    def format_time(self, seconds):
        """将秒数格式化为 分:秒（如 03:15）"""
        seconds = int(seconds)
        minutes = seconds // 60
        sec = seconds % 60
        return f"{minutes:02d}:{sec:02d}"

class Music_Pay_Button:
    def __init__(self, music_name, center_y, color, height):
        self.copy_center_y = center_y

        self.music_panel = music_panel
        self.height = height
        self.rect_area = self.music_panel.rect_area
        self.center_y = center_y
        self.image_item = pygame.Surface((music_panel.width * 0.95, self.height))
        self.rect_item = self.image_item.get_rect(center=(self.rect_area.width / 2, self.center_y))
        self.color_item = color
        self.new_color_item = color

        self.music_name = music_name.split("/")[-1]
        try:
            self.music_play = pygame.mixer.Sound(music_name)
        except:
            self.music_play = None

        self.text_color = BLACK
        self.font_music_name = pygame.font.SysFont("kaiti", round(30 * bili))
        self.text = self.font_music_name.render("".join(self.music_name.split(".")[0:-1]), True, self.text_color)
        self.text_rect = self.text.get_rect(centery=30 * bili)
        self.text_rect.x = 20 * bili
        self.font_黄宇涛 = pygame.font.Font(FONT_PATH, round(30 * bili))
        self.image_黄宇涛 = self.font_黄宇涛.render("黄宇涛", True, WHITE)
        self.rect_黄宇涛 = self.image_黄宇涛.get_rect(
            center=(self.rect_item.right - 100 * bili, self.rect_item.height / 2))

        self.fill_speed = 3 * bili
        self.rect_copy_y = self.rect_item.y

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.is_mouse_over_item() and adjust_volume_up.pulley.yn == False and music_panel.is_mouse_over_area() and music_panel.滑条s.yn == False:
                self.play(self.music_name, self.music_play, self.rect_item, self.text_rect, self.font_music_name)

    def play(self, music_name, music_play, rect_item, text_rect, font_music_name):
        if music_panel.当前播放音乐 != None:
            music_panel.当前播放音乐.stop()
        try:
            music_panel.当前播放音乐 = music_play
            music_panel.当前播放音乐名称 = music_name
            music_panel.可以播放()
            music_control.可以播放()
            center_control_button.可以播放()
        except:
            center_control_button.无法播放()
            music_panel.无法播放()
            music_control.无法播放()
        music_panel.无异常音乐名称 = music_name
        if music_panel.当前播放音乐名称 != "该文件损坏或无法打开":
            name = "".join(music_panel.当前播放音乐名称.split(".")[0:-1])
        else:
            name = music_panel.当前播放音乐名称
        # 要滑动音乐的参数
        name_x = rect_item.x + music_panel.rect_area.x + text_rect.x + music_panel.rect_music_container.x
        name_y = rect_item.y + music_panel.rect_area.y + text_rect.y + music_panel.rect_music_container.y
        font_name = font_music_name
        name_text = font_name.render(name, True, (0, 0, 0))
        name_target_place = (music_panel.rect_pay.x + music_panel.music_action.get_rect().right + 30 * bili,
                             music_panel.rect_pay.y + (music_panel.rect_pay.height - name_text.get_height()) / 2)

        x差 = abs(name_target_place[0] - name_x)
        y差 = abs(name_target_place[1] - name_y)
        两点间距离 = math.sqrt(x差 ** 2 + y差 ** 2)

        name_speed_x = x差 / 两点间距离 * 25 * bili
        name_speed_y = y差 / 两点间距离 * 25 * bili

        music_panel.获取要移动的数据(name, name_x, name_y, name_speed_x, name_speed_y, font_name,
                                     name_target_place, name_text)

    def update(self):
        self.image_item.fill(self.new_color_item)
        if self.is_mouse_over_item() and self.music_panel.is_mouse_over_area():
            self.text_color = WHITE
            self.rect_item.centerx -= self.fill_speed
            self.new_color_item = (220, 220, 220)
            self.image_item.blit(self.image_黄宇涛, self.rect_黄宇涛)
            pygame.draw.rect(self.image_item, PURPLE, (5 * bili, 5 * bili, 5 * bili, self.rect_item.height - 10 * bili),
                             border_radius=round(5 * bili))
        else:
            self.rect_item.centerx += 3 * bili
            self.new_color_item = self.color_item
            self.text_color = BLACK
        self.是否正在播放()
        self.text = self.font_music_name.render("".join(self.music_name.split(".")[0:-1]), True, self.text_color)
        self.rect_item.centerx = max(self.rect_area.width / 2 - 20 * bili, min(self.rect_item.centerx, self.rect_area.width / 2))
        self.image_item.blit(self.text, self.text_rect)

    # 检查鼠标是否悬停在按钮上
    def is_mouse_over_item(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.relative_pos = (
            self.mouse_pos[0] - (
                        self.music_panel.rect_panel.x + self.music_panel.rect_area.x + self.music_panel.rect_music_container.x + kuangjia.rect.left),
            self.mouse_pos[1] - (
                        self.music_panel.rect_panel.y + self.music_panel.rect_area.y + self.music_panel.rect_music_container.y + kuangjia.rect.top)
        )
        return self.rect_item.collidepoint(self.relative_pos)

    def 是否正在播放(self):
        # 检查当前播放音乐名称是否与按钮音乐名称相同
        if self.music_name == music_panel.当前播放音乐名称:
            self.text_color = WHITE
            # 播放音乐时，绘制矩形标记
            self.new_color_item = LILAC
            pygame.draw.rect(self.image_item, PURPLE, (5 * bili, 5 * bili, 5 * bili, self.rect_item.height - 10 * bili),
                             border_radius=round(5 * bili))

class Left_Control_Button:
    def __init__(self, center_x, center_y, width, height):
        self.width = width
        self.height = height
        self.center_x = center_x
        self.center_y = center_y
        self.fill = 80
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.center_x, self.center_y))
        # 深紫色
        self.color = PURPLE
        # 暂停图案三个点的坐标
        self.line_width = round(9 * bili)
    def handle_event(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.上一首()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.is_mouse_over() and music_panel.滑条s.yn == False and adjust_volume_up.pulley.yn == False:
                self.上一首()

    def 上一首(self):
        if (music_control.type_play == "顺序播放") or (music_control.type_play == "循环播放"):
            self.获取当前音乐索引()
            try:
                index = self.获取当前音乐索引()
                index -= 1
                if index < 0:
                    index = len(音乐按钮总和) - 1
                音乐按钮总和[index].play(音乐按钮总和[index].music_name, 音乐按钮总和[index].music_play,
                                         音乐按钮总和[index].rect_item,
                                         音乐按钮总和[index].text_rect, 音乐按钮总和[index].font_music_name)
                music_control.总时长 = music_panel.当前播放音乐.get_length()
            except:
                center_control_button.无法播放()
        elif music_control.type_play == "随机播放":
            try:
                index = random.choice(range(len(音乐按钮总和)))
                音乐按钮总和[index].play(音乐按钮总和[index].music_name, 音乐按钮总和[index].music_play,
                                         音乐按钮总和[index].rect_item,
                                         音乐按钮总和[index].text_rect, 音乐按钮总和[index].font_music_name)
                music_control.总时长 = music_panel.当前播放音乐.get_length()
            except:
                center_control_button.无法播放()

    def 获取当前音乐索引(self):
        for i in 音乐按钮总和:
            if i.music_name == music_panel.无异常音乐名称:
                return 音乐按钮总和.index(i)

    def update(self):
        if self.is_mouse_over():
            self.fill += 3
        else:
            self.fill -= 3
        self.fill = max(80, min(self.fill, 255))
        pygame.draw.rect(self.image, (LILAC[0], LILAC[1], LILAC[2], self.fill), (0, 0, self.width, self.height), border_radius=30)

        pygame.draw.rect(self.image, self.color, (26 * bili, 19 * bili, 10 * bili, self.rect.height - 38 * bili), border_radius=round(4 * bili))
        pygame.draw.rect(self.image, self.color, ((26 + 4) * bili, 17 * bili, 10 * bili, self.rect.height - 34 * bili), border_radius=round(4 * bili))
        pygame.draw.rect(self.image, self.color, ((26 + 4 + 4) * bili, 15 * bili, 10 * bili, self.rect.height - 30 * bili), border_radius=round(4 * bili))
        pygame.draw.rect(self.image, self.color, ((26 + 4 + 4 + 4) * bili, 13 * bili, 10 * bili, self.rect.height - 26 * bili), border_radius=round(4 * bili))

        pygame.draw.line(self.image, self.color, (30 * bili, 22 * bili), ((31 + 4 + 4 + 4) * bili, 16 * bili), width=self.line_width)
        pygame.draw.line(self.image, self.color, (30 * bili, 25 * bili), ((31 + 4 + 4 + 4) * bili, 32 * bili), width=self.line_width)

        #小竖杠
        pygame.draw.rect(self.image, self.color, (18 * bili, 14 * bili, 4 * bili, self.rect.height - 28 * bili), border_radius=round(2 * bili))

        music_control.image_button.blit(self.image, self.rect)

    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + music_control.rect_control.left - music_control.rect_button.left)
        pos[1] -= (kuangjia.rect.top + music_control.rect_control.top - music_control.rect_button.top)
        return self.rect.collidepoint(pos)

class Center_Control_Button:
    def __init__(self, center_x, center_y, width, height):
        self.width = width
        self.height = height
        self.center_x = center_x
        self.center_y = center_y

        self.fill = 80
        # 深紫色
        self.color = PURPLE

        self.font = pygame.font.SysFont("kaiti", 14)

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.center_x, self.center_y))

        # 播放状态
        self.is_playing = False
        self.start_time = 0  # 播放开始时间（毫秒）
        self.paused_time = 0  # 暂停时已播放的时间（毫秒）
        self.current_music = None

        # 暂停图案三个点的坐标
        self.line_width = round(5 * bili)

        self.fill_speed = round(8 * bili)
        self.fill_max = 255
        self.fill_min = 80
    def play(self):
        """播放或继续播放音乐"""
        # 首次播放
        if self.paused_time == 0:
            # 没有音乐时，播放第一首
            try:
                音乐按钮总和[0].play(音乐按钮总和[0].music_name, 音乐按钮总和[0].music_play, 音乐按钮总和[0].rect_item,
                                     音乐按钮总和[0].text_rect, 音乐按钮总和[0].font_music_name)
            except:
                pass
        # 恢复播放
        elif self.current_music is not None:
            self.current_music.unpause()
            self.start_time = pygame.time.get_ticks() - self.paused_time
            self.is_playing = True

    def pause(self):
        """暂停播放"""
        try:
            self.current_music.pause()
            self.paused_time = pygame.time.get_ticks() - self.start_time
            self.is_playing = False
        except:
            pass

    def update(self):
        if self.is_mouse_over():
            self.fill += self.fill_speed
        else:
            self.fill -= self.fill_speed
        self.fill = max(self.fill_min, min(self.fill, self.fill_max))
        pygame.draw.rect(self.image, (LILAC[0], LILAC[1], LILAC[2], self.fill), (0, 0, self.width, self.height), border_radius=30)
        if self.is_playing:
            pygame.draw.rect(self.image, self.color, (28*bili, 10*bili, 10*bili, self.rect.height - 20*bili), border_radius=round(2*bili))
            pygame.draw.rect(self.image, self.color, (self.rect.width-38*bili, 10*bili, 10*bili, self.rect.height - 20*bili), border_radius=round(2*bili))
        else:
            pygame.draw.rect(self.image, self.color, (28*bili, 10*bili, 10*bili, self.rect.height - 20*bili), border_radius=round(4*bili))
            pygame.draw.rect(self.image, self.color, ((28 + 6)*bili, 13*bili, 10*bili, self.rect.height - 26*bili), border_radius=round(4*bili))
            pygame.draw.rect(self.image, self.color, ((28 + 6 + 6)*bili, 16*bili, 10*bili, self.rect.height - 32*bili), border_radius=round(4*bili))
            pygame.draw.rect(self.image, self.color, ((28 + 6 + 6 + 6)*bili, 19*bili, 10*bili, self.rect.height - 38*bili), border_radius=round(4*bili))

            pygame.draw.line(self.image, self.color, (32*bili, 11*bili), ((33 + 6 + 6 + 6)*bili, 20*bili), width=self.line_width)
            pygame.draw.line(self.image, self.color, (32*bili, 37*bili), ((33 + 6 + 6 + 6)*bili, 27*bili), width=self.line_width)
        music_control.image_button.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                # 点击播放/暂停按钮
                if self.is_mouse_over() and adjust_volume_up.pulley.yn == False and music_panel.滑条s.yn == False:
                    self.开始与暂停()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.开始与暂停()
    def 开始与暂停(self):
        if self.is_playing:
            self.pause()
        else:
            self.play()

    def 无法播放(self):
        self.is_playing = False
        self.paused_time = 0

    def 可以播放(self):
        self.start_time = pygame.time.get_ticks()
        self.paused_time = 0
        self.current_music = music_panel.当前播放音乐.play(1, fade_ms=500)
        self.is_playing = True

    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + music_control.rect_control.left + music_control.rect_button.left)
        pos[1] -= (kuangjia.rect.top + music_control.rect_control.top + music_control.rect_button.top)
        return self.rect.collidepoint(pos)

class Right_Control_Button:
    def __init__(self, center_x, center_y, width, height):
        self.width = width
        self.height = height
        self.center_x = center_x
        self.center_y = center_y
        self.fill = 80
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.center_x, self.center_y))
        # 深紫色
        self.color = PURPLE
        # 暂停图案三个点的坐标
        self.line_width = round(9 * bili)
    def handle_event(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.下一首()
        elif event.type == pygame.MOUSEBUTTONUP and music_panel.滑条s.yn == False and adjust_volume_up.pulley.yn == False:
            if event.button == 1:
                if self.is_mouse_over():
                    self.下一首()

    def update(self):
        if self.is_mouse_over():
            self.fill += 3
        else:
            self.fill -= 3
        self.fill = max(80, min(self.fill, 255))
        pygame.draw.rect(self.image, (LILAC[0], LILAC[1], LILAC[2], self.fill), (0, 0, self.width, self.height), border_radius=30)

        pygame.draw.rect(self.image, self.color, (self.rect.width - (10 * bili) - (26 * bili), 19 * bili, 10 * bili, self.rect.height - 38 * bili), border_radius=round(4 * bili))
        pygame.draw.rect(self.image, self.color, (self.rect.width - (10 * bili) - ((26 + 4) * bili), 17 * bili, 10 * bili, self.rect.height - 34 * bili), border_radius=round(4 * bili))
        pygame.draw.rect(self.image, self.color, (self.rect.width - (10 * bili) - ((26 + 4 + 4) * bili), 15 * bili, 10 * bili, self.rect.height - 30 * bili), border_radius=round(4 * bili))
        pygame.draw.rect(self.image, self.color, (self.rect.width - (10 * bili) - ((26 + 4 + 4 + 4) * bili), 13 * bili, 10 * bili, self.rect.height - 26 * bili), border_radius=round(4 * bili))

        pygame.draw.line(self.image, self.color, (self.rect.width - (30 * bili), 22 * bili), (self.rect.width - ((31 + 4 + 4 + 4) * bili), 16 * bili), width=self.line_width)
        pygame.draw.line(self.image, self.color, (self.rect.width - (30 * bili), 25 * bili), (self.rect.width - ((31 + 4 + 4 + 4) * bili), 32 * bili), width=self.line_width)

        pygame.draw.rect(self.image, self.color, (self.rect.width - (4 * bili) - (18 * bili), 14 * bili, 4 * bili, self.rect.height - 28 * bili), border_radius=round(2 * bili))

        music_control.image_button.blit(self.image, self.rect)

    def 下一首(self):
        if (music_control.type_play == "顺序播放") or (music_control.type_play == "循环播放"):
            try:
                index = self.获取当前音乐索引()
                index += 1
                if index >= len(音乐按钮总和):
                    index = 0
                音乐按钮总和[index].play(音乐按钮总和[index].music_name, 音乐按钮总和[index].music_play,
                                         音乐按钮总和[index].rect_item,
                                         音乐按钮总和[index].text_rect, 音乐按钮总和[index].font_music_name)
                music_control.总时长 = music_panel.当前播放音乐.get_length()
            except:
                center_control_button.无法播放()
        elif music_control.type_play == "随机播放":
            try:
                index = random.choice(range(len(音乐按钮总和)))
                音乐按钮总和[index].play(音乐按钮总和[index].music_name, 音乐按钮总和[index].music_play,
                                         音乐按钮总和[index].rect_item,
                                         音乐按钮总和[index].text_rect, 音乐按钮总和[index].font_music_name)
                music_control.总时长 = music_panel.当前播放音乐.get_length()
            except:
                center_control_button.无法播放()

    def 获取当前音乐索引(self):
        for i in 音乐按钮总和:
            if i.music_name == music_panel.无异常音乐名称:
                return 音乐按钮总和.index(i)

    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + music_control.rect_control.left + music_control.rect_button.left)
        pos[1] -= (kuangjia.rect.top + music_control.rect_control.top + music_control.rect_button.top)
        return self.rect.collidepoint(pos)

class SuperMode:
    def __init__(self, centerx, text):
        self.image = pygame.Surface((50 * bili, 30 * bili), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = music_control.rect_button.height * 0.95

        # self.image_底色 = pygame.Surface((50 * bili, 30 * bili), pygame.SRCALPHA)

        self.fill = 80
        self.fill_speed = 8
        # 深紫色
        self.color = PURPLE
        self.font = pygame.font.SysFont("kaiti", round(15*bili))
        self.text = self.font.render(text, True, self.color)
        self.text_rect = self.text.get_rect(center=(self.rect.width/2, self.rect.height/2))

    def update(self):
        if self.is_mouse_over():
            self.fill += self.fill_speed
        else:
            self.fill -= self.fill_speed
        self.fill = max(50, min(self.fill, 255))

        pygame.draw.rect(music_control.image_button, (255, 0, 0, 0), (self.rect.topleft, (self.rect.width, self.rect.height)), border_radius=30)
        pygame.draw.rect(self.image, (LILAC[0], LILAC[1], LILAC[2], self.fill), (0, 0, self.rect.width, self.rect.height), border_radius=30)
        self.image.blit(self.text, self.text_rect)
        music_control.image_button.blit(self.image, self.rect)
    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + music_control.rect_control.left + music_control.rect_button.left)
        pos[1] -= (kuangjia.rect.top + music_control.rect_control.top + music_control.rect_button.top)
        return self.rect.collidepoint(pos)

class PlaybackMode(SuperMode):
    def __init__(self):
        super().__init__(music_control.rect_progressBar.left + music_control.rect_button.width * 0.1, "模式")
    def update(self):
        super().update()
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.is_mouse_over() and adjust_volume_up.pulley.yn == False:
                    playback_mode_up.yn = not playback_mode_up.yn
                    playback_mode_up.change_speed()
                elif not playback_mode_up.is_mouse_over():
                    playback_mode_up.yn = False
                    playback_mode_up.change_speed_False()

class ChangeBg(SuperMode):
    def __init__(self):
        super().__init__(music_control.rect_progressBar.centerx, "壁纸")
    def update(self):
        super().update()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.is_mouse_over() and adjust_volume_up.pulley.yn == False:
                    change_bg_up.yn = not change_bg_up.yn
                    change_bg_up.change_speed()
                elif not change_bg_up.is_mouse_over():
                    change_bg_up.yn = False
                    change_bg_up.change_speed_False()

class AdjustVolume(SuperMode):
    def __init__(self):
        super().__init__(music_control.rect_progressBar.right - music_control.rect_button.width * 0.1, "音量")
    def update(self):
        super().update()
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.is_mouse_over() and adjust_volume_up.pulley.yn == False:
                    adjust_volume_up.yn = not adjust_volume_up.yn
                    adjust_volume_up.change_speed()
                elif not adjust_volume_up.is_mouse_over() and adjust_volume_up.pulley.yn == False:
                    adjust_volume_up.yn = False
                    adjust_volume_up.change_speed_False()

class SuperModeUP:
    def __init__(self, centerx):
        self.width = 0
        self.height = 0
        self.speed = round(35 * bili)
        self.super_size_centery_起始 = change_bg.rect.centery
        self.super_size_centery_目标 = music_control.rect_button.height * 0.74

        self.super_size_centerx_起始 = centerx + (20 * bili)
        self.super_size_centerx_目标 = music_control.rect_button.width / 2

        if self.super_size_centerx_起始 < self.super_size_centerx_目标:
            self.zf = -1
            self.super_max_centerx = self.super_size_centerx_目标
            self.super_min_centerx = self.super_size_centerx_起始

        else:
            self.zf = 1
            self.super_max_centerx = self.super_size_centerx_起始
            self.super_min_centerx = self.super_size_centerx_目标

        self.super_max_width = music_control.装饰线宽
        self.super_max_height = change_bg.rect.height
        self.super_image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.super_image_copy = self.super_image.copy()
        self.super_rect = self.super_image.get_rect(center=(self.super_size_centerx_起始, self.super_size_centery_起始))
        self.yn = False
        self.fill_min = 150
        self.fill_max = 255
        self.fill_speed = round(6 * bili)
        self.fill = self.fill_min

        self.w_h_long = (self.super_max_width ** 2 + self.super_max_height ** 2) ** 0.5
        self.w_long = abs(self.super_max_width)
        self.h_long = abs(self.super_max_height)
        self.super_speedw = (self.w_long / self.w_h_long) * -1 * self.speed
        self.super_speedh = (self.h_long / self.w_h_long) * -1 * self.speed

        self.super_max_centery = self.super_size_centery_起始
        self.super_min_centery = self.super_size_centery_目标
        self.x_y_long = ((self.super_max_centerx - self.super_min_centerx) ** 2 + (self.super_max_centery - self.super_min_centery) ** 2) ** 0.5
        self.x_long = abs(self.super_size_centerx_目标 - self.super_size_centerx_起始)
        # 防止为零错误
        if self.x_long == 0:
            self.x_long = 0.01
        self.y_long = abs(self.super_size_centery_目标 - self.super_size_centery_起始)
        self.super_speedx = (self.x_long / self.x_y_long) * self.zf * self.speed
        self.super_speedy = (self.y_long / self.x_y_long) * self.speed

        # 同步时间
        self.super_speedx *= abs(self.super_speedw * (self.super_max_centerx - self.super_min_centerx)) / abs(self.super_speedx * self.super_max_width)
        self.super_speedy *= abs(self.super_speedh * (self.super_max_centery - self.super_min_centery)) / abs(self.super_speedy * self.super_max_height)

        # 深紫色
        self.color = PURPLE

        self.copy_super_rect_centerx = self.super_rect.centerx
        self.copy_super_rect_centery = self.super_rect.centery
        self.copy_super_rect_width = self.super_rect.width
        self.copy_super_rect_height = self.super_rect.height

    def update(self):
        self.copy_super_rect_width += self.super_speedw
        self.copy_super_rect_height += self.super_speedh
        self.copy_super_rect_width = max(0, min(self.copy_super_rect_width, self.super_max_width))
        self.copy_super_rect_height = max(0, min(self.copy_super_rect_height, self.super_max_height))
        if self.copy_super_rect_width > 0:
            if self.yn == True:
                if self.is_mouse_over():
                    self.fill += self.fill_speed
                else:
                    self.fill -= self.fill_speed
            self.fill = max(self.fill_min, min(self.fill, self.fill_max))
            self.change_place()
            pygame.draw.rect(self.super_image, (LILAC[0], LILAC[1], LILAC[2], self.fill), (0, 0, self.super_rect.width, self.super_rect.height), border_radius=round(8*bili))
        else:
            # 宽度隐藏时，填充为0
            self.fill = 0
    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + music_control.rect_control.left + music_control.rect_button.left)
        pos[1] -= (kuangjia.rect.top + music_control.rect_control.top + music_control.rect_button.top)
        return self.super_rect.collidepoint(pos)

    def change_place(self):
        self.super_image = pygame.transform.scale(self.super_image_copy, (self.super_rect.width, self.super_rect.height))
        self.copy_super_rect_centerx += self.super_speedx
        self.copy_super_rect_centery += self.super_speedy
        self.copy_super_rect_centerx = max(self.super_min_centerx, min(self.copy_super_rect_centerx, self.super_max_centerx))
        self.copy_super_rect_centery = max(self.super_min_centery, min(self.copy_super_rect_centery, self.super_max_centery))
        self.super_rect.centerx = self.copy_super_rect_centerx
        self.super_rect.centery = self.copy_super_rect_centery

        self.super_rect.width = self.copy_super_rect_width
        self.super_rect.height = self.copy_super_rect_height

    def change_speed_False(self):
        self.super_speedx = (self.x_long / self.x_y_long) * self.zf * self.speed
        self.super_speedy = (self.y_long / self.x_y_long) * self.speed
        # 同步时间
        self.super_speedx *= abs(self.super_speedw * abs(self.super_max_centerx - self.super_min_centerx)) / abs(self.super_speedx * self.super_max_width)
        self.super_speedy *= abs(self.super_speedh * abs(self.super_max_centery - self.super_min_centery)) / abs(self.super_speedy * self.super_max_height)
        self.super_speedw = (self.w_long / self.w_h_long) * -1 * self.speed
        self.super_speedh = (self.h_long / self.w_h_long) * -1 * self.speed
    def change_speed(self):
        self.super_speedx *= -1
        self.super_speedy *= -1
        self.super_speedw *= -1
        self.super_speedh *= -1

class PlaybackModeUP(SuperModeUP):
    def __init__(self):
        super().__init__(playback_mode.rect.centerx)
        self.循环 = 循环播放()
        self.顺序 = 顺序播放()
        self.随机 = 随机播放()
    def update(self):
        super().update()
        if self.super_rect.width > 0:
            self.循环.update()
            self.顺序.update()
            self.随机.update()
            music_control.image_button.blit(self.super_image, self.super_rect)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.循环.is_mouse_over():
                    music_control.set_播放模式("循环播放")
                    self.循环.font_color = RED
                    self.顺序.font_color = BLACK
                    self.随机.font_color = BLACK
                elif self.顺序.is_mouse_over():
                    music_control.set_播放模式("顺序播放")
                    self.顺序.font_color = RED
                    self.循环.font_color = BLACK
                    self.随机.font_color = BLACK
                elif self.随机.is_mouse_over():
                    music_control.set_播放模式("随机播放")
                    self.随机.font_color = RED
                    self.循环.font_color = BLACK
                    self.顺序.font_color = BLACK

class ChangeBgUP(SuperModeUP):
    def __init__(self):
        super().__init__(change_bg.rect.centerx)
        self.image_list = []
        self.path_list = []
        self.img_path = folders[34]
        for path in os.listdir(self.img_path):
            self.path_list.append(self.img_path + path)
        self.number = len(self.path_list)
        if self.number > 0:
            for i in range(self.number):
                # 防止加载不是图片而报错
                try:
                    self.image_list.append(BgImageSum((i + 1), pygame.image.load(self.path_list[i])))
                except:
                    self.image_list.append(BgImageSum((i + 1), pygame.Surface((100, 100))))
    def update(self):
        super().update()
        if self.super_rect.width > 0:
            for i in self.image_list:
                i.update()
        music_control.image_button.blit(self.super_image, self.super_rect)
    def handle_event(self, event):
        for i in self.image_list:
            i.handle_event(event)

class AdjustVolumeUP(SuperModeUP):
    def __init__(self):
        super().__init__(adjust_volume.rect.centerx)
        self.pulley = AdjustVolumePulley()
    def update(self):
        super().update()
        if self.super_rect.width > 0:
            self.pulley.update()
            music_control.image_button.blit(self.super_image, self.super_rect)
    def handle_event(self, event):
        self.pulley.handle_event(event)

class BgImageSum:
    def __init__(self, number, bgimg):
        self.img = bgimg
        self.number = number
        self.size = (0, 0)
        self.bgimg = pygame.transform.scale(self.img, self.size)
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.image_copy = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.top = 0
        self.radius = round(8*bili)
        self.mask = radius_image(self.radius, self.rect)
        self.fill = 0
        self.fill_speed = 15*bili
    def update(self):
        self.持续变化大小()
        if self.is_mouse_over() and change_bg_up.is_mouse_over():
            self.fill += self.fill_speed
        else:
            self.fill -= self.fill_speed
        self.fill = max(100, min(self.fill, 255))
        self.image.set_alpha(self.fill)
        self.image.blit(self.bgimg, (0, 0))
        self.image.blit(self.mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        change_bg_up.super_image.blit(self.image, self.rect)
    def 持续变化大小(self):
        if change_bg_up.number >= 12:
            self.size = (change_bg_up.super_rect.width / change_bg_up.number * 0.9, change_bg_up.super_rect.height)
        else:
            self.size = (change_bg_up.super_rect.width / 12, change_bg_up.super_rect.height)
        self.bgimg = pygame.transform.scale(self.img, self.size)
        self.image = pygame.transform.scale(self.image_copy, self.size)
        self.rect = self.image.get_rect()
        self.rect.centerx = (change_bg_up.super_rect.width / change_bg_up.number) * (self.number - 0.5)
        self.rect.top = 0
        self.mask = radius_image(self.radius, self.rect)
    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + music_control.rect_control.left + music_control.rect_button.left + change_bg_up.super_rect.left)
        pos[1] -= (kuangjia.rect.top + music_control.rect_control.top + music_control.rect_button.top + change_bg_up.super_rect.top)
        return self.rect.collidepoint(pos)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.is_mouse_over() and change_bg_up.is_mouse_over():
                music_control.set_change_bgimg(self.number - 1)

class AdjustVolumePulley:
    def __init__(self):
        self.width, self.height = 0, 0
        self.center = 0, 0
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image_copy = self.image.copy()
        self.rect = self.image.get_rect(center=self.center)

        self.image_pulley = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image_pulley_copy = self.image_pulley.copy()
        self.rect_pulley = self.image_pulley.get_rect()

        self.fill = 0
        self.fill_speed = 15*bili

        self.radius = round(8*bili)
        self.Sound = 80

        self.font = pygame.font.SysFont("kaiti", 0)

        self.yn = False
    def update(self):
        if adjust_volume_up.super_rect.width > 0:
            self.width, self.height = (adjust_volume_up.super_rect.width * 0.8, adjust_volume_up.super_rect.height * 0.6)
            self.image = pygame.transform.scale(self.image_copy, (self.width, self.height))
            self.center = (adjust_volume_up.super_rect.width * 0.43, adjust_volume_up.super_rect.height / 2)
            self.rect = self.image.get_rect(center=self.center)

            self.image_pulley = pygame.transform.scale(self.image_pulley_copy, (self.Sound / 100 * self.width, self.height))
            self.rect_pulley = self.image_pulley.get_rect()
            self.rect_pulley.topleft = 0, 0

            self.调音量()
            self.渐变色()
            self.image.set_alpha(self.fill)
            # 声音底色
            pygame.draw.rect(self.image, (105, 80, 140), (0, 0, self.rect.width, self.rect.height), border_radius=self.radius)
            # 声音进度条, 当小于7%时, 进度条高度缩小
            if self.Sound > 7:
                pygame.draw.rect(self.image_pulley, (PURPLE[0], PURPLE[1], PURPLE[2], self.fill), (0, 0, self.rect_pulley.width, self.rect_pulley.height), border_radius=self.radius)
            else:
                pygame.draw.rect(self.image_pulley, (PURPLE[0], PURPLE[1], PURPLE[2], self.fill), (0, (self.rect.height - self.Sound/100 * self.rect.width)/2 + 1, self.rect_pulley.width, self.Sound/100 * self.rect.width), border_radius=self.radius)
            self.image.blit(self.image_pulley, self.rect_pulley)
            adjust_volume_up.super_image.blit(self.image, self.rect)
            adjust_volume_up.super_image.blit(self.text, self.text_rect)
    def 渐变色(self):
        if (self.is_mouse_over() and adjust_volume_up.is_mouse_over()) or adjust_volume_up.pulley.yn == True:
            self.fill += self.fill_speed
        else:
            self.fill -= self.fill_speed
        self.fill = max(150, min(self.fill, 255))
    def 调音量(self):
        self.font = pygame.font.SysFont("kaiti", round(15 * bili * adjust_volume_up.super_rect.height/adjust_volume_up.super_max_height))
        self.text = self.font.render(str(int(self.Sound)) + "%", True, PURPLE)
        self.text_rect = self.text.get_rect()
        self.text_rect.centery = adjust_volume_up.super_rect.height / 2
        self.text_rect.right = adjust_volume_up.super_rect.width * 0.95

        if self.yn == True:
            posx = pygame.mouse.get_pos()[0]
            posx -= (kuangjia.rect.left + music_control.rect_control.left + music_control.rect_button.left + adjust_volume_up.super_rect.left + self.rect.left)
            if self.width == 0:
                self.Sound = 0
            else:
                self.Sound = round(posx / self.width * 100)
        self.Sound = max(0, min(self.Sound, 100))
    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.is_mouse_over() and adjust_volume_up.is_mouse_over() and adjust_volume_up.yn == True:
                    self.yn = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.yn = False

    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + music_control.rect_control.left + music_control.rect_button.left + adjust_volume_up.super_rect.left)
        pos[1] -= (kuangjia.rect.top + music_control.rect_control.top + music_control.rect_button.top + adjust_volume_up.super_rect.top)
        return self.rect.collidepoint(pos)

class 播放方式组件:
    def __init__(self, name, number, font_color):
        self.name = name
        self.number = number
        self.centerx = 0
        self.font_color = font_color
        self.fill = 0
        self.fill_max = 255
        self.fill_min = 0
        self.fill_speed = round(7*bili)
        self.radius = round(20*bili)
        self.center = (0, 0)
        self.width = 0
        self.height = 0
        self.super_image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.super_image_copy = self.super_image.copy()
        self.super_rect = self.super_image.get_rect(center=self.center)
        self.font = pygame.font.SysFont("kaiti", 0)
        self.text = self.font.render(str(name), True, self.font_color)
        self.text_rect = self.text.get_rect(center=((self.super_rect.width - self.text.get_width())/2, (self.super_rect.height - self.text.get_height())/2))
    def update(self):
        self.转换大小()
        if self.is_mouse_over():
            self.fill += self.fill_speed
        else:
            self.fill -= self.fill_speed
        self.fill = max(self.fill_min, min(self.fill, self.fill_max))
        pygame.draw.rect(self.super_image, (PURPLE[0], PURPLE[1], PURPLE[2], self.fill), (0, 0, self.super_rect.width, self.super_rect.height), border_radius=self.radius)
        self.super_image.blit(self.text, self.text_rect)
    def 转换大小(self):
        self.center = ((playback_mode_up.super_rect.width / 3) * (self.number - 0.5), playback_mode_up.super_rect.height / 2)
        self.width = playback_mode_up.super_rect.width / 3 * 0.8
        self.height = playback_mode_up.super_rect.height
        self.super_image = pygame.transform.scale(self.super_image_copy, (self.width, self.height))
        self.super_rect = self.super_image.get_rect(center=self.center)
        self.font = pygame.font.SysFont("kaiti", round(15 * bili * playback_mode_up.super_rect.height / playback_mode_up.super_max_height))
        self.text = self.font.render(str(self.name), True, self.font_color)
        self.text_rect = self.text.get_rect(center=(self.super_rect.width / 2, self.super_rect.height / 2))
    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + music_control.rect_control.left + music_control.rect_button.left + playback_mode_up.super_rect.left)
        pos[1] -= (kuangjia.rect.top + music_control.rect_control.top + music_control.rect_button.top + playback_mode_up.super_rect.top)
        return self.super_rect.collidepoint(pos)

class 循环播放(播放方式组件):
    def __init__(self):
        if music_control.type_play == "循环播放":
            self.COLOR = RED
        else:
            self.COLOR = BLACK
        super().__init__("循环播放", 1, self.COLOR)
    def update(self):
        super().update()
        playback_mode_up.super_image.blit(self.super_image, self.super_rect)

class 顺序播放(播放方式组件):
    def __init__(self):
        if music_control.type_play == "顺序播放":
            self.COLOR = RED
        else:
            self.COLOR = BLACK
        super().__init__("顺序播放", 2, self.COLOR)
    def update(self):
        super().update()
        playback_mode_up.super_image.blit(self.super_image, self.super_rect)

class 随机播放(播放方式组件):
    def __init__(self):
        if music_control.type_play == "随机播放":
            self.COLOR = RED
        else:
            self.COLOR = BLACK
        super().__init__("随机播放", 3, self.COLOR)
    def update(self):
        super().update()
        playback_mode_up.super_image.blit(self.super_image, self.super_rect)

class Cake:
    def __init__(self):
        self.music_yn = False
        # 设置透明度
        self.alpha = 0
        self.alpha_speed = 1.5

        self.image = pygame.Surface((width * 0.5, width * 0.5), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(width/2, kuangjia.rect.height-self.image.get_height()/2))
        # <rect(130, 117, 388, 151)> <rect(65, 268, 518, 192)> <rect(0, 459, 648, 261)>
        self.cake_bottom_height = self.rect.height*(4/11)
        self.cake_center_height = self.rect.height*(4/15)
        self.cake_top_height = self.rect.height*(4/19)

        self.bottom_cake_bili = 0.9

        self.cake_bottom = CakeBottom((self.rect.width/2, (self.rect.height - (self.cake_bottom_height*0.5))), (self.rect.width*self.bottom_cake_bili, self.cake_bottom_height))
        self.cake_center = CakeCenter((self.rect.width/2, (self.rect.height - (self.cake_bottom_height + self.cake_center_height*0.5))+2*bili), (self.rect.width*(4/5)*self.bottom_cake_bili, self.cake_center_height))
        self.cake_top = CakeTop((self.rect.width/2, (self.rect.height - (self.cake_bottom_height + self.cake_center_height + self.cake_top_height*0.5))+2*bili), (self.rect.width*(3/5)*self.bottom_cake_bili, self.cake_top_height))

        self.candle_centerx_bottom = (self.cake_top.rect.centerx, self.cake_top.rect.top)
        self.candle_size = (self.cake_top.size[0] * 0.05, self.rect.height*(1/9))
        self.candle_left = CandleSuper(self.candle_size, (self.candle_centerx_bottom[0]*0.8, self.candle_centerx_bottom[1]))
        self.candle_center = CandleSuper(self.candle_size, (self.candle_centerx_bottom[0]*1, self.candle_centerx_bottom[1]))
        self.candle_right = CandleSuper(self.candle_size, (self.candle_centerx_bottom[0]*1.2, self.candle_centerx_bottom[1]))

        # 加载奶油花方法
        def load_cream(botton_cream_number, x, y):
            # 加载奶油花图片
            try:
                cream_path = folders[22] + os.listdir(folders[22])[0]
                self.image_cream = pygame.transform.scale(pygame.image.load(cream_path), self.cream_size)
            except:
                self.image_cream = pygame.Surface(self.cream_size)
                self.image_cream.fill(RED)
            self.botton_cream_number = botton_cream_number
            for i in range(0, self.botton_cream_number):
                self.rect_ceream = self.image_cream.get_rect()
                self.rect_ceream.topleft = (
                    round(x + i * self.cream_size[0]),
                    round(y - self.cream_size[1] + 5)) # 加五剔除空隙
                self.image_cream_list.append((self.image_cream, self.rect_ceream))
        # 加载奶油花图片列表
        self.image_cream_list = []
        self.cream_size = (self.rect.width / 10, self.rect.width / 10)
        load_cream(round(self.cake_center.rect.width / self.cream_size[0]), self.cake_center.rect.x, self.cake_center.rect.top)
        load_cream(round(self.cake_bottom.rect.width / self.cream_size[0]), self.cake_bottom.rect.x, self.cake_bottom.rect.top)

        # 加载插入树枝图片
        def load_insert(image, angle, size, center):
            self.image_insert = pygame.transform.scale(image, (size[0], size[1]))
            self.image_insert = pygame.transform.rotate(self.image_insert, angle)
            self.rect_insert = self.image_insert.get_rect(center=center)
            # 将插入树枝图片和矩形添加到列表中
            self.image_insert_list.append((self.image_insert, self.rect_insert))

        self.image_insert_list = []
        try:
            image_insert_1 = pygame.image.load(folders[23] + os.listdir(
                folders[23])[0])
        except:
            image_insert_1 = pygame.Surface((self.cream_size[0], self.cream_size[1]*3))
            image_insert_1.fill(RED)
        try:
            image_insert_2 = pygame.image.load(folders[24] + os.listdir(
                folders[24])[0])
        except:
            image_insert_2 = pygame.Surface((self.cream_size[0], self.cream_size[1]*3))
            image_insert_2.fill(RED)
        # 创建两个树枝对象
        load_insert(image_insert_1, 20, (self.rect.width / 4, self.rect.width / 3), (self.rect.width * 0.15, self.rect.height * 0.2))
        load_insert(image_insert_2, -15, (self.rect.width / 7, self.rect.width / 6), (self.rect.width * 0.9, self.rect.height * 0.5))
        self.ticks = None
        # 水果
        self.fruit_list = []
        fruit_number = 20
        # 水果定位x
        x = 0
        间距_fruit = round(90*bili)
        for i in range(1, fruit_number):
            size_fruit = random.randint(int(50*bili), (int(70*bili)))
            try:
                self.image_fruit = pygame.transform.scale(pygame.image.load(folders[43] + random.choice(os.listdir(folders[43]))), (size_fruit, size_fruit))
            except:
                self.image_fruit = pygame.Surface((0, 0))
            self.rect_fruit = self.image_fruit.get_rect()
            if x > self.cake_top.rect.width-self.rect_fruit.width:
                x = random.randint(0, 间距_fruit)
            self.rect_fruit.bottom = self.cake_top.rect.top
            self.rect_fruit.x = round(self.cake_top.rect.x + x)
            self.fruit_list.append((self.image_fruit, self.rect_fruit))
            x += 间距_fruit
    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= kuangjia.rect.left
        pos[1] -= kuangjia.rect.top
        return self.rect.collidepoint(pos)
    def update(self):
        if not self.music_yn:
            birthday_music.play(-1)
            self.alpha = 0
            self.ticks = pygame.time.get_ticks()
            self.music_yn = True
        # 如果大于3秒并且透明度小于255就开始显示
        elif pygame.time.get_ticks() - self.ticks > 3000 and self.alpha < 255:
            self.alpha += self.alpha_speed
            self.alpha = max(0, min(self.alpha, 255))

        if self.alpha == 255: # 如果蛋糕整体的透明度达到255，就开始显示文字
            self.cake_center.alpha_name += self.alpha_speed
            self.cake_center.alpha_name = min(self.cake_center.alpha_name, 255)
        """# 当名字的透明度为255时，都不刷新，减少不必要的开销
        if self.cake_center.alpha_name != 255:  """
        self.cake_bottom.update()
        self.cake_center.update()
        self.cake_top.update()

        self.candle_left.update()
        self.candle_center.update()
        self.candle_right.update()
    def draw(self):
        self.image.fill((0, 0, 0, 0))

        self.cake_bottom.draw(self.alpha)
        self.cake_center.draw(self.alpha)
        self.cake_top.draw(self.alpha)

        self.candle_left.draw()
        self.candle_center.draw()
        self.candle_right.draw()

        self.image.blit(self.cake_top.image, self.cake_top.rect)
        self.image.blit(self.cake_center.image, self.cake_center.rect)
        self.image.blit(self.cake_bottom.image, self.cake_bottom.rect)

        self.image.blit(self.candle_left.image, self.candle_left.rect)
        self.image.blit(self.candle_center.image, self.candle_center.rect)
        self.image.blit(self.candle_right.image, self.candle_right.rect)

        self.image.blit(self.candle_left.fire_image, self.candle_left.fire_rect)
        self.image.blit(self.candle_center.fire_image, self.candle_center.fire_rect)
        self.image.blit(self.candle_right.fire_image, self.candle_right.fire_rect)

        for i in self.fruit_list:
            i[0].set_alpha(self.alpha)
            self.image.blit(i[0], i[1])

        # 绘制插入树枝
        for i in self.image_insert_list:
            i[0].set_alpha(self.alpha)
            self.image.blit(i[0], i[1])

        # 绘制奶油花
        for i in self.image_cream_list:
            i[0].set_alpha(self.alpha)
            self.image.blit(i[0], i[1])

        # 绘制花花草草的元素
        for i in self.cake_bottom.image_grass_flower_list:
            i[0].set_alpha(self.alpha)
            self.image.blit(i[0], i[1])
        kuangjia.image.blit(self.image, self.rect)
    def 重置(self):
        self.ticks = pygame.time.get_ticks()
        self.music_yn = False
        birthday_music.stop()
        self.cake_center.重置()
        self.candle_left.重置()
        self.candle_center.重置()
        self.candle_right.重置()

class CakeTop:
    def __init__(self, center, size):
        self.radius = round(15*bili)
        self.center = center
        self.size = size
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.center)
        self.color = PINK

        # 定义加载水果方法
        def load_star(images, star_number, size):
            # 加载水果图片
            for i in range(round(size[1]/3)):
                for j in range(star_number+1):
                    image_star = random.choice(images)
                    rect_star = image_star.get_rect()
                    if i % 2 == 0:
                        rect_star.topleft = (j*rect_star.width, i*rect_star.height)
                    else:
                        rect_star.topleft = (j*rect_star.width - rect_star.width/2, i*rect_star.height)
                    self.image_star_list.append((image_star, rect_star))

        self.image_star_list = []

        star_files = os.listdir(folders[19])
        image_stars = []
        self.number = 11
        self.star_size = (self.rect.width / self.number, ((3*self.rect.height) / self.number))
        if len(star_files) > 0:
            for i in star_files:
                try:
                    image_stars.append(pygame.transform.scale(pygame.image.load(folders[19] + i), self.star_size))
                except:
                    image_stars.append(pygame.Surface(self.star_size))
        else:
            image_stars = [pygame.Surface(self.star_size)]

        load_star(image_stars, self.number, self.star_size)
    def update(self):
        pass
    def draw(self, alpha):
        pygame.draw.rect(self.image, self.color, ((0, 0), self.size), border_top_left_radius=self.radius, border_top_right_radius=self.radius)
        # 绘制水果
        for i in self.image_star_list:
            i[0].set_alpha(alpha)
            self.image.blit(i[0], i[1])
class CakeCenter:
    def __init__(self, center, size):
        self.radius = round(15 * bili)
        self.center = center
        self.size = size
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.center)
        self.color = PURPLE

        self.font = pygame.font.Font(FONT_PATH, round(50 * bili))
        self.image_text_1 = self.font.render("Happy birthday", True, WHITE)
        self.image_text_2 = self.font.render("to Huang Yutao!", True, WHITE)
        self.image_text_1_rect = self.image_text_1.get_rect(center=(self.rect.width/2, self.rect.height/2-60*bili))
        self.image_text_2_rect = self.image_text_2.get_rect(center=(self.rect.width/2, self.rect.height/2))

        self.alpha_name = 0

        # 加载右边的香蜂草图形
        try:
            image_balm_old = pygame.image.load(folders[28]+os.listdir(folders[28])[0])
            self.image_balm = pygame.transform.scale(image_balm_old, (self.rect.width*0.2, self.rect.height*0.7))
        except:
            self.image_balm = pygame.Surface((0, 0))
        self.rect_balm = self.image_balm.get_rect()
        self.rect_balm.right = self.rect.width
        self.rect_balm.centery = round(self.rect.height * 0.4)

        # 绘制左边的麦穗
        try:
            image_wheat_old = pygame.image.load(folders[21]+os.listdir(folders[21])[0])
            new_width = self.rect.width*0.2
            new_height = image_wheat_old.get_height()*new_width/image_wheat_old.get_width()
            self.image_wheat = pygame.transform.scale(image_wheat_old, (new_width, new_height))
        except:
            self.image_wheat = pygame.Surface((0, 0))
        self.rect_wheat = self.image_wheat.get_rect()
        self.rect_wheat.left = 0
        self.rect_wheat.centery = round(self.rect.height * 0.4)
    def update(self):
        self.image_text_1.set_alpha(self.alpha_name)
        self.image_text_2.set_alpha(self.alpha_name)

    def draw(self, alpha):
        pygame.draw.rect(self.image, self.color, ((0, 0), self.size), border_top_left_radius=self.radius, border_top_right_radius=self.radius)
        self.image.blit(self.image_text_1, self.image_text_1_rect)
        self.image.blit(self.image_text_2, self.image_text_2_rect)

        # 设置透明度
        self.image_wheat.set_alpha(alpha)
        self.image.blit(self.image_wheat, self.rect_wheat)

        self.image_balm.set_alpha(alpha)
        self.image.blit(self.image_balm, self.rect_balm)
    def 重置(self):
        self.alpha_name = 0
class CakeBottom:
    def __init__(self, center, size):
        self.radius = round(15 * bili)
        self.center = center
        self.size = size
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.center)
        self.color = YELLOW

        # 加载黄色珍珠图片
        self.pearl_size = (20 * bili, 20 * bili)
        try:
            pearl_path = folders[20] + os.listdir(folders[20])[0]
            self.pearl_image = pygame.transform.scale(pygame.image.load(pearl_path), self.pearl_size)
        except:
            self.pearl_image = pygame.Surface(self.pearl_size)
            self.pearl_image.fill(YELLOW)
        self.botton_pearl_image_list = []

        self.botton_sin_play_list = []
        # 计算弧上的点，连成多边形
        for a in range(90, 180+1):
            rad = math.radians(a)
            x = self.radius + self.radius * math.cos(rad)
            y = self.radius - self.radius * math.sin(rad)
            self.botton_sin_play_list.append((x, y))
        # 计算sin函数上的点
        self.x = 0
        for i in range(round(self.rect.width) + 20):
            self.y = 40*bili + 20 * math.sin(math.radians(self.x * 2))
            self.botton_sin_play_list.append((round(self.x), round(self.y)))
            if i % 12 == 0:
                self.rect_pearl = self.pearl_image.get_rect(center=(self.x, self.y))
                self.botton_pearl_image_list.append((self.pearl_image, self.rect_pearl))
            self.x += 1
        # 计算弧上的点，连成多边形
        for a in range(0, -90-1, -1):
            rad = math.radians(a)
            x = (self.rect.width - self.radius) + self.radius * math.cos(rad)
            y = self.radius + self.radius * math.sin(rad)
            self.botton_sin_play_list.append((x, y))

        # 加载红花图片
        self.flower_size = (50 * bili, 50 * bili)
        try:
            flower_path = folders[17] + os.listdir(folders[17])[0]
            self.flower_image = pygame.transform.scale(pygame.image.load(flower_path), self.flower_size)
        except:
            self.flower_image = pygame.Surface(self.flower_size)
        self.botton_flower_image_list = []

        # 用用指数函数绘制斜线
        self.botton_exp_play_list = []
        # 计算弧上的点，连成多边形
        for a in range(90, 180 + 1):
            rad = math.radians(a)
            x = self.radius + self.radius * math.cos(rad)
            y = self.radius - self.radius * math.sin(rad)
            self.botton_exp_play_list.append((x, y))
        # 计算指数函数上的点
        self.x = 1
        for i in range(0, round(self.rect.width)):
            try:
                self.y = self.rect.height - ((self.rect.width/2)/(self.x + 200*bili))*self.rect.height/2
            except:
                pass
            # 当前y的位置能够显示时才添加元素，减少内存消耗
            if (self.y >= 0) and (self.y <= self.rect.height):
                self.botton_exp_play_list.append((self.x, self.y))
                if i % 20 == 0:
                    # 加载三个不同大小的红花
                    self.rect_flower = self.flower_image.get_rect(center=(self.x, self.y))
                    self.botton_flower_image_list.append((self.flower_image, self.rect_flower))

            self.x += 1
        # 计算弧上的点，连成多边形
        for a in range(0, -90 - 1, -1):
            rad = math.radians(a)
            x = (self.rect.width - self.radius) + self.radius * math.cos(rad)
            y = self.radius + self.radius * math.sin(rad)
            self.botton_exp_play_list.append((x, y))

        # 加载花花草草到列表方法
        def load_grass_flower(i):
            start = (i * self.rect.width / self.竖线数量 + 5 * bili,
                     self.botton_flower_image_list[i * (int(len(self.botton_flower_image_list) / self.竖线数量))][1].y + 35*bili)
            end = (i * self.rect.width / self.竖线数量 + 5 * bili,
                   self.rect.height)
            self.竖线list.append((start, end))

            # 存储第i列的元素图像信息
            # 每列的长度和元素数量
            length = (end[1] - start[1])
            number = int(length / 18)
            # 每列的圆点的中心坐标
            circle_list= []
            for j in range(1, number):
                image = random.choice(self.image_grass_flower_load_list)
                # 第i列的j个元素的坐标
                rect = image.get_rect(center=(start[0] + self.rect.x,
                                              start[1] + j/number*length + 10*bili + self.rect.y))
                circle_rect = (start[0], start[1] + (j/number)*length + 20*bili) # + 20*bili为向下挪动一点，保证能够正常显示红花
                circle_list.append(circle_rect)
                # 加载每列的元素图像以及坐标
                self.image_grass_flower_list.append((image, rect))
            self.circle_center_list.append(circle_list)
        # 加载花花草草图片, 注意：image为列表多个元素
        self.grass_flower_size = (50 * bili, 50 * bili)
        self.image_grass_flower_load_list = [] # 存储花花草草的图像Surface
        self.image_grass_flower_list = [] # 存储花花草草的图像信息和坐标
        self.circle_center_list = [] # 存储圆点的坐标
        self.circle_size = 5
        flowers_path = folders[18]
        if len(os.listdir(flowers_path)) > 0:
            for i in os.listdir(flowers_path):
                try:
                    self.image_grass_flower_load_list.append(pygame.transform.scale(pygame.image.load(flowers_path + i), self.grass_flower_size))
                except:
                    self.image_grass_flower_load_list.append(pygame.Surface(self.grass_flower_size))
        else:
            self.image_grass_flower_load_list.append(pygame.Surface(self.grass_flower_size))
        # 用列表存储竖线的起点和终点位置
        self.竖线list = []
        self.竖线数量 = 20
        for i in range(0, self.竖线数量+1):
            # 加载花花草草到列表
            load_grass_flower(i)

        # 加载彩带图片
        try:
            image_ribbon_old = pygame.image.load(folders[45] + os.listdir(folders[45])[0])
            self.image_ribbon = pygame.transform.scale(image_ribbon_old, (self.rect.width, self.rect.width * 0.25))
        except:
            self.image_ribbon = pygame.Surface((0, 0))
        self.rect_ribbon = self.image_ribbon.get_rect(center=(self.rect.width/2, self.rect.height * 0.45))

    def update(self):
        pass
    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + cake.rect.left)
        pos[1] -= (kuangjia.rect.top + cake.rect.top)
        return self.rect.collidepoint(pos)
    def draw(self, alpha):
        pygame.draw.rect(self.image, self.color, ((0, 0), self.size), border_radius=self.radius)
        # 绘制9条竖线
        for i in range(len(self.竖线list)):
            pygame.draw.line(self.image, LILAC, self.竖线list[i][0], self.竖线list[i][1], 5)
            for j in range(len(self.circle_center_list[i])):
                # 绘制圆点
                pygame.draw.circle(self.image, RED, self.circle_center_list[i][j], self.circle_size, 0)
        # 指数函数
        pygame.draw.polygon(self.image, self.color, self.botton_exp_play_list)
        # 彩带绘制
        self.image_ribbon.set_alpha(alpha)
        self.image.blit(self.image_ribbon, self.rect_ribbon)

        # 红花绘制
        for i in range(len(self.botton_flower_image_list)):
            self.botton_flower_image_list[i][0].set_alpha(alpha)
            self.image.blit(self.botton_flower_image_list[i][0], self.botton_flower_image_list[i][1])
        # 波浪线
        pygame.draw.polygon(self.image, WHITE, self.botton_sin_play_list)
        # 珍珠绘制
        for i in self.botton_pearl_image_list:
            i[0].set_alpha(alpha)
            self.image.blit(i[0], i[1])

# 蜡烛类
class CandleSuper:
    def __init__(self, size, center_bottom):
        # 火的透明度
        self.alpha = 0
        self.alpha_speed = 6

        self.size = size
        self.centerx_bottom = center_bottom
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        pygame.draw.rect(self.image, YELLOW, ((0, 0), size))
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.bottom = self.centerx_bottom
        for i in range(5):
            pygame.draw.line(self.image, WHITE, (self.rect.width, i*self.rect.height/5), (0, i*self.rect.height/5+self.rect.height/5), 10)

        self.fire_image = pygame.Surface((self.size[1]*0.3, self.size[1]*0.3), pygame.SRCALPHA)
        self.radius = round(self.fire_image.get_width()*0.6*bili)
        pygame.draw.rect(self.fire_image, RED, ((0, 0), self.fire_image.get_size()), border_top_left_radius=self.radius, border_bottom_right_radius=self.radius)
        self.fire_image = pygame.transform.rotate(self.fire_image, 45)
        self.fire_rect = self.fire_image.get_rect()
        self.fire_rect.centerx = self.rect.centerx
        self.fire_rect.bottom = self.rect.top

        self.fire_in_image = pygame.Surface((self.fire_rect.width/3, self.fire_rect.height/3), pygame.SRCALPHA)
        self.in_radius = round(self.fire_in_image.get_width() * 0.6 * bili)
        pygame.draw.rect(self.fire_in_image, YELLOW, ((0, 0), self.fire_in_image.get_size()), border_top_left_radius=self.in_radius, border_bottom_right_radius=self.in_radius)
        self.fire_in_image = pygame.transform.rotate(self.fire_in_image, 45)
        self.fire_in_rect = self.fire_in_image.get_rect()
        self.fire_in_rect.center = (round(self.fire_rect.width/2), round(self.fire_rect.height/2))

    def update(self):
        self.alpha += self.alpha_speed
        if self.alpha > 255 or self.alpha < 0:
            self.alpha_speed *= -1
    def draw(self):
        self.fire_image.set_alpha(self.alpha)
        self.fire_image.blit(self.fire_in_image, self.fire_in_rect)
        self.image.blit(self.fire_image, self.fire_rect)
    def 重置(self):
        self.alpha = 0
# 底部花类
class BottomFlower:
    def __init__(self, centerx):
        self.centerx = centerx
        self.size = (60, 50)
        try:
            self.image = pygame.transform.scale(pygame.image.load(folders[42] + os.listdir(folders[42])[0]), self.size)
        except:
            self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect(center=(self.centerx, kuangjia.rect.height-self.size[1]/2))
    def draw(self):
        kuangjia.image.blit(self.image, self.rect)

# 蛋糕合照类
class PhotoGreeting(pygame.sprite.Sprite):
    def __init__(self, center, angle, path):
        super().__init__()
        self.center = center
        size = (300*bili, 220*bili)
        try:
            img = pygame.transform.scale(pygame.image.load(path), size)
        except:
            img = pygame.Surface(size, pygame.SRCALPHA)
            img.fill(BLUE)
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.blit(img, (0, 0))
        self.image = pygame.transform.rotate(self.image, angle)
        self.image.set_alpha(255)
        self.rect = self.image.get_rect(center=self.center)

# 气球
class Balloon(pygame.sprite.Sprite):
    def __init__(self, center, speed, size, color):
        super().__init__()
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.alpha = 180
        pygame.draw.ellipse(self.image, (color[0], color[1], color[2], self.alpha), ((0, 0), (size[0], size[1]/2)))
        pygame.draw.line(self.image, (WHITE[0], WHITE[1], WHITE[2], self.alpha), (size[0]/2, size[1]/2), (size[0]/2, size[1]), 5)
        self.rect = self.image.get_rect(center=center)
        self.speed = speed
        self.alpha_speed = 0.5
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# 游戏初始画面
class GameScreen:
    def __init__(self):
        try:
            self.background_image = pygame.transform.scale(pygame.image.load(folders[1] + os.listdir(
                "./assets/fishGame/bgImg")[0]), (width, height))
        except:
            self.background_image = pygame.Surface((width, height))
            self.background_image.fill(BLUE)
        self.background_rect = self.background_image.get_rect(center=(width*0.5, height*0.5))

        self.num = 0
    def update(self):
        for i in game_number_list:
            # 显示人数选择
            i.update()
    # 开始游戏与选择人数模式的核心逻辑
    def handle_event(self, event):
        pass
    def 重置(self):
        choose_fish_Group.empty()# 清除玩家设置组显示
    def play_music(self):
        # print("播放鱼的背景音乐")
        # 循环播放鱼的背景音乐
        bg_fish_music.play(-1)
    def stop_music(self):
        # print("停止鱼的背景音乐")
        # 停止鱼的背景音乐
        bg_fish_music.stop()
        # print(222)

# 游戏模式选择人数
class GameNumber:
    def __init__(self, center, player_id, name):
        self.player_id = player_id
        self.size = (270 * bili, 140 * bili)
        self.name = name
        self.font = pygame.font.SysFont("kaiti", round(30 * bili), True, True)
        self.image_name = self.font.render(self.name, True, VIOLET, True)
        self.rect_name = self.image_name.get_rect(center=(self.size[0] / 2, self.size[1] / 2))

        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=center)

        self.border_radius = round(20 * bili)

        self.color_yes = (0, 255, 0)
        self.color_no = (128, 128, 128)
        self.color = self.color_no

        self.border = 8 * bili

        self.num = 0

    def update(self):
        if self.is_mouse_over():
            self.color = self.color_yes
        else:
            self.color = self.color_no
        pygame.draw.rect(self.image, self.color, (0, 0, self.size[0], self.size[1]), border_radius=self.border_radius)
        pygame.draw.rect(self.image, BLACK,
                         (self.border, self.border, self.size[0] - self.border * 2, self.size[1] - self.border * 2),
                         border_radius=self.border_radius)
        self.image.blit(self.image_name, self.rect_name)
        # 加载游戏模式image
        kuangjia.image.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.is_mouse_over():
                if self.player_id == 4:  # 如果开始游戏按钮已开启
                    # 创建一个我鱼路径列表
                    path = []
                    for i in choose_fish_Group:
                        # 获取玩家设置的鱼路径并添加到路径列表
                        path.append(i.return_my_fish_path())
                    # 添加我方鱼
                    add_my_fish(self.num, path)
                    button_music.play()
                    切换关卡(8)
                else:
                    # print(i.name+"被点击了")
                    action_game.num = self.player_id  # 记录玩家数量
                    # 添加self.num个玩家设置（选择鱼）到玩家设置组
                    if self.player_id == 1:
                        choose_fish_Group.add(ChooseFish(1, (width * 0.5, height * 0.4)))
                    elif self.player_id == 2:
                        choose_fish_Group.add(ChooseFish(1, (width * 0.35, height * 0.4)))
                        choose_fish_Group.add(ChooseFish(2, (width * 0.65, height * 0.4)))
                    elif self.player_id == 3:
                        choose_fish_Group.add(ChooseFish(1, (width * 0.25, height * 0.4)))
                        choose_fish_Group.add(ChooseFish(2, (width * 0.75, height * 0.4)))
                        choose_fish_Group.add(ChooseFish(3, (width * 0.5, height * 0.4)))
                    # 下一个关卡
                    button_music.play()
                    切换关卡(7)

    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= kuangjia.rect.left
        pos[1] -= kuangjia.rect.top
        return self.rect.collidepoint(pos)

# 玩家设置
class ChooseFish(pygame.sprite.Sprite):
    def __init__(self, player_id, center):
        super().__init__()
        self.player_id = player_id

        self.image = pygame.Surface((200 * bili, height * 0.5), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=center)

        self.image_click_1 = pygame.Surface((50*bili, 50*bili), pygame.SRCALPHA)
        self.rect_click_1 = self.image_click_1.get_rect(center=(self.rect.width / 2, self.image_click_1.get_height()))
        self.color_click_1_yes = VIOLET
        self.color_click_1_no = BLACK
        self.color_click_1 = self.color_click_1_no
        self.point_1 = ((self.rect_click_1.width / 2, 0),
                        (self.rect_click_1.width, self.rect_click_1.height),
                        (0, self.rect_click_1.height))

        self.image_click_2 = pygame.Surface((50 * bili, 50 * bili), pygame.SRCALPHA)
        self.rect_click_2 = self.image_click_2.get_rect(center=(self.rect.width / 2, self.rect.height - self.image_click_1.get_height()))
        self.color_click_2_yes = VIOLET
        self.color_click_2_no = BLACK
        self.color_click_2 = self.color_click_2_no
        self.point_2 = ((self.rect_click_1.width / 2, self.rect_click_2.height),
                        (0, 0),
                        (self.rect_click_2.width, 0))

        self.font = pygame.font.SysFont("kaiti", round(30*bili))
        self.image_text = self.font.render("玩家" + str(self.player_id), True, YELLOW)
        self.rect_text = self.image_text.get_rect(center=(self.rect.width / 2, self.rect.height * 0.765))

        # 玩家底座显示位置
        self.Rect = (((self.rect.width - self.rect.width*0.8)/2, (self.rect.height - self.rect.width*0.8)/2), (self.rect.width*0.8, self.rect.width*0.8))

        self.icon_my_fish_list = []
        self.image_my_fish_list = []
        self.choose_fish_index = 0
        # 存储鱼所显示的图片路径
        if len(fish_icon_list) > 0:
            for i in range(len(fish_icon_list)):
                # 存储鱼图标路径，用于传入参数
                self.icon_my_fish_list.append(folders[11] + fish_icon_list[i])
                # 初始化显示的鱼图片
                try:
                    image_my_fish_old = pygame.image.load(folders[11] + fish_icon_list[i]).convert_alpha()
                    if image_my_fish_old.get_width() > image_my_fish_old.get_height():
                        image_my_fish_old_width = 120*bili
                        image_my_fish_old_bili = image_my_fish_old_width/image_my_fish_old.get_width()
                        image_my_fish_old_height = image_my_fish_old.get_height()*image_my_fish_old_bili
                    else:
                        image_my_fish_old_height = 120*bili
                        image_my_fish_old_bili = image_my_fish_old_height / image_my_fish_old.get_height()
                        image_my_fish_old_width = image_my_fish_old.get_width() * image_my_fish_old_bili
                    image_my_fish = pygame.transform.scale(image_my_fish_old, (image_my_fish_old_width, image_my_fish_old_height))
                except:
                    image_my_fish_old_width = 120*bili
                    image_my_fish_old_height = 120*bili
                    image_my_fish_old = pygame.Surface((image_my_fish_old_width, image_my_fish_old_height), pygame.SRCALPHA)
                    image_my_fish = image_my_fish_old

                # 对原始图片进行缩放
                rect_my_fish = image_my_fish.get_rect(center=(self.rect.width / 2, self.rect.height / 2))
                self.image_my_fish_list.append((image_my_fish, rect_my_fish))
        else:
            # 没有鱼图标，显示默认图标
            self.icon_my_fish_list.append("None")
            image_my_fish = pygame.Surface((120*bili, 120*bili), pygame.SRCALPHA)
            rect_my_fish = image_my_fish.get_rect(center=(self.rect.width / 2, self.rect.height / 2))
            # 加载默认图标到列表
            self.image_my_fish_list.append((image_my_fish, rect_my_fish))

        # print(self.rect)
    def is_mouse_over_1(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + self.rect.left)
        pos[1] -= (kuangjia.rect.top + self.rect.top)
        return self.rect_click_1.collidepoint(pos)
    def is_mouse_over_2(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + self.rect.left)
        pos[1] -= (kuangjia.rect.top + self.rect.top)
        return self.rect_click_2.collidepoint(pos)
    def update(self):
        if self.is_mouse_over_1():
            self.color_click_1 = self.color_click_1_yes
        else:
            self.color_click_1 = self.color_click_1_no
        if self.is_mouse_over_2():
            self.color_click_2 = self.color_click_2_yes
        else:
            self.color_click_2 = self.color_click_2_no
        # 加载玩家设置image
        pygame.draw.rect(self.image, (GRAY[0], GRAY[1], GRAY[2], 128), ((0, 0), self.image.get_size()), border_radius=round(30*bili))
        pygame.draw.polygon(self.image_click_1, self.color_click_1, self.point_1)
        pygame.draw.polygon(self.image_click_2, self.color_click_2, self.point_2)
        self.image.blit(self.image_text, self.rect_text)
        self.image.blit(self.image_click_1, self.rect_click_1)
        self.image.blit(self.image_click_2, self.rect_click_2)
        pygame.draw.rect(self.image, WHITE, self.Rect, border_radius=round(20*bili))
        self.image.blit(self.image_my_fish_list[self.choose_fish_index][0], self.image_my_fish_list[self.choose_fish_index][1])
        kuangjia.image.blit(self.image, self.rect)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.is_mouse_over_1():
                    button_music.play()
                    self.choose_fish_index -= 1
                    if self.choose_fish_index < 0:
                        self.choose_fish_index = len(self.image_my_fish_list) - 1
                elif self.is_mouse_over_2():
                    button_music.play()
                    self.choose_fish_index += 1
                    if self.choose_fish_index >= len(self.image_my_fish_list):
                        self.choose_fish_index = 0
    def return_my_fish_path(self):
        return self.icon_my_fish_list[self.choose_fish_index]

# 游戏说明
class GameSpeak:
    def __init__(self):
        self.image_number = []
        self.font_text = pygame.font.SysFont("kaiti", round(20*bili))
        self.image_1 = self.font_text.render("本游戏提供三人模式", True, VIOLET)
        self.image_2 = self.font_text.render("初始值大小均为10克，通过吃小鱼来增长大小", True, VIOLET)
        self.image_3 = self.font_text.render("玩家1按键：上下左右(W S A D) 技能(E)", True, VIOLET)
        self.image_4 = self.font_text.render("玩家2按键：上下左右(I K J L) 技能(O)", True, VIOLET)
        self.image_5 = self.font_text.render("玩家3按键：上下左右(↑ ↓ ← →) 技能(数字区1)", True, VIOLET)
        self.image_6 = self.font_text.render("击败敌方有60%概率掉落属性加成", True, VIOLET)
        self.image_7 = self.font_text.render("玩家可捡拾掉落的属性加成，7秒过后过期自动消失", True, VIOLET)
        self.image_8 = self.font_text.render("生命与技能最大存储量均为3", True, VIOLET)
        self.image_9 = self.font_text.render("有四种难度等级可供选择", True, VIOLET)
        self.image_10 = self.font_text.render("玩家积分达到30000分，即游戏胜利", True, VIOLET)
        self.image_11 = self.font_text.render("注：键盘需在英文输入状态下使用", True, VIOLET)
        self.image_number.append(self.image_1)
        self.image_number.append(self.image_2)
        self.image_number.append(self.image_3)
        self.image_number.append(self.image_4)
        self.image_number.append(self.image_5)
        self.image_number.append(self.image_6)
        self.image_number.append(self.image_7)
        self.image_number.append(self.image_8)
        self.image_number.append(self.image_9)
        self.image_number.append(self.image_10)
        self.image_number.append(self.image_11)

        self.image_text = pygame.Surface((500 * bili, 600 * bili), pygame.SRCALPHA)
        self.rect_text = self.image_text.get_rect(center=(width * 0.8, height * 0.5))
        pygame.draw.rect(self.image_text, BLACK, ((0, 0), self.rect_text.size), border_radius=round(20*bili))
        for i in range(len(self.image_number)):
            self.image_text.blit(self.image_number[i], (10*bili, i * 50 * bili + 20*bili))

        self.image = pygame.Surface((140 * bili, 70 * bili), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(width * 0.2, height / 2))
        pygame.draw.rect(self.image, BLACK, ((0, 0), self.rect.size), border_radius=round(20*bili))
        self.font_speak = pygame.font.SysFont("kaiti", round(30*bili))
        self.image_speak = self.font_speak.render("游戏说明", True, VIOLET)
        self.rect_speak = self.image_speak.get_rect(center=(self.rect.width / 2, self.rect.height / 2))
        self.image.blit(self.image_speak, self.rect_speak)

    def update(self):
        kuangjia.image.blit(self.image, self.rect)
        if self.is_mouse_over():
            kuangjia.image.blit(self.image_text, self.rect_text)
    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= kuangjia.rect.left
        pos[1] -= kuangjia.rect.top
        return self.rect.collidepoint(pos)

# 游戏难度
class GameDifficult:
    def __init__(self):
        self.bg_color = (GRAY[0], GRAY[1], GRAY[2], 128)
        self.border_radius = round(30 * bili)
        self.image = pygame.Surface((400 * bili, 70 * bili), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(width * 0.5, height * 0.95))
        
        self.enemy_number = 0 # 初始敌鱼数量为0个
        self.enemy_width_max_min = (0, 0) # 初始敌鱼宽度最大值为0个
        self.enemy_speed_range = (0, 0, 0) # 初始敌鱼速度范围为0个

        self.current_difficult = 1 # 初始值为简单
        self.font = pygame.font.SysFont("kaiti", round(30*bili))
        self.difficult_dict = {1: self.font.render("简单", True, YELLOW), 
                          2: self.font.render("中等", True, YELLOW), 
                          3: self.font.render("困难", True, YELLOW), 
                          4: self.font.render("超难", True, YELLOW)}
        self.image_text = self.difficult_dict[self.current_difficult] # 初始值为简单
        self.rect_text = self.image_text.get_rect(center=(self.rect.width / 2, self.rect.height / 2))

        self.image_click_1 = pygame.Surface((50 * bili, 60 * bili), pygame.SRCALPHA)
        self.rect_click_1 = self.image_click_1.get_rect(center=(40*bili, self.rect.height / 2))
        self.color_click_1_yes = VIOLET
        self.color_click_1_no = BLACK
        self.color_click_1 = self.color_click_1_no
        self.point_1 = ((0, self.rect_click_1.height / 2), (self.rect_click_1.width, 0), (self.rect_click_1.width, self.rect_click_1.height))

        self.image_click_2 = pygame.Surface((50 * bili, 60 * bili), pygame.SRCALPHA)
        self.rect_click_2 = self.image_click_2.get_rect(center=(self.rect.width - 40*bili, self.rect.height / 2))
        self.color_click_2_yes = VIOLET
        self.color_click_2_no = BLACK
        self.color_click_2 = self.color_click_2_no
        self.point_2 = ((self.rect_click_2.width, self.rect_click_2.height / 2), (0, 0), (0, self.rect_click_2.height))

    def update(self):
        if self.is_mouse_over_1():
            self.color_click_1 = self.color_click_1_yes

        else:
            self.color_click_1 = self.color_click_1_no
        if self.is_mouse_over_2():
            self.color_click_2 = self.color_click_2_yes
        else:
            self.color_click_2 = self.color_click_2_no
    def draw(self):
        # 加载游戏难度image
        pygame.draw.rect(self.image, self.bg_color, ((0, 0), self.rect.size),border_radius=self.border_radius)
        pygame.draw.polygon(self.image_click_1, self.color_click_1, self.point_1)
        pygame.draw.polygon(self.image_click_2, self.color_click_2, self.point_2)
        self.image.blit(self.image_click_1, self.rect_click_1)
        self.image.blit(self.image_click_2, self.rect_click_2)
        self.image.blit(self.image_text, self.rect_text)
        kuangjia.image.blit(self.image, self.rect)

    def is_mouse_over_1(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + self.rect.left)
        pos[1] -= (kuangjia.rect.top + self.rect.top)
        return self.rect_click_1.collidepoint(pos)

    def is_mouse_over_2(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= (kuangjia.rect.left + self.rect.left)
        pos[1] -= (kuangjia.rect.top + self.rect.top)
        return self.rect_click_2.collidepoint(pos)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.is_mouse_over_1():
                    button_music.play()
                    self.current_difficult -= 1
                    if self.current_difficult < 1:
                        self.current_difficult = len(self.difficult_dict)
                        # print(self.current_difficult)
                    self.image_text = self.difficult_dict[self.current_difficult]
                    self.rect_text = self.image_text.get_rect(center=(self.rect.width / 2, self.rect.height / 2))
                elif self.is_mouse_over_2():
                    button_music.play()
                    self.current_difficult += 1
                    if self.current_difficult > len(self.difficult_dict):
                        self.current_difficult = 1
                        # print(self.current_difficult)
                    self.image_text = self.difficult_dict[self.current_difficult]
                    self.rect_text = self.image_text.get_rect(center=(self.rect.width / 2, self.rect.height / 2))
    def set_enemy_fish_number(self):
        if self.current_difficult == 1:
            self.enemy_number = 25
            self.enemy_width_max_min = (20*bili, 50*bili)
            self.enemy_speed_range = (0.15, 1.8, 4)
        elif self.current_difficult == 2:
            self.enemy_number = 30
            self.enemy_width_max_min = (25*bili, 55*bili)
            self.enemy_speed_range = (0.2, 2, 5)
        elif self.current_difficult == 3:
            self.enemy_number = 35
            self.enemy_width_max_min = (30*bili, 60*bili)
            self.enemy_speed_range = (0.25, 2.5, 8)
        elif self.current_difficult == 4:
            self.enemy_number = 40
            self.enemy_width_max_min = (35*bili, 65*bili)
            self.enemy_speed_range = (0.32, 3.2, 10)
        return 0
    # 重置游戏难度为简单 1
    def 重置(self):
        self.current_difficult = 1
        self.set_enemy_fish_number()
        # 重置游戏难度文本image
        self.image_text = self.difficult_dict[self.current_difficult]
        self.rect_text = self.image_text.get_rect(center=(self.rect.width / 2, self.rect.height / 2))

# 我鱼类
class MyFish(pygame.sprite.Sprite):
    # 定义两个玩家的控制配置
    PLAYER_CONFIG = {
        # 一号玩家的控制配置
        1: {
            'move_keys': {
                'left': pygame.K_a,
                'right': pygame.K_d,
                'up': pygame.K_w,
                'down': pygame.K_s
            },
            'attack_key': pygame.K_e,
            'start_position': (kuangjia.rect.width*0.3, kuangjia.rect.height*0.4),
            'color': (255, 51, 255),  # 紫色
            'lifebar_center': (kuangjia.rect.width*0.23, 80*bili) # 血条中心坐标
        },
        # 二号玩家的控制配置
        3: {
            'move_keys': {
                'left': pygame.K_j,
                'right': pygame.K_l,
                'up': pygame.K_i,
                'down': pygame.K_k
            },
            'attack_key': pygame.K_o,
            'start_position': (kuangjia.rect.width*0.5, kuangjia.rect.height*0.6),
            'color': (255, 128, 0),  # 黄色
            'lifebar_center': (kuangjia.rect.width * 0.5, 80*bili) # 血条中心坐标
        },
        2: {
            'move_keys': {
                'left': pygame.K_LEFT,
                'right': pygame.K_RIGHT,
                'up': pygame.K_UP,
                'down': pygame.K_DOWN
            },
            'attack_key': pygame.K_KP_1,
            'start_position': (kuangjia.rect.width*0.7, kuangjia.rect.height*0.4),
            'color': (0, 255, 128),  # 绿色
            'lifebar_center': (kuangjia.rect.width * 0.77, 80*bili) # 血条中心坐标
        }
    }

    def __init__(self, player_id, fish_icon):
        super().__init__()
        self.player_id = player_id
        # 配置玩家的控制配置
        self.config = self.PLAYER_CONFIG[player_id]
        self.keys = self.config['move_keys']

        # 加载鱼图片
        def load_fish_icon():
            try:
                # 加载原始图片
                self.ico_left_copy = pygame.transform.flip(pygame.image.load(fish_icon), True, False)  # 水平翻转
                self.ico_right_copy = pygame.transform.flip(pygame.image.load(fish_icon), False, False)  # 保持原样
                # 加载原始大小
                self.size_copy = (self.ico_left_copy.get_width(), self.ico_right_copy.get_height())
                # 加载原始比例:宽/高
                self.bili_copy = self.ico_left_copy.get_width() / self.ico_right_copy.get_height()

                # 加载我鱼图标
                fish_image = self.ico_left_copy
                fish_size = 1000 # 面积固定为1000
                # 系数，确保缩小后的面积固定为1000
                k = math.sqrt(fish_size / (fish_image.get_width() * fish_image.get_height()))
                # 缩放后的鱼宽高
                fish_width = fish_image.get_width() * k
                fish_height = fish_image.get_height() * k
                self.little_size = (fish_width, fish_height)  # 缩放后的鱼大小

                # 创建缩小后的左右图像
                self.image_left = pygame.transform.scale(self.ico_left_copy, self.little_size)  # 缩小鱼图片
                self.image_right = pygame.transform.scale(self.ico_right_copy, self.little_size)  # 缩小鱼图片


            except:
                self.little_size = (45*bili, 22.5*bili)  # 缩放后的鱼大小

                # 加载原始图片
                self.ico_left_copy = pygame.Surface(self.little_size)  # 水平翻转
                self.ico_right_copy = pygame.Surface(self.little_size)  # 保持原样
                # 加载原始大小
                self.size_copy = (self.ico_left_copy.get_width(), self.ico_right_copy.get_height())
                # 加载原始比例:宽/高
                self.bili_copy = self.ico_left_copy.get_width() / self.ico_right_copy.get_height()

                # 加载失败时使用颜色块
                self.image_left = pygame.Surface(self.little_size)
                self.image_right = pygame.Surface(self.little_size)
                self.image_left.fill((0, 0, 255))
                self.image_right.fill((0, 255, 0))

        # 先调用加载函数
        load_fish_icon()
        # 计算对角线增长比例
        self.对角线 = math.sqrt(self.size_copy[0] ** 2 + self.size_copy[1] ** 2)
        self.增长比例_width = self.size_copy[0] / self.对角线
        self.增长比例_height = self.size_copy[1] / self.对角线

        # 初始化当前显示图像
        self.image = self.image_left

        # 创建碰撞掩码（用于精确碰撞检测）
        self.mask_left = pygame.mask.from_surface(self.image_left)
        self.mask_right = pygame.mask.from_surface(self.image_right)
        self.mask = self.mask_left

        # 初始技能属性
        self.skill = {
            # 初始积分
            "积分": 0,
            # 初始速度，只有捡技能才能加速
            "speed_fish": 1,
            # 初始子弹速度
            "speed_attack": 20,
            # 初始子弹加载进度
            "bullet_time": 0,
            # 子弹加载速度
            "bullet_speed_load": 0.07,
            # 子弹增量大小
            "bullet_number": 0
        }
        self.direction = "left"  # 初始化方向
        if self.direction == "left":
            self.image = self.image_left
            self.mask = self.mask_left  # 初始化掩码

        elif self.direction == "right":
            self.image = self.image_right
            self.mask = self.mask_right  # 初始化掩码

        self.rect = self.image.get_rect(center=self.config['start_position'])  # 初始化位置矩形
        self.centerx_copy = self.rect.centerx
        self.centery_copy = self.rect.centery
        # 子弹图片的路径
        self.bullet_path = f"./assets/fishGame/myFish/bullet{self.player_id}/"
        # 血条坐标列表
        self.image_rect_life_list = []
        # 绘制血条image
        self.image_life = pygame.Surface((40*bili, 40*bili), pygame.SRCALPHA)

        # 绘制爱心
        pygame.draw.circle(self.image_life, (255, 0, 0), (1/4*self.image_life.get_width(), 1/4*self.image_life.get_width()), 1/4*self.image_life.get_width())
        pygame.draw.circle(self.image_life, (255, 0, 0), (3/4*self.image_life.get_width(), 1/4*self.image_life.get_width()), 1/4*self.image_life.get_width())
        pygame.draw.polygon(self.image_life, (255, 0, 0), [(self.image_life.get_width() * 0.03, self.image_life.get_height() * 0.35),(self.image_life.get_width()*0.49, self.image_life.get_height()*0.8), (self.image_life.get_width() * 0.93, self.image_life.get_height() * 0.35), (self.image_life.get_width()*0.5, self.image_life.get_height()/4)])
        # 初始化血条数量
        for i in range(3):
            self.rect_life = self.image_life.get_rect(center=self.config['lifebar_center'])
            self.rect_life.x += i * 50 * bili
            self.image_rect_life_list.append((self.image_life, self.rect_life))
    def update(self):
        # 刷新数据
        my_fish_name_list[self.player_id - 1].add_积分_子弹(self.skill["积分"], (self.skill["bullet_time"] / 100))
        # print("玩家", self.player_id, "更新")
        key = pygame.key.get_pressed()
        # 玩家移动
        if key[self.keys['left']]:
            self.centerx_copy -= self.skill["speed_fish"]
        if key[self.keys['right']]:
            self.centerx_copy += self.skill["speed_fish"]
        if key[self.keys['up']]:
            self.centery_copy -= self.skill["speed_fish"]
        if key[self.keys['down']]:
            self.centery_copy += self.skill["speed_fish"]
        # 子弹加载进度
        self.skill["bullet_time"] += self.skill["bullet_speed_load"]
        # 最多只能存储3颗子弹
        self.skill["bullet_time"] = max(0, min(self.skill["bullet_time"], 300))
        # 鱼的位置限定范围
        self.centerx_copy = max(self.rect.width / 2.0, min(self.centerx_copy, kuangjia.rect.width - self.rect.width / 2.0))
        self.centery_copy = max(self.rect.height / 2.0, min(self.centery_copy, kuangjia.rect.height - self.rect.height / 2.0))
        self.rect.center = (self.centerx_copy, self.centery_copy)

        # 用于测试增加大小
        """self.add_size(3000*bili)
        self.add_积分(3000*bili/100)"""

    def draw(self):
        # 绘制我鱼
        kuangjia.image.blit(self.image, self.rect)
        # 绘制血条
        for image_life, rect_life in self.image_rect_life_list:
            kuangjia.image.blit(image_life, rect_life)

    def handle_event(self, event):
        # 切换方向
        if event.type == pygame.KEYDOWN:
            if event.key == self.keys['left']:
                self.direction = "left"  # 切换方向为左移
                # 刷新图标和掩码
                self.image = self.image_left
                self.mask = self.mask_left
            if event.key == self.keys['right']:
                self.direction = "right"  # 切换方向为右移
                self.image = self.image_right
                self.mask = self.mask_right
            # 发射子弹，如果子弹加载进度大于等于100，才能发射子弹
            if event.key == self.config['attack_key'] and self.skill["bullet_time"] >= 100:
                # 发射子弹
                self.add_bullet()
                bullet_music.play() # 播放子弹音效
                # 减少一颗子弹加载进度
                self.skill["bullet_time"] -= 100
                # print("发射子弹")

    # enemy_size与my_size为面积/增加大小
    def add_size(self, enemy_size):
        # 计算我方当前面积
        my_size = self.rect.width * self.rect.height

        # 增长系数
        k = 1.5
        # 计算增长比例：敌人越大，增长越多
        extra_growth = (enemy_size / my_size)*k + 1 # 额外增长（敌人越大越多）,基础值加1
        # print(extra_growth)

        
        # 先计算宽度，再根据原始宽高比计算高度
        new_width = self.rect.width + extra_growth
        # new_width = min(new_width, 800)
        new_height = new_width / self.bili_copy # 计算新尺寸（保持原始宽高比）
        # new_height = min(new_height, 800)
        
        # 最大高度
        """if new_height > 400*bili:
            new_height = 400*bili
            new_width = new_height * self.bili_copy"""
        
        new_size = (new_width, new_height)

        # 缩放后的原始图像
        self.image_left = pygame.transform.scale(self.ico_left_copy, new_size)
        self.image_right = pygame.transform.scale(self.ico_right_copy, new_size)

        # 更新 mask
        self.mask_left = pygame.mask.from_surface(self.image_left)
        self.mask_right = pygame.mask.from_surface(self.image_right)

        # 根据方向设置当前图像
        if self.direction == "left":
            self.image = self.image_left
            self.mask = self.mask_left
        elif self.direction == "right":
            self.image = self.image_right
            self.mask = self.mask_right

        # 更新 rect（保持中心位置不变）
        old_center = self.rect.center
        # print(new_size[0]/new_size[1], self.rect.width/self.rect.height, self.ico_left_copy.get_width() / self.ico_left_copy.get_height())
        self.rect = self.image.get_rect(center=old_center)

    # 更新鱼积分
    def add_积分(self, score):
        # 更新我鱼积分
        self.skill["积分"] += score

    def add_speed_fish(self, speed):
        self.skill["speed_fish"] += speed
    # 增加子弹的加载进度速度
    def add_bullet_speed_load(self, speed):
        self.skill["bullet_speed_load"] += speed

    def add_bullet_number(self):
        # 增加子弹数量
        self.skill["bullet_time"] = 300
    def add_life(self, num):
        # 生命值加1
        # 遍历增加生命值图标，每次增加一个生命值
        for i in range(num):
            # 限定范围为0-3
            if len(self.image_rect_life_list) >= 3:
                break
            self.rect_life = self.image_life.get_rect(center=self.config['lifebar_center'])
            self.rect_life.x += len(self.image_rect_life_list) * 50 * bili
            self.image_rect_life_list.append((self.image_life, self.rect_life))
    # 加载子弹
    def add_bullet(self):
        # 玩家的子弹精灵组添加子弹对象
        if len(os.listdir(self.bullet_path)) > 0:
            # 加载子弹
            bullet_path = self.bullet_path+os.listdir(self.bullet_path)[0]
        else:
            bullet_path = "None"
        bullet_list[self.player_id-1].add(Bullet(bullet_path, list(self.rect.center), self.skill["speed_attack"], self.direction, (self.rect.width*0.6, self.rect.width*0.3)))
# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet, center, speed, direction, size):
        pygame.sprite.Sprite.__init__(self)
        try:
            self.bullet = pygame.image.load(bullet).convert_alpha()
            self.bullet = pygame.transform.scale(self.bullet, size)
        except:
            self.bullet = pygame.Surface(size)
            self.bullet.fill(RED)
        self.center = center
        self.speed = speed
        self.size = size
        self.direction = direction

        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        # 设置子弹方向
        if self.direction == "left":
            # 转向右边，x轴翻转
            self.bullet = pygame.transform.flip(self.bullet, True, False)
            self.image.blit(self.bullet, (0, 0))
            self.speed = -self.speed
        else:
            self.image.blit(self.bullet, (0, 0))
        self.rect = self.image.get_rect(center=self.center)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.center = (int(self.center[0]), int(self.center[1]))
        self.center[0] += self.speed
        if self.center[0] < -self.rect.width/2 or self.center[0] > kuangjia.rect.width + self.rect.width/2:
            self.kill()
# 爆炸类
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        # 加载爆炸图片
        path_explosion = folders[4]
        self.center = center
        self.explosion_list = []
        if len(os.listdir(path_explosion)) > 0:
            for i in range(len(os.listdir(path_explosion))):
                try:
                    explosion = pygame.image.load(path_explosion + os.listdir(path_explosion)[i]).convert_alpha()
                    explosion = pygame.transform.scale(explosion, size)
                    self.explosion_list.append(explosion)
                except:
                    self.explosion_list.append(pygame.Surface(size))
        else:
            self.explosion_list.append(pygame.Surface(size))
        self.time_ticks = pygame.time.get_ticks()
        self.index_id = 0
        self.image = self.explosion_list[self.index_id]
        self.rect = self.image.get_rect(center=self.center)
    def update(self):
        if pygame.time.get_ticks() - self.time_ticks > 100:
            self.time_ticks = pygame.time.get_ticks()
            self.index_id += 1
            if self.index_id >= len(self.explosion_list):
                self.kill()
            else:
                self.image = self.explosion_list[self.index_id]

# 我鱼名称
class MyFishName:
    def __init__(self, name, center, color, size, player_id, bullet_path, image_head, size_head):
        self.player_id = player_id
        # 将 size 转换为整数，pygame.font.SysFont 要求字体大小必须是整数
        self.font = pygame.font.SysFont('kaiti', int(size))
        self.color = color
        self.center = center
        self.image_name = self.font.render(name, True, self.color)
        self.rect_name = self.image_name.get_rect(center=self.center)
        self.image_积分_子弹 = self.font.render("积分：0.00 子弹：0.00", True, self.color)
        self.rect_积分_子弹 = self.image_积分_子弹.get_rect(center=(self.center[0], self.center[1] + 80 * bili))

        self.path_bullet = bullet_path
        try:
            self.image_bullet = pygame.image.load(self.path_bullet + os.listdir(self.path_bullet)[0])
        except:
            self.image_bullet = pygame.Surface((10, 25))
            self.image_bullet.fill(RED)
        # 如果是横向就摆正
        if self.image_bullet.get_width() > self.image_bullet.get_height():
            self.image_bullet = pygame.transform.rotate(self.image_bullet, 90)
        # 保持宽度为10，高度与之成比例
        self.width_bullet = 20*bili
        self.bili_bullet = self.width_bullet/self.image_bullet.get_width()
        self.height_bullet = self.bili_bullet*self.image_bullet.get_height()
        # 获取最终的子弹尺寸
        jiange = (self.width_bullet + 30*bili) # 子弹之间的间距
        akx = self.center[0] + 20*bili # 初始位置
        self.rect_bullet_list = ((akx + jiange, self.center[1]), (akx + 2*jiange, self.center[1]), (akx + 3*jiange, self.center[1])) # 子弹的位置集合
        self.size_bullet = (self.width_bullet, self.height_bullet)
        self.image_bullet = pygame.transform.scale(self.image_bullet, self.size_bullet)
        self.num_bullet = 0
        # 玩家头像
        self.image_head = pygame.transform.scale(image_head, (size_head[0]*2, size_head[1]*2))
        self.rect_head = self.image_head.get_rect(center=(self.center[0] - 130*bili, self.center[1] + 30*bili))
    def update(self):
        kuangjia.image.blit(self.image_name, self.rect_name)
        kuangjia.image.blit(self.image_积分_子弹, self.rect_积分_子弹)
        # 便利每个子弹数量
        for i in range(1, int(self.num_bullet)+1):
            kuangjia.image.blit(self.image_bullet, self.rect_bullet_list[i-1])
        # 绘制玩家头像
        kuangjia.image.blit(self.image_head, self.rect_head)
    def add_积分_子弹(self, 积分, 子弹):
        del self.num_bullet
        self.num_bullet = 子弹
        del self.image_积分_子弹
        self.image_积分_子弹 = self.font.render("积分：" + f"{积分:.2f} 子弹：" + f"{self.num_bullet:.2f}",  True, self.color)
        # self.rect_积分_子弹 = self.image_积分_子弹.get_rect(center=(self.center[0], self.center[1] + 80 * bili))

# 加成属性
class AddSkill(pygame.sprite.Sprite):
    def __init__(self, skill, center):
        pygame.sprite.Sprite.__init__(self)
        self.name = skill
        self.size = (50*bili, 50*bili)
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=center)
        # 加载技能图标
        def image_skill_load():
            path = folders[5]
            try:
                skill_icon = pygame.image.load(path + os.listdir(path)[0])
                skill_icon = pygame.transform.scale(skill_icon, self.size)
                self.image.blit(skill_icon, (0, 0))
            except:
                pygame.draw.circle(self.image, RED, (self.size[0]/2, self.size[1]/2), self.size[0]/2)
        self.font = pygame.font.SysFont("kaiti", int(20*bili))
        # 调用加载技能图标函数
        image_skill_load()
        if len(self.name) > 2:
            self.name_1 = self.name[:2]
            self.name_2 = self.name[2:]

            self.image_render_1 = self.font.render(self.name_1, True, RED)
            self.rect_render_1 = self.image_render_1.get_rect(center=(self.rect.width / 2, self.rect.height / 2-7*bili))
            self.image_render_2 = self.font.render(self.name_2, True, RED)
            self.rect_render_2 = self.image_render_2.get_rect(center=(self.rect.width / 2, self.rect.height / 2+7*bili))
            self.image.blit(self.image_render_1, self.rect_render_1)
            self.image.blit(self.image_render_2, self.rect_render_2)
        else:
            self.image_render = self.font.render(self.name, True, RED)
            self.rect_render = self.image_render.get_rect(center=(self.rect.width / 2, self.rect.height / 2))
            self.image.blit(self.image_render, self.rect_render)
        # 创建掩码
        self.mask = pygame.mask.from_surface(self.image)
        # 创建初始时间
        self.start_time = pygame.time.get_ticks()
        # 显示时间为7秒
        self.show_time = 7000
    def update(self):
        # 时间到达，删除精灵
        if (pygame.time.get_ticks() - self.start_time) > self.show_time:
            self.kill()
# 敌人鱼类
class EnemyFish(pygame.sprite.Sprite):
    def __init__(self, fish_path, direction, my_fish_size_max, enemy_fish_width_max_min, speed_range):
        super().__init__()
        self.direction = direction
        # 加载原始图片
        try:
            low_ico = pygame.image.load(fish_path)
        except:
            low_ico = pygame.Surface((100, 100))
            low_ico.fill((255, 0, 0))
        # 获取原始图片尺寸
        size = low_ico.get_size()
        # 随机最大宽度的算法
        max_width = round(math.sqrt(my_fish_size_max) + enemy_fish_width_max_min[1]) # enemy_fish_width_max_min：敌鱼最小宽度范围，最大宽度为鱼的面积加上敌鱼的宽度范围

        # 定义最大面积，防止过大
        max_size = (kuangjia.rect.width * 0.2)**2

        # 限制最大宽度，确保鱼的面积不超过 max_size
        # 面积 = width * height，height = width * (size[1]/size[0])
        # width = sqrt(面积 * (size[0]/size[1]))
        max_width_limit = int(math.sqrt(max_size * (size[0]/size[1])))
        max_width = min(max_width, max_width_limit)
        
        # new_width为随机获取敌鱼宽度范围内的宽度
        new_width = random.randint(round(enemy_fish_width_max_min[0]), max_width)
        width_bili = new_width/size[0] # 宽度与原始图片宽度比例
        # 高度
        new_height = size[1]*width_bili
        # 新的敌鱼图片尺寸
        self.little_size = (new_width, new_height)

        # 加载鱼图片
        def load_fish_icon():
            try:
                # 加载原始图片
                self.ico_left_copy = pygame.transform.flip(pygame.image.load(fish_path), True, False)  # 水平翻转
                self.ico_right_copy = pygame.transform.flip(pygame.image.load(fish_path), False, False)  # 保持原样
                # 加载原始大小
                self.size_copy = (self.ico_left_copy.get_width(), self.ico_right_copy.get_height())
                # 加载原始比例:宽/高
                self.bili_copy = self.ico_left_copy.get_width() / self.ico_right_copy.get_height()

                # 创建缩小后的左右图像
                self.image_left = pygame.transform.scale(self.ico_left_copy, self.little_size)  # 缩小鱼图片
                self.image_right = pygame.transform.scale(self.ico_right_copy, self.little_size)  # 缩小鱼图片


            except:
                # 加载失败时使用颜色块
                self.image_left = pygame.Surface(self.little_size)
                self.image_right = pygame.Surface(self.little_size)
                self.image_left.fill((0, 0, 255))
                self.image_right.fill((0, 255, 0))

        # 先调用加载函数
        load_fish_icon()

        # 初始化当前显示图像
        self.image = self.image_left

        # 创建碰撞掩码（用于精确碰撞检测）
        self.mask_left = pygame.mask.from_surface(self.image_left)
        self.mask_right = pygame.mask.from_surface(self.image_right)
        # self.mask = self.mask_left

        choc = []
        for i in range(10):
            choc.append(random.uniform(speed_range[0], speed_range[1]))
        choc.append(speed_range[2]) # 唯一最大速度
        self.speed_fish = random.choice(choc)
        if self.direction == "left":
            self.image = self.image_left
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(int(kuangjia.rect.width + self.rect.width), int(kuangjia.rect.width + self.rect.width*2))
            self.rect.y = random.randint(0, int(kuangjia.rect.height - self.rect.height))
            self.speed_fish = -self.speed_fish
            # 斩杀线
            self.kill_line = -self.rect.width
            self.mask = self.mask_left  # 设置掩码
        else:
            self.image = self.image_right
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(int(-self.rect.width*2), int(-self.rect.width))
            self.rect.y = random.randint(0, int(kuangjia.rect.height - self.rect.height))
            self.speed_fish = self.speed_fish
            # 斩杀线
            self.kill_line = kuangjia.rect.width+self.rect.width//2
            self.mask = self.mask_right  # 设置掩码
        self.centerx_copy = self.rect.centerx
        self.centery_copy = self.rect.centery

    def update(self):
        self.centerx_copy += self.speed_fish
        # 自杀条件
        if self.direction == "left" and self.centerx_copy < self.kill_line:
            self.kill()
        elif self.direction == "right" and self.centerx_copy > self.kill_line:
            self.kill()
        self.rect.center = (int(self.centerx_copy), int(self.centery_copy))
# 游戏胜利
class GameWin:
    def __init__(self):
        self.image = pygame.Surface((400*bili, 300*bili), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(kuangjia.rect.width//2, kuangjia.rect.height//2))

        self.font = pygame.font.SysFont("kaiti", round(30 * bili))
        self.image_text = None
        self.rect_text = None
        self.image_text2 = self.font.render("(哟，挺闲的啊)", True, (255, 0, 255))
        self.rect_text2 = self.image_text2.get_rect(center=(self.rect.width // 2, self.rect.height // 2 + 50*bili))

        self.yn = False # 先定义为False，后续在获胜时设置为True

        self.color_yes = (255, 0, 0)
        self.color_no = (0, 255, 0)
        self.color = self.color_no
    def update(self):
        if self.is_mouse_over():
            self.color = self.color_yes
        else:
            self.color = self.color_no

    def draw(self):
        pygame.draw.rect(self.image, self.color, ((0, 0), self.rect.size), border_radius=30)
        self.image.blit(self.image_text, self.rect_text)
        self.image.blit(self.image_text2, self.rect_text2)
        kuangjia.image.blit(self.image, self.rect)

    def set_player_id(self, player_id):
        self.image_text = self.font.render("玩家"+str(player_id)+"获胜了！", True, (255, 0, 255))
        self.rect_text = self.image_text.get_rect(center=(self.rect.width // 2, self.rect.height // 2 - 50*bili))
    def is_mouse_over(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= kuangjia.rect.left
        pos[1] -= kuangjia.rect.top
        return self.rect.collidepoint(pos)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.yn: # 只有在游戏胜利时才处理事件
            if self.is_mouse_over() and event.button == 1:
                button_music.play()
                返回关卡()
    def 重置(self):
        self.yn = False

# 增加敌方数量
def add_enemy_fish(enemy_fish_width_max, speed_range):
    # 随机选择一个路径创建一个敌鱼
    path = random.choice(enemy_fish_path_list)
    # 随机选择一个方向
    direction = random.choice(["left", "right"])
    # 获取玩家鱼的面积列表
    my_fish_size_list = []
    # 遍历玩家鱼组，获取所有玩家鱼的面积

    for x in my_fish_Group:
        # 获取玩家鱼的面积决定敌方鱼的参数
        my_fish_size_list.append(x.rect.width * x.rect.height)
    # 获取玩家鱼的最大面积
    my_fish_size_max = max(my_fish_size_list)
    # 列表删除，避免重复计算
    del my_fish_size_list[:]
    # 创建一个敌人
    enemy_fish = EnemyFish(path, direction, my_fish_size_max, enemy_fish_width_max, speed_range)
    # 添加到敌人组
    enemy_fish_Group.add(enemy_fish)
# 碰撞检测
def collide_check():
    current_time = pygame.time.get_ticks()

    # 我方鱼与敌方鱼精确碰撞检测
    for my_fish in my_fish_Group:
        # 我鱼与技能的碰撞
        collisions = pygame.sprite.spritecollide(
            my_fish,
            skill_Group,
            True,  # 删除技能
        )
        # 遍历碰撞的技能
        for skl in collisions:
            skill_music.play() # 播放技能音效
            if skl.name == skill_list[0]:
                size = 10000*bili
                my_fish.add_size(size)  # 加体重
                my_fish.add_积分(size/100)  # 加积分
                # print(skl.name, end=":")
            elif skl.name == skill_list[1]:
                my_fish.add_speed_fish(0.3) # 加鱼速度
                # print(skl.name, end=":")
            elif skl.name == skill_list[2]:
                my_fish.add_life(1) # 加生命值
                # print(skl.name, end=":")
            elif skl.name == skill_list[3]:
                my_fish.add_bullet_speed_load(0.05) # 加子弹加载速度
                # print(skl.name, end=":")
            elif skl.name == skill_list[4]:
                my_fish.add_bullet_number() # 加子弹数量
                # print(skl.name, end=":")
            # print(my_fish.skill)
        # 获取与当前玩家鱼碰撞的所有敌鱼, 默认返回敌方鱼精灵
        collisions = pygame.sprite.spritecollide(
            my_fish,
            enemy_fish_Group,
            False,  # 先不删除，需要先判断大小
            pygame.sprite.collide_mask
        )

        # 标记当前帧是否已经受到伤害
        took_damage_this_frame = False

        for enemy_fish in collisions:
            # 获取敌方鱼的大小（通过 rect.width 或 rect.size）
            enemy_size = enemy_fish.rect.width * enemy_fish.rect.height  # 敌方鱼面积
            my_size = my_fish.rect.width * my_fish.rect.height  # 我方鱼面积

            # 判断：只有我方鱼更大时才能吃掉敌人
            if my_size > enemy_size:
                # 吃鱼音效播放
                eat_muaic.play()
                enemy_fish.kill()  # 移除敌鱼
                my_fish.add_size(enemy_size) # 加体重
                # 更新我鱼积分
                my_fish.add_积分(enemy_size/100)
                # print(f"玩家{my_fish.player_id} 吃掉了一条敌鱼! 玩家大小: {my_size:.1f}, 敌人大小: {enemy_size:.1f}")
            elif len(my_fish.image_rect_life_list) > 0 and not took_damage_this_frame:
                # 检查是否在冷却期内, getattr 获取属性值，没有则默认0秒
                last_damage_time = getattr(my_fish, 'last_damage_time', 0)
                # 碰撞冷却时间（毫秒），避免短时间内重复扣血， 2秒无敌
                if current_time - last_damage_time >= 2000:
                    # 生命值减少1
                    my_fish.last_damage_time = current_time  # 记录受伤时间
                    took_damage_this_frame = True  # 标记本帧已受伤，避免多次扣血
                    # 安全地操作血条列表
                    if hasattr(my_fish, 'image_rect_life_list') and my_fish.image_rect_life_list:
                        my_fish.image_rect_life_list.pop(-1)
            # 如果血量为0，删除鱼对象
            elif len(my_fish.image_rect_life_list) <= 0:
                my_fish.kill()
        # 最后看看积分是否超过30000，超过就获胜
        if my_fish.skill["积分"] > 30000 and not game_win.yn: # 此处只能调用一次
            game_win.yn = True # 只能获胜一次
            game_win.set_player_id(my_fish.player_id)
    # 敌方鱼与我方子弹碰撞检测
    for bullets in bullet_list:
        # 获取与当前子弹碰撞的所有敌鱼, 默认返回敌方鱼精灵
        for bullet in bullets:
            collisions = pygame.sprite.spritecollide(
                bullet,
                enemy_fish_Group,
                True,  # 删除敌鱼
                pygame.sprite.collide_mask
            )
            for i in collisions:
                explosion_music.play() # 播放子弹爆炸音效
                bullet.kill() # 子弹也删除
                explosion_Group.add(Explosion(i.rect.center, (i.rect.size[1], i.rect.size[1])))
                # 随机是否添加技能，三分之一的概率
                skill_yn = random.choice([False, False, False, True, True])
                if skill_yn:
                    # 随机选择一个技能
                    skill_Group.add(AddSkill(random.choice(skill_list), i.rect.center))
# 更新绘制我鱼
def update_draw_my_fish():
    # 用zip函数同时遍历我鱼组和我鱼名称列表，更新和绘制
    for my_fish in my_fish_Group:
        if my_fish.alive():  # 只有活着的鱼才更新和绘制
            my_fish.update()
            my_fish.draw()
    for i in my_fish_name_list:
        i.update()
# 创建我鱼
def add_my_fish(num, path):
    global bullet_Group, bullet_list
    # print("添加我方鱼")
    # 获取敌鱼数量
    game_difficult.set_enemy_fish_number()
    # 子弹组
    bullet_list = []
    # 随机添加我鱼到我鱼组
    for i in range(1, num + 1):
        if len(fish_icon_list) > 0:
            my_fish = MyFish(i, path[i-1])
        else:
            my_fish = MyFish(i, "None")
        my_fish_Group.add(my_fish)
        # 添加我鱼名称到列表，获取第一个血条的中心坐标
        my_fish_name_list.append(MyFishName("玩家" + str(i), (my_fish.image_rect_life_list[1][1].centerx, my_fish.image_rect_life_list[1][1].centery-40*bili), my_fish.config['color'],  30*bili, i, my_fish.bullet_path, my_fish.ico_right_copy, my_fish.little_size))
        # 子弹精灵添加到列表中
        bullet_list.append(pygame.sprite.Group())
# 创建线程
class_thread = threading.Thread(target=ClassThread)
class_thread.daemon = True  # 主线程退出时，后台线程也退出
# 线程启动
class_thread.start()

def radius_image(radius, rect):
    # 2. 创建圆角遮罩（白色圆角矩形，透明背景）
    mask = pygame.Surface(rect.size, pygame.SRCALPHA)
    # 绘制中间矩形部分
    pygame.draw.rect(mask, (255, 255, 255, 255), pygame.Rect(0, 0, rect.width, rect.height).inflate(-2 * radius, 0))
    pygame.draw.rect(mask, (255, 255, 255, 255), pygame.Rect(0, 0, rect.width, rect.height).inflate(0, -2 * radius))
    # 绘制四个圆角（使用相对坐标）
    pygame.draw.ellipse(mask, (255, 255, 255, 255), pygame.Rect(0, 0, 2 * radius, 2 * radius))
    pygame.draw.ellipse(mask, (255, 255, 255, 255), pygame.Rect(rect.width - 2 * radius, 0, 2 * radius, 2 * radius))
    pygame.draw.ellipse(mask, (255, 255, 255, 255), pygame.Rect(0, rect.height - 2 * radius, 2 * radius, 2 * radius))
    pygame.draw.ellipse(mask, (255, 255, 255, 255), pygame.Rect(rect.width - 2 * radius, rect.height - 2 * radius, 2 * radius, 2 * radius))
    return mask

def 加载画面screen():
    kuangjia.image.fill((30, 30, 30))
    加载画面s.update()
    加载画面s.draw()

def 生日解锁screen():
    kuangjia.image.fill((255, 255, 255))
    # 眼球1
    eye_1.update()
    eye_2.update()
    # 眼球2
    eye_1.draw()
    eye_2.draw()
    # 记住密码
    password.update()
    password.draw()
    # 年
    clock1.update()
    clock1.draw()
    # 月
    clock2.update()
    clock2.draw()
    # 日
    clock3.update()
    clock3.draw()
    # 解锁按钮
    unlock.update()
    unlock.draw()

def 大厅选择screen():
    kuangjia.image.fill((255, 225, 158))
    if len(point_move_Group) < 400:
        point_move_Group.add(PointMove(random.randint(0, round(width)), -height, random.uniform(-3, 3), random.uniform(4, 7)))
    point_move_Group.update()
    point_move_Group.draw(kuangjia.image)
    button_1.update()
    button_2.update()
    button_3.update()
    button_4.update()
    if letter.book_update_yn == True or letter.book_speed != 0:
        letter.update()
        letter.draw()

def 听音乐screen():

    kuangjia.image.fill((230, 230, 230))

    # music_control.update()
    music_control.draw_button()

    playback_mode_up.update()
    change_bg_up.update()
    adjust_volume_up.update()

    adjust_volume.update()
    playback_mode.update()
    change_bg.update()

    left_control_button.update()
    center_control_button.update()
    right_control_button.update()

    music_control.draw_bgimg()
    music_control.draw_control()

    music_panel.update()

def 祝福语screen():
    kuangjia.image.fill(LILAC)
    if len(ballon_Group) < 10:
        width = random.randint(int(100*bili), int(200*bili))
        height = width * 2.3
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        speed = random.uniform(1.3, 4)
        centerx = random.choice([random.randint(0, round(kuangjia.rect.width*0.4)), random.randint(round(kuangjia.rect.width*0.6), kuangjia.rect.width)])
        ballon_Group.add(Balloon((centerx, int(kuangjia.rect.height+height)), speed, (width, height), (a, b, c)))
    ballon_Group.update()
    photo_greeting_Group.draw(kuangjia.image)
    ballon_Group.draw(kuangjia.image)
    cake.update()
    cake.draw()
    for i in flower_list:
        i.draw()

def 游戏1screen():
    # 绘制海洋背景图
    kuangjia.image.blit(game_screen.background_image, game_screen.background_rect)
    for i in game_number_list:
        # 显示人数选择
        i.update()
    game_speak.update()

def 游戏2screen():
    # 绘制海洋背景图
    kuangjia.image.blit(game_screen.background_image, game_screen.background_rect)
    choose_fish_Group.update()  # 显示玩家设置（选择鱼）
    choose_fish_Group.draw(kuangjia.image)

    game_difficult.update()
    game_difficult.draw()
    
    action_game.update()

def 游戏3screen():
    global mouse_stay_time, mouse_pos_center

    # ===================== 核心正确逻辑 =====================
    # 如果鼠标位置变了 → 立刻显示鼠标，重新计时
    if pygame.mouse.get_pos() != mouse_pos_center:
        mouse_pos_center = pygame.mouse.get_pos()  # 更新位置
        mouse_stay_time = pygame.time.get_ticks()  # 重置计时
        pygame.mouse.set_visible(True)  # 显示鼠标

    # 如果鼠标位置没变，且超过 500ms → 隐藏
    else:
        if pygame.time.get_ticks() - mouse_stay_time > 500:
            pygame.mouse.set_visible(False)

    if button_last.is_mouse_over():
        button_last.image.set_alpha(255)
    else:
        button_last.image.set_alpha(0)
        
    # 绘制海洋背景
    try:
        kuangjia.image.blit(game_bgimg, (0, 0))
    except:
        kuangjia.image.fill((30, 30, 30))
    # 添加敌鱼
    if (len(enemy_fish_Group) < game_difficult.enemy_number) and len(my_fish_Group) > 0:
        add_enemy_fish(game_difficult.enemy_width_max_min, game_difficult.enemy_speed_range) # 根据难易程度调整敌鱼大小范围与数量

    # 刷新我方鱼的位置与显示
    update_draw_my_fish()

    # 刷新敌方鱼的位置与显示
    enemy_fish_Group.update()
    enemy_fish_Group.draw(kuangjia.image)

    # 刷新子弹的显示
    for i in bullet_list:
        i.update()
        i.draw(kuangjia.image)

    # 刷新技能的显示
    skill_Group.update()
    skill_Group.draw(kuangjia.image)

    # 刷新爆炸的显示
    explosion_Group.update()
    explosion_Group.draw(kuangjia.image)

    # 碰撞检测
    collide_check()

    # 刷新游戏胜利的显示
    if game_win.yn:
        game_win.update()
        game_win.draw()

def 音乐暂停():
    if music_panel.当前播放音乐 != None:
        music_panel.当前播放音乐.stop()
        music_panel.当前播放音乐.close()
    music_panel.当前播放音乐 = None

def 关卡1重置():
    pass

def 关卡2重置():
    pass
    """clock1.重置()
    clock2.重置()
    clock3.重置()"""

def 关卡3重置():
    letter.重置()

def 关卡4重置():
    pass

def 关卡5重置():
    ballon_Group.empty() # 重置气球
    cake.重置()

def 关6重置():
    game_screen.重置()
    game_difficult.重置()  # 重置游戏难度

def 关7重置():
    pass

def 关8重置():
    enemy_fish_Group.empty() # 重置敌鱼
    my_fish_Group.empty() # 重置我鱼
    my_fish_name_list.clear() # 重置我鱼信息列表
    bullet_list.clear() # 重置子弹列表
    game_win.重置() # 重置游戏胜利的显示

def 当前关卡():
    global 当前关卡s
    if 当前关卡s[0] == True:
        return 1
    elif 当前关卡s[1] == True:
        return 2
    elif 当前关卡s[2] == True:
        return 3
    elif 当前关卡s[3] == True:
        return 4
    elif 当前关卡s[4] == True:
        return 5
    elif 当前关卡s[5] == True:
        return 6
    elif 当前关卡s[6] == True:
        return 7
    elif 当前关卡s[7] == True:
        return 8
    else:
        return 0
hhh = 0
def 切换关卡(目标关卡):
    global 当前关卡s, hhh
    for i in range(0, len(当前关卡s)):  # 0~5
        if i == 目标关卡 - 1:
            当前关卡s[i] = True
            if i == 5:
                # 停止音乐播放
                if center_control_button.is_playing == True:
                    hhh = 1
                    center_control_button.pause()
                else:
                    hhh = 0
                # 开始播放鱼游戏的新背景音乐
                game_screen.play_music()
        else:
            当前关卡s[i] = False

def 返回关卡():
    current_guan_qia = 当前关卡()
    if current_guan_qia > 1:
        if current_guan_qia == 2:
            关卡1重置()
            关卡2重置()
        elif current_guan_qia == 3:
            关卡2重置()
            关卡3重置()
            point_move_Group.empty()  # 只有返回第2关时，重置点移动
        elif current_guan_qia == 7:
            关6重置()# 重置游戏选择模式数据
        elif current_guan_qia == 8:
            # 将鼠标显示
            pygame.mouse.set_visible(True)
            # 将返回按钮的透明度设置为255，使按钮显示
            button_last.image.set_alpha(255)
            关8重置()# 重置游戏数据
        # 如果是第4关、第5关、第6关，需要重置第3关的数据
        if current_guan_qia == 4 or current_guan_qia == 5 or current_guan_qia == 6:
            关卡3重置()
            当前关卡s[2] = True
            当前关卡s[3] = False
            当前关卡s[4] = False
            当前关卡s[5] = False
            if current_guan_qia == 4:
                关卡4重置()
            elif current_guan_qia == 5:
                关卡5重置()
            elif current_guan_qia == 6:
                # 先尝试将旧的鱼背景音乐停止
                try:
                    # 停止音乐播放
                    # print(111)
                    if hhh == 1:
                        center_control_button.play()
                    game_screen.stop_music()
                except:
                    # print(555)
                    pass
                关6重置()
        # 只有不在第4关、第5关、第6关，才返回直接上一级
        else:
            当前关卡s[current_guan_qia - 1] = False
            当前关卡s[current_guan_qia - 2] = True
    elif current_guan_qia == 1:
        保存数据()
        pygame.quit()
        sys.exit()

def 保存数据():
    if password.yn and clock1.return_value() == 2006 and clock2.return_value() == 6 and clock3.return_value() == 8:
        password.save_password("200668")
    else:
        password.save_password("False")
    # 如果数量不为零，才保存背景图片
    if change_bg_up.number != 0:
        music_control.save_bgimg(music_control.get_bgimg_number())
    music_control.save_play_mode()
当前关卡s = [True, False, False, False, False, False, False, False]

while True:
    if (当前关卡() == 4):
        music_panel.不滑动()

    kuangjia.image.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            保存数据()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            保存数据()
            pygame.quit()
            sys.exit()

        button_last.handle_event_last(event) # 处理返回按钮事件

        if 当前关卡() == 1:
            加载画面s.handle_event(event)
        elif 当前关卡() == 2:
            clock1.handle_event(event)
            password.handle_event(event)
        elif 当前关卡() == 3:
            button_1.handle_event(event)
        elif 当前关卡() == 4:
            # 每个音乐独立的handle_event
            for i in 音乐按钮总和:
                i.handle_event(event)
            music_control.handle_event(event)
            left_control_button.handle_event(event)
            center_control_button.handle_event(event)
            right_control_button.handle_event(event)

            playback_mode.handle_event(event)
            change_bg.handle_event(event)
            adjust_volume.handle_event(event)

            playback_mode_up.handle_event(event)
            change_bg_up.handle_event(event)
            adjust_volume_up.handle_event(event)

            music_panel.handle_event(event)# 放后面避免冲突
        elif 当前关卡() == 5:
            pass
        elif 当前关卡() == 6:
            for i in game_number_list:
                i.handle_event(event)
        elif 当前关卡() == 7:
            for set in choose_fish_Group:
                set.handle_event(event)
            action_game.handle_event(event)
            game_difficult.handle_event(event)
        elif 当前关卡() == 8:
            # 循环便利我方鱼组，处理事件事件
            for i in my_fish_Group:
                i.handle_event(event)
            game_win.handle_event(event)

    if 当前关卡() == 1:
        加载画面screen()
    elif 当前关卡() == 2:
        生日解锁screen()
    elif 当前关卡() == 3:
        大厅选择screen()
    elif 当前关卡() == 4:
        听音乐screen()
    elif 当前关卡() == 5:
        祝福语screen()
    elif 当前关卡() == 6:
        游戏1screen()
    elif 当前关卡() == 7:
        游戏2screen()
    elif 当前关卡() == 8:
        游戏3screen()

    # 如果当前关卡大于1，才更新音乐自动播放下一首，无论是否在音乐关卡
    if 当前关卡() > 1:
        music_control.update()

    # 返回键更新
    button_last.update()
    screen.blit(kuangjia.image, kuangjia.rect)

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)