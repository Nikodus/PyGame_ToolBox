import pygame
from PyGame_Toolbox.Objects import Object
from PyGame_Toolbox.defines import *

# TODO TextBox fertigstellen
class TextBox(Object):
    __Rectangle = None


    def __init__(self, x: int, y: int, width: int, height: int,font: pygame.font = fonts.medium_text_font,
                 text_color: pygame.color = colors.white):
        self.__Rectangle = pygame.rect


    def __draw__(self, window):
        super().__draw__(window)

    def __left_click_events__(self):
        return super().__left_click_events_rect__(self.__Rectangle)

    def __right_click_events__(self):
        return super().__right_click_events_rect__(self.__Rectangle)

    def __middle_click_events__(self):
        return super().__middle_click_events_rect__(self.__Rectangle)
