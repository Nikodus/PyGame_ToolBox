import pygame
from PyGame_Toolbox.Objects import Object
from PyGame_Toolbox.defines import *

# TODO eventuelles Mergen mit dem Text_button Object.

class Invisible_Button(Object):
    __Rectangle = None
    __showButton = 0

    def __init__(self, x: int, y: int, width: int, height: int):
        self.__Rectangle = pygame.Rect(x, y, width, height)

    def __draw__(self, window):
        if self.__showButton == 1:
            pygame.draw.rect(window, colors.black, self.__Rectangle)
            button_text = fonts.dynamic_font(self.__Rectangle, "Here").render("Here", True, colors.white)
            text_rect = button_text.get_rect(center=self.__Rectangle.center)
            window.blit(button_text, text_rect)

    def __left_click_events__(self):
        return super().__left_click_events_rect__(self.__Rectangle)

    def __right_click_events__(self):
        return super().__right_click_events_rect__(self.__Rectangle)

    def __middle_click_events__(self):
        return super().__middle_click_events_rect__(self.__Rectangle)

    def showButton(self):
        self.__showButton = 1
