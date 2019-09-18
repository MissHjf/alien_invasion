import sys
import pygame
from settings import Settings
from ship import Ship
from people import People
import game_functions as gf

def run_game():
    #初始化一个游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship=Ship(screen)
    people=People(screen)

    #开始游戏的主循环
    while True:

        #监视屏幕和鼠标和键盘事件
        gf.check_events(ship)
        ship.update()
        #更新屏幕上的图像，并切换到新图像
        gf.update_screen(ai_settings,screen,ship,people)


run_game()