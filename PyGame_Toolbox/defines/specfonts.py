from pygame import font
import pygame


class specfonts:
    def __init__(self):
        font.init()

    def dynamic_font(self,rectange: pygame.rect.Rect, Text: str, border: int = 0):
        width = rectange.width - border
        height = rectange.height - border
        result_font = font.Font(None, 100)
        i = 99
        size = result_font.size(Text)
        while (width - size[0] < 0 or height - size[1] < 0) and i > 1:
            result_font = font.Font(None, i)
            size = result_font.size(Text)
            i -= 1
        return font.Font(None, i + 1)


