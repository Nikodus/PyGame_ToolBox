import pygame
from PyGame_Toolbox.Objects import Object
from PyGame_Toolbox.defines import *

class Label(Object):
    __Label_rect = None
    __Text = None
    __Text_font = None
    __Text_color = None


    def __init__(self, x: int, y: int, Text_font: pygame.font, Text: str = "Label",
                 Text_color: pygame.color = colors.white):
        self.__Text = Text
        self.__Text_font = Text_font
        self.__Label_rect = pygame.Rect(x, y, Text_font.size(Text)[0], Text_font.size(Text)[1])
        self.__Text_color = Text_color

    def __draw__(self, window):
        button_text = self.__Text_font.render(self.__Text, True, self.__Text_color)
        text_rect = button_text.get_rect(center=self.__Label_rect.center)
        window.blit(button_text, text_rect)

    def __left_click_events__(self):
        return super().__left_click_events_rect__(self.__Label_rect)

    def __right_click_events__(self):
        return super().__right_click_events_rect__(self.__Label_rect)

    def __middle_click_events__(self):
        return super().__middle_click_events_rect__(self.__Label_rect)
