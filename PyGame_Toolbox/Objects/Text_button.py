import pygame
from PyGame_Toolbox.Objects import Object
from PyGame_Toolbox.defines import *


class Text_button(Object):
    __Rectangle = None
    __Button_color = None
    __Text = None
    __Text_color = None
    __Font = None


    # TODO auf Pygame rect umbauen

    def __init__(self, rect:pygame.rect, text: str = "Button",
                 font: pygame.font = fonts.medium_text_font, button_color: pygame.color = colors.gray,
                 text_color: pygame.color = colors.white):
        self.__Rectangle = rect
        self.__Text = text
        self.__Font = font
        self.__Button_color = button_color
        self.__Text_color = text_color

    def __draw__(self, window: pygame.display):
        pygame.draw.rect(window, self.__Button_color, self.__Rectangle)
        button_text = self.__Font.render(self.__Text, True, self.__Text_color)
        text_rect = button_text.get_rect(center=self.__Rectangle.center)
        window.blit(button_text, text_rect)

    def __left_click_events__(self):
        return super().__left_click_events_rect__(self.__Rectangle)

    def __right_click_events__(self):
        return super().__right_click_events_rect__(self.__Rectangle)

    def __middle_click_events__(self):
        return super().__middle_click_events_rect__(self.__Rectangle)

    def getRectangle(self):
        return self.__Rectangle

    def setButtonColor(self, color: pygame.color):
        self.__Button_color = color

    def setButtonTextColor(self, color: pygame.color):
        self.__Text_color = color

    def setHeight(self,new_height:int ):
        self.__Rectangle.height = new_height

    def setWidth(self, new_width: int):
        self.__Rectangle.width = new_width