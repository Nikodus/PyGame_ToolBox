from enum import Enum

import pygame

from PyGame_Toolbox.Objects import *




class Toolbox:
    __Object_list = []

    def __init__(self):
        None

    def add_Object(self, newObject: Object):

        if isinstance(newObject, Toolbar):
            for obj in self.__Object_list:
                if isinstance(obj, Toolbar):
                    raise Exception("Only one Toolbar allowed")
            self.__Object_list.append(newObject)
        else:
            self.__Object_list.insert(0, newObject)

    def add_Object_List(self, newObject_list: list):
        for newObject in newObject_list:
            if isinstance(newObject, Object):
                self.add_Object(newObject)
            else:
                raise TypeError("Wrong Type in List: " + str(newObject))

    def draw(self, window: pygame.display):
        for Obj in self.__Object_list:
            Obj.__draw_visible__(window)

    def left_click_events(self):
        list_object = self.__Object_list[::-1]
        for Obj in list_object:
            if Obj.__left_click_events__():
                break

    def right_click_events(self):
        list_object = self.__Object_list[::-1]
        for Obj in list_object:
            if Obj.__right_click_events__():
                break

    def middle_click_events(self):
        list_object = self.__Object_list[::-1]
        for Obj in list_object:
            if Obj.__middle_click_events__():
                break

    def key_down_events(self,event:pygame.event):
        for obj in self.__Object_list:
            try:
                if obj.__key_down_events__(event):
                    break
            except:
                None
