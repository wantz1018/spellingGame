import random
import sys
import time

import pygame
import requests
from bs4 import BeautifulSoup

print('\033[33m')
time.sleep(0.5)
print('欢迎来到单词的世界!')
time.sleep(0.5)
print('在这里，你将用给定的字母拼出单词，单词越长，得分越高')
time.sleep(0.5)
print('现在好好享受单词的魅力吧')
time.sleep(0.5)
print('\033[0m')
input('输入go开始游戏')
time.sleep(0.5)
# 游戏模块
level = int(input('请选择难度（1~10）,低于1视为1，高于10视为10.特别的，输入0结束游戏:'))
if level < 1 and level != 0:
    level = 1
elif level > 10:
    level = 10
elif level == 0:
    sys.exit(0)
# 初始字母数
start_num = int(26/level)
# 当前可用字母存放的地方
letter = []
# 已经拼写出来的单词存放的地方
words = []
# 26个字母列表
letter_list = []
# 元音字母列表
yuan_yin = ['a', 'o', 'i', 'e', 'u']
# 分数
score = 0
# 游戏是否继续
game = True
# 检查次数
check_no = 1
# 程序暂停
game_exit = 1
# 当前翻译
one = set()
# 字母修改次数
re_num = 11 - level
for i in range(97, 123):    # 生成含有26个英文字母的列表
    letter_list.append(chr(i))
# 随机放入start_num个字母
for i in range(1, start_num):
    x = random.randrange(97, 123)
    letter.append(chr(x))
    x = random.randrange(97, 123)
    letter.append(chr(x))
    x = random.randrange(97, 123)
    letter.append(chr(x))
    x = random.randrange(97, 123)
    letter.append(chr(x))
for n in range(1, start_num):
    y = random.randrange(1, len(yuan_yin))
    letter.append(yuan_yin[y-1])
# 辅音字母列表
fu_yin = letter_list
for an in yuan_yin:
    if an in fu_yin:
        fu_yin.remove(str(an))
# 单词文档初始化
    file = open('all_my_word.txt', mode='w')
    # file.write('\n')
# 当前记录的单词
now_danci = ''


def find_word(word):    # 定义查找单词函数
    try:
        url = 'http://dict.youdao.com/w/eng/{}/#keyfrom=dict2.index'.format(word)
        website = requests.get(url).text
        global one
        global transform
        html = BeautifulSoup(website, 'lxml')
        trans = html.find(class_='trans-container')
        if str(type(trans)) == 'NoneType':
            exit(0)
        else:
            transform = trans.find_all('li')
        if str(type(transform)) == 'NoneType':
            exit(0)
        for sa in transform:
            if type != 'NoneType':
                print('\033[36m' + str(sa.string) + '\033[0m')
                write_in_file(dan_ci, str(sa.string))
            else:
                return 0
        if len(transform) > 0:
            return word
        else:
            return 0
    except Exception as e:
        print('出错啦！')
        print(e)


def write_in_file(now_word, now_trans):    # 将结果写入文本文档中
    global now_danci
    file_handle = open('all_my_word.txt', mode='a')
    if now_word != now_danci:
        file_handle.write(now_word + '\n')
        now_danci = now_word
    file_handle.write(str(now_trans) + '\n')


def show_file():    # 将文档中的内容展示出来
    file_show = open('all_my_word.txt', mode='r')
    my = file_show.read()
    print('\033[36m' + "您拼写出来的单词以及对应意思为：\n")
    time.sleep(0.5)
    print('\033[34m' + my + '\033[0m')
    time.sleep(0.6)


def write():    # 输入单词并检查函数
    global game_exit
    new_letter = letter
    fre = []
    # 检查是否在给出的字母表里
    for zi_mu in dan_ci:
        if zi_mu not in new_letter:
            print('字母列表中的字母{}数量不足'.format(zi_mu))
            for point in fre:
                letter.append(point)
            return 0
        else:
            new_letter.remove(zi_mu)
            fre.append(zi_mu)
    if dan_ci in words:
        print('单词已经拼写过了哦，请重新输入：')
        for yy in dan_ci:
            letter.append(yy)
        return 0
    return dan_ci


def score_add(kg):
    # 积分程序
    score_now = 0
    if kg != 0 and dan_ci not in words:
        score_now = int(len(dan_ci) - 1)
        words.append(str(dan_ci))
        if score_now == 0:
            print('单个字母不计积分！')
            return 0
        elif score_now == 1:
            print('\033[31m两个字母的单词不计分\033[0m')
            return 0
        else:
            print('恭喜获得{}分'.format(score_now - 1))
            for poi in dan_ci:
                if str(poi) in letter:
                    letter.remove(str(poi))
            for num in range(1, len(dan_ci)):
                nm_e = random.randrange(97, 123)
                print('\033[32m获得字母{}\033[0m'.format(chr(nm_e)))
                letter.append(chr(nm_e))
            return score_now
    elif kg == 0:
        print('抱歉没找到这个单词:(')
        for sa in dan_ci:
            letter.append(sa)
        score_now = 0
    return score_now


def end():   # 游戏结束并进行结算
    print('游戏结束！')
    print('您总共拼写出{}个单词'.format(len(words)))
    print('获得分数：{}分'.format(score))
    if input('是否查看所拼写的单词(y/n)') == 'y':
        for all_word in words:
            print('\033[31m' + all_word + '\033[0m', end=' ')
        print('\n')
        show_file()
    sys.exit(0)


def add_yuan():     # 检测列表中是否含有元音字母
    for yy in yuan_yin:
        if yy in letter:
            return 1
    return 0


def print_letter():     # 打印当前可用字母
    print('\033[34m当前可用字母列表：\033[0m')
    na = -1
    bian_chang = int(pow(len(letter), 0.5))
    for hang in range(0, bian_chang + 1):
        for lie in range(0, bian_chang + 1):
            na += 1
            if na < len(letter):
                print(letter[na], end=' ')
        print()


def word_replace():  # 单词替换程序
    global score
    global re_num
    if score >= 2:
        mode = str(input('替换：1，增加：2，减少：3'))
        if mode == '1':
            print('替换一个元音需2积分，替换一个辅音需4积分')
            re_word = input('请输入需要替换的字母：')
            if re_word in letter:
                if re_word in yuan_yin:
                    if score >= 2:
                        score = score - 2
                        print('使用成功！')
                        letter.remove(re_word)
                        re_t = yuan_yin[random.randrange(0, 5)]
                    else:
                        print('对不起，您的积分不足！')
                        print('当前积分:{}'.format(score))
                else:
                    if score >= 4:
                        score = score - 4
                        print('使用成功！')
                        letter.remove(re_word)
                        re_t = fu_yin[random.randrange(0, 21)]
                        letter.append(re_t)
                    else:
                        print('对不起，您的积分不足！')
            else:
                print('对不起，您输入的字母不在已有字母列表中')
            print('成功将' + str(re_word) + '替换成' + str(re_t))
        elif mode == '2':
            print('随机增加一个元音需要4积分，随机增加一个元音需要2积分')
            kind = input('随机增加元音：1，随机增加辅音：2')
            if kind == '1':
                add = random.randrange(0, 5)
                add_one = yuan_yin[add]
                print('成功增添字母{}'.format(add_one))
                letter.append(add_one)
                score -= 4
            elif kind == '2':
                add = random.randrange(0, 21)
                add_one = fu_yin[add]
                print('成功增添字母{}'.format(add_one))
                letter.append(add_one)
                score -= 2
        elif mode == '3':
            print('删除一个元音需要4积分，删除一个辅音需要2积分')
            kind_1 = input('请输入要删除的字母：')
            if kind_1 in letter:
                if kind_1 in yuan_yin:
                    if score >= 2:
                        print('删除成功！')
                        score -= 2
                        letter.remove(str(kind_1))
                    else:
                        print('对不起，您的积分不足')
                if kind_1 in fu_yin:
                    if score >= 4:
                        print('删除成功！')
                        letter.remove(str(kind_1))
                        score -= 4
                    else:
                        print('对不起，您的积分不足')
            else:
                print('请正确输入！（本次扣除1积分）')
                score -= 1
        else:
            return 0
    elif re_num >= 0:
        print('由于积分不足，使用修改次数')
        print('当前积分外可用修改次数:{}次'.format(re_num))
        mode = str(input('替换：1，增加：2，减少：3'))
        if mode == '1':
            re_word = input('请输入需要替换的字母：')
            if re_word in letter:
                if re_word in yuan_yin:
                    print('使用成功！')
                    letter.remove(re_word)
                    letter.append(yuan_yin[random.randrange(0, 5)])
                    re_num -= 1
                else:
                    print('使用成功！')
                    letter.remove(re_word)
                    letter.append(fu_yin[random.randrange(0, 21)])
                    re_num -= 1
            else:
                print('对不起，您输入的字母不在已有字母列表中')
        elif mode == '2':
            kind = input('随机增加元音：1，随机增加辅音：2')
            if kind == '1':
                add = random.randrange(0, 5)
                u = yuan_yin[add]
                print('成功增加{}'.format(u))
                letter.append(u)
                re_num -= 1
            elif kind == '2':
                add = random.randrange(0, 21)
                letter.append(fu_yin[add])
                re_num -= 1
            elif kind == '':
                return 0
        elif mode == '3':
            kind_1 = input('输入要删除的字母')
            if kind_1 in letter:
                if kind_1 in yuan_yin:
                    print('删除成功！')
                    letter.remove(str(kind_1))
                    re_num -= 1
                if kind_1 in fu_yin:
                    print('删除成功！')
                    letter.remove(str(kind_1))
                    re_num -= 1
            else:
                print('请正确输入！（本次扣除1积分）')
                score -= 1
                re_num -= 1
        else:
            print('请正确输入！')
            return 0
    else:
        print('对不起，您的积分不足')
    print('当前积分{}'.format(score))
    time.sleep(1)
    print('当前积分外可用修改次数：{}次'.format(re_num))


def screen(word_in):   # 将内容更新到屏幕上
    pygame.init()  # 初始化
    icon = pygame.image.load("letters//English_logo.png")  # 创立一个图片对象
    pygame.display.set_icon(icon)  # 将这个图片设为游戏图标
    vInfo = pygame.display.Info()  # 当前操作系统的屏幕参数
    size = width, height = 600, 400  # 赋值参数
    BLACK = 0, 0, 0
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)  # 窗口大小
    pygame.display.set_caption("单词挑战")  # 窗口名字
    letter = pygame.image.load("letters//letter_{}.png".format(str(word_in)))  # 导入图片
    letter_pic = letter.get_rect()
    fps = 30  # 定义刷新率
    fclock = pygame.time.Clock()  # 创立一个time对象，用于控制时间
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # 增加退出键
                    sys.exit()
        screen.blit(letter, (200, 100))
        pygame.display.update()  # 刷新窗口变化的地方
        fclock.tick(fps)  # 窗口每秒刷新fps次
        screen.fill('gray')


while game:     # 主程序
    # screen("X")
    if add_yuan() == 0:
        letter.append(yuan_yin[random.randrange(0, 5)])
        print('列表中已没有元音字母，增加一个元音字母！')
    print_letter()
    print('\033[32m输入‘1’进行字母更改\033[0m')
    print('\033[32m输入“0”结束游戏\033[0m')
    print('\033[32m直接按回车随机添加一个字母，此操作需要有效的更改次数或者足够积分\033[0m')
    # 输入单词
    dan_ci = str(input('请输入单词：'))
    if dan_ci == '0':
        game = False
        end()
    elif dan_ci == '1':
        word_replace()
    elif dan_ci == '':
        if score > 0:
            score -= 1
            ins = random.randrange(97, 123)
            letter.append(str(chr(ins)))
            print('增添单词{}'.format(chr(ins)))
            print('使用1积分，当前积分{}分'.format(score))
        elif re_num > 0:
            re_num -= 1
            ins = random.randrange(97, 123)
            letter.append(str(chr(ins)))
            print('增添单词{}'.format(chr(ins)))
            print('使用积分外次数，当前可用积分外次数{}次'.format(re_num))
        else:
            print('\033[31m对不起，您的更改次数用完了\033[0m')
    else:
        # 执行检查程序
        # write()
        if write() != 0 and game_exit == 1:
            # 执行查找程序
            open_or_not = find_word(dan_ci)
            # print(one)
            # 执行积分程序
            # score_add()
            score = score + score_add(open_or_not)
            print('当前积分{}'.format(score))
        else:
            pass
    if len(letter) == 0 or len(letter) == 1:
        print('恭喜你拼写完所有字母！')
        end()