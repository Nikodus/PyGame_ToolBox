import pygame
from PyGame_Toolbox.Objects.Text_button import Text_button
from PyGame_Toolbox.Objects import Object
from PyGame_Toolbox.defines import *


class Toolbar(Object):
    __Button_list = None
    __height = None
    __width = None
    __bar_color = None
    __text_border = None
    __option_height = None

    def __init__(self, height: int, text_border: int = 20, option_height: int = 20,
                 bar_color: pygame.color = colors.gray):
        self.__Button_list = []
        self.__height = height
        self.__width = pygame.display.get_window_size()[0]
        self.__bar_color = bar_color
        self.__bar_rect = pygame.Rect(0, 0, self.__width, self.__height)
        self.__text_border = text_border
        self.__option_height = option_height
        self.__specfonts = specfonts()

    def __draw__(self, window):
        self.__bar_rect = pygame.Rect(0, 0, self.__width, self.__height)
        pygame.draw.rect(window, self.__bar_color, self.__bar_rect)
        for cat in self.__Button_list:
            cat[0].__draw__(window)
            if cat[1] == 1:
                for option in cat:
                    if option == cat[0]:
                        continue
                    if option == cat[1]:
                        continue
                    option.__draw__(window)

    # TODO offclick Funktion verbessern

    def __left_click_events__(self):
        result = False
        for cat in self.__Button_list:
            if cat[0].__left_click_events__():
                result = True
            if cat[1] == 1:
                for option in cat:
                    if option == cat[0]:
                        continue
                    if option == cat[1]:
                        continue
                    if option.__left_click_events__():
                        result = True
        return result

    def __right_click_events__(self):
        result = False
        for cat in self.__Button_list:
            if cat[0].__right_click_events__():
                result = True
            if cat[1] == 1:
                for option in cat:
                    if option == cat[0]:
                        continue
                    if option == cat[1]:
                        continue
                    if option.__right_click_events__():
                        result = True
        return result

    def __middle_click_events__(self):
        result = False
        for cat in self.__Button_list:
            if cat[0].__middle_click_events__():
                result = True
            if cat[1] == 1:
                for option in cat:
                    if option == cat[0]:
                        continue
                    if option == cat[1]:
                        continue
                    if option.__middle_click_events__():
                        result = True
        return result

    def add_Category(self, Text: str = "Category"):
        list_size = len(self.__Button_list)
        category_font = self.__specfonts.dynamic_font(self.__bar_rect, Text, self.__text_border)

        cat_y = 0
        cat_height = self.__bar_rect.height
        cat_width = category_font.size(Text)[0] + 10

        if list_size == 0:
            optionlist = [Text_button(pygame.Rect(10, cat_y, cat_width, cat_height), Text, category_font), 0]
            optionlist[0].setLeftonClickFunction(self.__onclickCategory__, optionlist)
            optionlist[0].setLeftoffClickFunction(self.__offclickCategory__, optionlist)
            self.__Button_list.append(optionlist)

        else:
            cat_x = self.__Button_list[list_size - 1][0].getRectangle()
            optionlist = [
                Text_button(pygame.Rect(cat_x.x + cat_x.width + 5, cat_y, cat_width, cat_height), Text, category_font),
                0]
            optionlist[0].setLeftonClickFunction(self.__onclickCategory__, optionlist)
            optionlist[0].setLeftoffClickFunction(self.__offclickCategory__, optionlist)
            self.__Button_list.append(optionlist)

    def __onclickCategory__(self, optionlist: list):
        if optionlist[1] == 0:
            optionlist[1] = 1
            optionlist[0].setButtonColor(colors.dark_gray)
        else:
            optionlist[1] = 0
            optionlist[0].setButtonColor(colors.gray)

    def __offclickCategory__(self, optionlist: list):
        optionlist[1] = 0
        optionlist[0].setButtonColor(colors.gray)

    def add_Option(self, index: int, Text: str = "Option"):
        if index > len(self.__Button_list):
            raise IndexError
        if self.__Button_list == []:
            raise RuntimeError

        cat_rect = self.__Button_list[index][0].getRectangle()
        dummy_rect = pygame.Rect(0, 0, cat_rect.width, self.__option_height + 3)
        opt_font = self.__specfonts.dynamic_font(dummy_rect, Text, 5)

        opt_x = self.__Button_list[index][0].getRectangle().x
        opt_width = self.__Button_list[index][0].getRectangle().width
        opt_height = self.__option_height + 10

        last_index = len(self.__Button_list[index]) - 1

        if last_index == 1:
            opt_y = self.__bar_rect.height
            self.__Button_list[index].append(
                Text_button(pygame.Rect(opt_x, opt_y, opt_width, opt_height), Text, opt_font))

        else:
            opt_y = self.__Button_list[index][last_index].getRectangle().y + self.__Button_list[index][
                last_index].getRectangle().height
            self.__Button_list[index].append(
                Text_button(pygame.Rect(opt_x, opt_y, opt_width, opt_height), Text, opt_font))

    def Option_set_leftClick_Function(self, category_index: int, option_index: int, function, *parameter):
        if category_index > len(self.__Button_list):
            raise IndexError
        if option_index > len(self.__Button_list[category_index]):
            raise IndexError
        if self.__Button_list == []:
            raise RuntimeError
        option_index += 2
        self.__Button_list[category_index][option_index].setLeftonClickFunction(function, *parameter)

    def Option_set_rightClick_Function(self, category_index: int, option_index: int, function, *parameter):
        if category_index > len(self.__Button_list):
            raise IndexError
        if option_index > len(self.__Button_list[category_index]):
            raise IndexError
        if self.__Button_list == []:
            raise RuntimeError
        option_index += 2
        self.__Button_list[category_index][option_index].setRightonClickFunction(function, *parameter)

    def Option_set_middleClick_Function(self, category_index: int, option_index: int, function, *parameter):
        if category_index > len(self.__Button_list):
            raise IndexError
        if option_index > len(self.__Button_list[category_index]):
            raise IndexError
        if self.__Button_list == []:
            raise RuntimeError
        option_index += 2
        self.__Button_list[category_index][option_index].setMiddleonClickFunction(function, *parameter)



    # TODO Option Objects für Toolbox


class Option(Object):
    def __init__(self):
        super()

    def __draw__(self, window):
        None

    def __left_click_events__(self):
        None

    def __right_click_events__(self):
        None

    def __middle_click_events__(self):
        None