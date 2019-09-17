import sys
import pygame

#监视屏幕和鼠标事件
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship,people):
    """更新屏幕上的图像，并切换到新图像"""
    #每次循环时都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    people.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()