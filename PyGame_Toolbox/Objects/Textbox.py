from enum import Enum

import pygame
from PyGame_Toolbox.Objects import Object
from PyGame_Toolbox.defines import *

class Modes(Enum):
    Numeric = 0
    Text = 1
    Any = 2

# TODO TextBox fertigstellen
class TextBox(Object):
    __Rectangle = None
    __text = []
    __selected = False
    __Font = None
    __Text_color = None
    __textbox_color = None
    __textbox_color_selected = None
    __max_chars = None
    __text_mode = None


    def __init__(self, x: int, y: int, width: int, height: int,font: pygame.font = fonts.medium_text_font, max_chars: int = 5, text_mode :Enum = Modes.Any,
                 textbox_color: pygame.color = colors.gray,textbox_color_selected: pygame.color = colors.light_gray,
                 text_color: pygame.color = colors.white,):
        self.__Rectangle = pygame.Rect(x,y,width,height)
        self.__Font = font
        self.__Text_color = text_color
        self.__textbox_color = textbox_color
        self.__textbox_color_selected = textbox_color_selected
        self.__max_chars = max_chars
        self.__text_mode = text_mode


    def __draw__(self, window):
        if self.__selected:
            pygame.draw.rect(window, self.__textbox_color_selected, self.__Rectangle)
        else:
            pygame.draw.rect(window, self.__textbox_color, self.__Rectangle)
        button_text = self.__Font.render(self.listtostr(self.__text), True, self.__Text_color)
        text_rect = button_text.get_rect(center=self.__Rectangle.center)
        window.blit(button_text, text_rect)

    def __left_click_events__(self):
        return super().__left_click_events_rect__(self.__Rectangle)

    def __right_click_events__(self):
        return super().__right_click_events_rect__(self.__Rectangle)

    def __middle_click_events__(self):
        return super().__middle_click_events_rect__(self.__Rectangle)

    def leftonclick(self):
        if not self._Object__disable:
            self.setselect(True)
            return self._Object__Left_onclick_fun(*self._Object__Left_onclick_fun_param)
        return None
    def leftoffclick(self):
        if not self._Object__disable:
            self.setselect(False)
            return self._Object__Left_offclick_fun(*self._Object__Left_offclick_fun_param)
        return None

    def __key_down_events__(self,event: pygame.event):
        if self.__selected:
            text = event.unicode
            text = str(text)

            if self.__text_mode == Modes.Any:
                if text.isprintable():
                    if len(self.__text) < self.__max_chars:
                        self.__text.append(text)

            if self.__text_mode == Modes.Text:
                if text.isalpha():
                    if len(self.__text) < self.__max_chars:
                        self.__text.append(text)

            if self.__text_mode == Modes.Numeric:
                if text.isdigit():
                    if len(self.__text) < self.__max_chars:
                        self.__text.append(text)

            if text == "\x08":
                try:
                    self.__text.pop()
                except:
                    None

            if text == "\r":
                self.__return_event()

    def __return_event(self):
        print(self.__text)
        self.clear_text()

    def setselect(self, newvalue: bool):
        self.__selected = newvalue

    def clear_text(self):
        self.__text.clear()

    def listtostr(self, inputlist:list):
        outputstr = ""
        i = 0
        while i< len(inputlist):
            outputstr = outputstr + inputlist[i]
            i+=1
        return outputstr

