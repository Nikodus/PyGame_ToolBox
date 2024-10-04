import time
from pygame import font
import pygame


class Defines:
    gray = (150, 150, 150)
    light_gray = (200, 200, 200)
    dark_gray = (100, 100, 100)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    magenta = (255, 0, 255)
    cyan = (0, 255, 255)
    background = (40, 40, 40)
    font.init()
    big_text_font = font.Font(None, 64)
    medium_text_font = font.Font(None, 32)
    small_text_font = font.Font(None, 24)

    def dynamic_font(self,rectange:pygame.rect.Rect, Text:str, border:int = 0):
        width = rectange.width - border
        height = rectange.height - border
        result_font = font.Font(None,100)
        i = 99
        size = result_font.size(Text)
        while (width-size[0]<0 or height-size[1]<0) and i>1:
            result_font = font.Font(None,i)
            size = result_font.size(Text)
            i-=1
        return font.Font(None,i+1)



    def dropdown_animation(self,rectangle:pygame.rect.Rect,window:pygame.display,color:pygame.color,new_height:int):
        height = rectangle.height

        for i in range(new_height-height):
            rectangle.height = height+i
            pygame.draw.rect(window,color,rectangle)
            time.sleep(0.001)

    # TODO Animation Testen (Später) (Möglicherweise umprogrammieren)


# TODO Animationen wie Dropdown Fade-in oder Fade-out implementieren
