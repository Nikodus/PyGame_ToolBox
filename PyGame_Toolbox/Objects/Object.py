import pygame

class Object:
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
    __visible = True
    __disable = False

    def __draw__(self, window: pygame.display):
        pass


    def __draw_visible__(self,window: pygame.display):
        if self.__visible:
            self.__draw__(window)

    def __left_click_events__(self):
        pass

    def __left_click_events_rect__(self,rect:pygame.rect):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > rect.x and pos[0] < (rect.x + rect.width):
                if pos[1] > rect.y and pos[1] < (rect.y + rect.height):
                    self.leftonclick()
                    result = True
            else:
                self.leftoffclick()
        except:
            None
        return result

    def __right_click_events__(self):
        pass
    def __right_click_events_rect__(self,rect:pygame.rect):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > rect.x and pos[0] < (rect.x + rect.width):
                if pos[1] > rect.y and pos[1] < (rect.y + rect.height):
                    self.rightonclick()
                    result = True
            else:
                self.rightoffclick()
        except:
            None
        return result

    def __middle_click_events__(self):
        pass

    def __middle_click_events_rect__(self,rect:pygame.rect):
        result = False
        try:
            pos = pygame.mouse.get_pos()
            if pos[0] > rect.x and pos[0] < (rect.x + rect.width):
                if pos[1] > rect.y and pos[1] < (rect.y + rect.height):
                    self.middleonclick()
                    result = True
            else:
                self.middleoffclick()
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

    def leftonclick(self):
        if not self.__disable:
            return self.__Left_onclick_fun(*self.__Left_onclick_fun_param)
        return None
    def leftoffclick(self):
        if not self.__disable:
            return self.__Left_offclick_fun(*self.__Left_offclick_fun_param)
        return None
    def rightonclick(self):
        if not self.__disable:
            return self.__Right_onclick_fun(*self.__Right_onclick_fun_param)
        return None
    def rightoffclick(self):
        if not self.__disable:
            return self.__Right_offclick_fun(*self.__Right_offclick_fun_param)
        return None
    def middleonclick(self):
        if not self.__disable:
            return self.__Middle_onclick_fun(*self.__Middle_onclick_fun_param)
        return None
    def middleoffclick(self):
        if not self.__disable:
            return self.__Middle_offclick_fun(*self.__Middle_offclick_fun_param)
        return None

    def setVisibility(self,newValue:bool):
        self.__visible = newValue

    def getVisibility(self):
        return self.__visible

    def setDisable(self,newValue:bool):
        self.__disable = newValue

    def getDisable(self):
        return self.__disable

# TODO weitere Objekte hinzufügen
