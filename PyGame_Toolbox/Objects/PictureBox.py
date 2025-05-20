import pygame
from PyGame_Toolbox.Objects import Object

class PictureBox(Object):
    __Picture = None
    __Picture_rect = None
    __width = None
    __height = None

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
        return super().__left_click_events_rect__(self.__Picture_rect)

    def __right_click_events__(self):
        return super().__right_click_events_rect__(self.__Picture_rect)

    def __middle_click_events__(self):
        return super().__middle_click_events_rect__(self.__Picture_rect)
