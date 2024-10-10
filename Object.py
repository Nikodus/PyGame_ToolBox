from defines import *



class Object:

    def __draw__(self, window):
        pass

    def __left_click_events__(self):
        pass

    def __right_click_events__(self):
        pass

    def __middle_click_events__(self):
        pass


class Text_button(Object):
    __Rectangle = None
    __Button_color = None
    __Text = None
    __Text_color = None
    __Font = None
    __Left_onclick_fun = None
    __Left_onclick_fun_param = None
    __Right_onclick_fun = None
    __Right_onclick_fun_param = None
    __Middle_onclick_fun = None
    __Middle_onclick_fun_param = None
    __Left_offclick_fun = None
    __Left_offclick_fun_param = None
    __Right_offclick_fun = None
    __Right_offclick_fun_param = None
    __Middle_offclick_fun = None
    __Middle_offclick_fun_param = None

    # TODO auf Pygame rect umbauen

    def __init__(self, rect:pygame.rect, text: str = "Button",
                 font: pygame.font = Defines.medium_text_font, button_color: pygame.color = Defines.gray,
                 text_color: pygame.color = Defines.white):
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
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.__Rectangle.x and pos[0] < (self.__Rectangle.x + self.__Rectangle.width):
                if pos[1] > self.__Rectangle.y and pos[1] < (self.__Rectangle.y + self.__Rectangle.height):
                    self.__Left_onclick_fun(*self.__Left_onclick_fun_param)
                    result = True
            else:
                self.__Left_offclick_fun(*self.__Left_offclick_fun_param)
        except:
            None
        return result

    def __right_click_events__(self):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.__Rectangle.x and pos[0] < (self.__Rectangle.x + self.__Rectangle.width):
                if pos[1] > self.__Rectangle.y and pos[1] < (self.__Rectangle.y + self.__Rectangle.height):
                    self.__Right_onclick_fun(*self.__Right_onclick_fun_param)
                    result = True
            else:
                self.__Right_offclick_fun(*self.__Right_offclick_fun_param)
        except:
            None
        return result

    def __middle_click_events__(self):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.__Rectangle.x and pos[0] < (self.__Rectangle.x + self.__Rectangle.width):
                if pos[1] > self.__Rectangle.y and pos[1] < (self.__Rectangle.y + self.__Rectangle.height):
                    self.__Middle_onclick_fun(*self.__Middle_onclick_fun_param)
                    result = True
            else:
                self.__Middle_offclick_fun(*self.__Middle_offclick_fun_param)
        except:
            None
        return result

    def getRectangle(self):
        return self.__Rectangle

    def setLeftonClickFunction(self, function, *parameter):
        self.__Left_onclick_fun = function
        self.__Left_onclick_fun_param = parameter

    def setLeftoffClickFunction(self, function, *parameter):
        self.__Left_offclick_fun = function
        self.__Left_offclick_fun_param = parameter

    def setRightonClickFunction(self, function, *parameter):
        self.__Right_onclick_fun = function
        self.__Right_onclick_fun_param = parameter

    def setRightoffClickFunction(self, function, *parameter):
        self.__Right_offclick_fun = function
        self.__Right_offclick_fun_param = parameter

    def setMiddleonClickFunction(self, function, *parameter):
        self.__Middle_onclick_fun = function
        self.__Middle_onclick_fun_param = parameter

    def setMiddleoffClickFunction(self, function, *parameter):
        self.__Middle_offclick_fun = function
        self.__Middle_offclick_fun_param = parameter

    def setButtonColor(self, color: pygame.color):
        self.__Button_color = color

    def setButtonTextColor(self, color: pygame.color):
        self.__Text_color = color

    def setHeight(self,new_height:int ):
        self.__Rectangle.height = new_height

    def setWidth(self, new_width: int):
        self.__Rectangle.width = new_width


class Toolbar(Object):
    __Button_list = None
    __height = None
    __width = None
    __bar_color = None
    __defines = Defines()
    __text_border = None
    __option_height = None

    def __init__(self, height: int, text_border: int = 20, option_height: int = 20,
                 bar_color: pygame.color = Defines.gray):
        self.__Button_list = []
        self.__height = height
        self.__width = pygame.display.get_window_size()[0]
        self.__bar_color = bar_color
        self.__bar_rect = pygame.Rect(0, 0, self.__width, self.__height)
        self.__text_border = text_border
        self.__option_height = option_height

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
        category_font = self.__defines.dynamic_font(self.__bar_rect, Text, self.__text_border)

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
            optionlist = [Text_button(pygame.Rect(cat_x.x + cat_x.width + 5, cat_y, cat_width, cat_height), Text, category_font), 0]
            optionlist[0].setLeftonClickFunction(self.__onclickCategory__, optionlist)
            optionlist[0].setLeftoffClickFunction(self.__offclickCategory__, optionlist)
            self.__Button_list.append(optionlist)

    def __onclickCategory__(self, optionlist: list):
        if optionlist[1] == 0:
            optionlist[1] = 1
            optionlist[0].setButtonColor(self.__defines.dark_gray)
        else:
            optionlist[1] = 0
            optionlist[0].setButtonColor(self.__defines.gray)

    def __offclickCategory__(self, optionlist: list):
        optionlist[1] = 0
        optionlist[0].setButtonColor(self.__defines.gray)

    def add_Option(self, index: int, Text: str = "Option"):
        if index > len(self.__Button_list):
            raise IndexError
        if self.__Button_list == []:
            raise RuntimeError

        cat_rect = self.__Button_list[index][0].getRectangle()
        dummy_rect = pygame.Rect(0, 0, cat_rect.width, self.__option_height + 3)
        opt_font = self.__defines.dynamic_font(dummy_rect, Text, 5)

        opt_x = self.__Button_list[index][0].getRectangle().x
        opt_width = self.__Button_list[index][0].getRectangle().width
        opt_height = self.__option_height + 10

        last_index = len(self.__Button_list[index]) - 1

        if last_index == 1:
            opt_y = self.__bar_rect.height
            self.__Button_list[index].append(Text_button(pygame.Rect(opt_x, opt_y, opt_width, opt_height), Text, opt_font))

        else:
            opt_y = self.__Button_list[index][last_index].getRectangle().y + self.__Button_list[index][
                last_index].getRectangle().height
            self.__Button_list[index].append(Text_button(pygame.Rect(opt_x, opt_y, opt_width, opt_height), Text, opt_font))

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

    # TODO Unter Option Funktion hinzufügen


class PictureBox(Object):
    __Picture = None
    __Picture_rect = None
    __width = None
    __height = None
    __Left_onclick_fun = None
    __Left_onclick_fun_param = None
    __Right_onclick_fun = None
    __Right_onclick_fun_param = None
    __Middle_onclick_fun = None
    __Middle_onclick_fun_param = None
    __Left_offclick_fun = None
    __Left_offclick_fun_param = None
    __Right_offclick_fun = None
    __Right_offclick_fun_param = None
    __Middle_offclick_fun = None
    __Middle_offclick_fun_param = None

    def __init__(self, x: int, y: int, path: str, width: int = None, height: int = None):
        try:
            self.__Picture = pygame.image.load(path)
        except:
            raise FileNotFoundError("File Not Found")

        if width is not None:
            if height is not None:
                self.__Picture_rect = pygame.Rect(x, y, width, height)
            else:
                self.__Picture_rect = pygame.Rect(x, y, width, self.__Picture.get_rect().height)
        elif height is not None:
            self.__Picture_rect = pygame.Rect(x, y, self.__Picture.get_rect().width, height)
        else:
            self.__Picture_rect = pygame.Rect(x, y, self.__Picture.get_rect().width, self.__Picture.get_rect().height)

        self.__height = height
        self.__width = width

    def setScale(self, scale: float):
        self.__height = self.__Picture.get_rect().height * scale
        self.__width = self.__Picture.get_rect().width * scale

        self.__Picture_rect = pygame.Rect(self.__Picture_rect.x, self.__Picture_rect.y, self.__width, self.__height)

    def set_width_height_Scale(self, scale_width: float, scale_height: float):
        self.__height = self.__Picture.get_rect().height * scale_height
        self.__width = self.__Picture.get_rect().width * scale_width

        self.__Picture_rect = pygame.Rect(self.__Picture_rect.x, self.__Picture_rect.y, self.__width, self.__height)

    def __draw__(self, window):
        self.__Picture = pygame.transform.scale(self.__Picture, [self.__Picture_rect.width, self.__Picture_rect.height])
        window.blit(self.__Picture, self.__Picture_rect)

    def __left_click_events__(self):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.__Picture_rect.x and pos[0] < (self.__Picture_rect.x + self.__Picture_rect.width):
                if pos[1] > self.__Picture_rect.y and pos[1] < (self.__Picture_rect.y + self.__Picture_rect.height):
                    self.__Left_onclick_fun(*self.__Left_onclick_fun_param)
                    result = True
            else:
                self.__Left_offclick_fun(*self.__Left_offclick_fun_param)
        except:
            None
        return result

    def __right_click_events__(self):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.__Picture_rect.x and pos[0] < (self.__Picture_rect.x + self.__Picture_rect.width):
                if pos[1] > self.__Picture_rect.y and pos[1] < (self.__Picture_rect.y + self.__Picture_rect.height):
                    self.__Right_onclick_fun(*self.__Right_onclick_fun_param)
                    result = True
            else:
                self.__Right_offclick_fun(*self.__Right_offclick_fun_param)
        except:
            None
        return result

    def __middle_click_events__(self):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.__Picture_rect.x and pos[0] < (self.__Picture_rect.x + self.__Picture_rect.width):
                if pos[1] > self.__Picture_rect.y and pos[1] < (self.__Picture_rect.y + self.__Picture_rect.height):
                    self.__Middle_onclick_fun(*self.__Middle_onclick_fun_param)
                    result = True
            else:
                self.__Middle_offclick_fun(*self.__Middle_offclick_fun_param)
        except:
            None
        return result

    def setLeftonClickFunction(self, function, *parameter):
        self.__Left_onclick_fun = function
        self.__Left_onclick_fun_param = parameter

    def setLeftoffClickFunction(self, function, *parameter):
        self.__Left_offclick_fun = function
        self.__Left_offclick_fun_param = parameter

    def setRightonClickFunction(self, function, *parameter):
        self.__Right_onclick_fun = function
        self.__Right_onclick_fun_param = parameter

    def setRightoffClickFunction(self, function, *parameter):
        self.__Right_offclick_fun = function
        self.__Right_offclick_fun_param = parameter

    def setMiddleonClickFunction(self, function, *parameter):
        self.__Middle_onclick_fun = function
        self.__Middle_onclick_fun_param = parameter

    def setMiddleoffClickFunction(self, function, *parameter):
        self.__Middle_offclick_fun = function
        self.__Middle_offclick_fun_param = parameter


class Label(Object):
    __Label_rect = None
    __Text = None
    __Text_font = None
    __Text_color = None
    __Left_onclick_fun = None
    __Left_onclick_fun_param = None
    __Right_onclick_fun = None
    __Right_onclick_fun_param = None
    __Middle_onclick_fun = None
    __Middle_onclick_fun_param = None
    __Left_offclick_fun = None
    __Left_offclick_fun_param = None
    __Right_offclick_fun = None
    __Right_offclick_fun_param = None
    __Middle_offclick_fun = None
    __Middle_offclick_fun_param = None

    def __init__(self, x: int, y: int, Text_font: pygame.font, Text: str = "Label",
                 Text_color: pygame.color = Defines.white):
        self.__Text = Text
        self.__Text_font = Text_font
        self.__Label_rect = pygame.Rect(x, y, Text_font.size(Text)[0], Text_font.size(Text)[1])
        self.__Text_color = Text_color

    def __draw__(self, window):
        button_text = self.__Text_font.render(self.__Text, True, self.__Text_color)
        text_rect = button_text.get_rect(center=self.__Label_rect.center)
        window.blit(button_text, text_rect)

    def __left_click_events__(self):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.__Label_rect.x and pos[0] < (self.__Label_rect.x + self.__Label_rect.width):
                if pos[1] > self.__Label_rect.y and pos[1] < (self.__Label_rect.y + self.__Label_rect.height):
                    self.__Left_onclick_fun(*self.__Left_onclick_fun_param)
                    result = True
            else:
                self.__Left_offclick_fun(*self.__Left_offclick_fun_param)
        except:
            None
        return result

    def __right_click_events__(self):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.__Label_rect.x and pos[0] < (self.__Label_rect.x + self.__Label_rect.width):
                if pos[1] > self.__Label_rect.y and pos[1] < (self.__Label_rect.y + self.__Label_rect.height):
                    self.__Right_onclick_fun(*self.__Right_onclick_fun_param)
                    result = True
            else:
                self.__Right_offclick_fun(*self.__Right_offclick_fun_param)
        except:
            None
        return result

    def __middle_click_events__(self):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.__Label_rect.x and pos[0] < (self.__Label_rect.x + self.__Label_rect.width):
                if pos[1] > self.__Label_rect.y and pos[1] < (self.__Label_rect.y + self.__Label_rect.height):
                    self.__Middle_onclick_fun(*self.__Middle_onclick_fun_param)
                    result = True
            else:
                self.__Middle_offclick_fun(*self.__Middle_offclick_fun_param)
        except:
            None
        return result

    def setLeftonClickFunction(self, function, *parameter):
        self.__Left_onclick_fun = function
        self.__Left_onclick_fun_param = parameter

    def setLeftoffClickFunction(self, function, *parameter):
        self.__Left_offclick_fun = function
        self.__Left_offclick_fun_param = parameter

    def setRightonClickFunction(self, function, *parameter):
        self.__Right_onclick_fun = function
        self.__Right_onclick_fun_param = parameter

    def setRightoffClickFunction(self, function, *parameter):
        self.__Right_offclick_fun = function
        self.__Right_offclick_fun_param = parameter

    def setMiddleonClickFunction(self, function, *parameter):
        self.__Middle_onclick_fun = function
        self.__Middle_onclick_fun_param = parameter

    def setMiddleoffClickFunction(self, function, *parameter):
        self.__Middle_offclick_fun = function
        self.__Middle_offclick_fun_param = parameter


class Invisible_Button(Object):
    __Rectangle = None
    __Left_onclick_fun = None
    __Left_onclick_fun_param = None
    __Right_onclick_fun = None
    __Right_onclick_fun_param = None
    __Middle_onclick_fun = None
    __Middle_onclick_fun_param = None
    __Left_offclick_fun = None
    __Left_offclick_fun_param = None
    __Right_offclick_fun = None
    __Right_offclick_fun_param = None
    __Middle_offclick_fun = None
    __Middle_offclick_fun_param = None
    __showButton = 0

    def __init__(self, x: int, y: int, width: int, height: int):
        self.__Rectangle = pygame.Rect(x, y, width, height)

    def __draw__(self, window):
        if self.__showButton == 1:
            pygame.draw.rect(window, Defines.black, self.__Rectangle)
            button_text = Defines.dynamic_font(Defines, self.__Rectangle, "Here").render("Here", True, Defines.white)
            text_rect = button_text.get_rect(center=self.__Rectangle.center)
            window.blit(button_text, text_rect)

    def __left_click_events__(self):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.__Rectangle.x and pos[0] < (self.__Rectangle.x + self.__Rectangle.width):
                if pos[1] > self.__Rectangle.y and pos[1] < (self.__Rectangle.y + self.__Rectangle.height):
                    self.__Left_onclick_fun(*self.__Left_onclick_fun_param)
                    result = True
            else:
                self.__Left_offclick_fun(*self.__Left_offclick_fun_param)
        except:
            None
        return result

    def __right_click_events__(self):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.__Rectangle.x and pos[0] < (self.__Rectangle.x + self.__Rectangle.width):
                if pos[1] > self.__Rectangle.y and pos[1] < (self.__Rectangle.y + self.__Rectangle.height):
                    self.__Right_onclick_fun(*self.__Right_onclick_fun_param)
                    result = True
            else:
                self.__Right_offclick_fun(*self.__Right_offclick_fun_param)
        except:
            None
        return result

    def __middle_click_events__(self):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.__Rectangle.x and pos[0] < (self.__Rectangle.x + self.__Rectangle.width):
                if pos[1] > self.__Rectangle.y and pos[1] < (self.__Rectangle.y + self.__Rectangle.height):
                    self.__Middle_onclick_fun(*self.__Middle_onclick_fun_param)
                    result = True
            else:
                self.__Middle_offclick_fun(*self.__Middle_offclick_fun_param)
        except:
            None
        return result

    def setLeftonClickFunction(self, function, *parameter):
        self.__Left_onclick_fun = function
        self.__Left_onclick_fun_param = parameter

    def setLeftoffClickFunction(self, function, *parameter):
        self.__Left_offclick_fun = function
        self.__Left_offclick_fun_param = parameter

    def setRightonClickFunction(self, function, *parameter):
        self.__Right_onclick_fun = function
        self.__Right_onclick_fun_param = parameter

    def setRightoffClickFunction(self, function, *parameter):
        self.__Right_offclick_fun = function
        self.__Right_offclick_fun_param = parameter

    def setMiddleonClickFunction(self, function, *parameter):
        self.__Middle_onclick_fun = function
        self.__Middle_onclick_fun_param = parameter

    def setMiddleoffClickFunction(self, function, *parameter):
        self.__Middle_offclick_fun = function
        self.__Middle_offclick_fun_param = parameter

    def showButton(self):
        self.__showButton = 1

# TODO TextBox hinzufügen


# TODO weitere Objekte hinzufügen
