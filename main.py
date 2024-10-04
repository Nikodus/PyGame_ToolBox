import Toolbox
from Toolbox import Defines
import pygame
import sys

pygame.init()

toolbox = Toolbox.Toolbox()

size = width, height = 800, 430
window = pygame.display.set_mode(size)

button = Toolbox.Text_button(pygame.Rect(200, 300, 100, 30))
button.setLeftonClickFunction(print, "On")

toolbox.add_Object(button)
toolbar = Toolbox.Toolbar(30, 5, 20)
toolbar.add_Category()
toolbar.add_Category("Test")
toolbar.add_Category("Info")
toolbar.add_Category("Options")
toolbar.add_Category("ÄÖÜ")

toolbar.add_Option(0, "Hello")
toolbar.add_Option(0, "Cool")
toolbar.add_Option(0, "World")
toolbar.add_Option(3, "Hello")
toolbar.add_Option(3, "Cool")
toolbar.add_Option(3, "World")
toolbar.Option_add_leftClick_Function(0, 0, print, "Hello")
toolbar.Option_add_leftClick_Function(0, 1, print, "Cool")
toolbar.Option_add_leftClick_Function(0, 2, print, "World")
toolbar.Option_add_rightClick_Function(0, 0, print, "World")
toolbar.Option_add_rightClick_Function(0, 1, print, "Cool")
toolbar.Option_add_rightClick_Function(0, 2, print, "Hello")
toolbar.Option_add_middleClick_Function(0, 0, print, "Middle Click")
toolbar.Option_add_middleClick_Function(0, 1, print, "is")
toolbar.Option_add_middleClick_Function(0, 2, print, "Cool")

toolbox.add_Object(toolbar)
#Testing

img = Toolbox.PictureBox(200, 50, 'testimg.png')
img.setScale(0.2)
img.setLeftonClickFunction(print, "Its Me")
toolbox.add_Object(img)


text = Toolbox.Label(50,50,Defines.medium_text_font,"Hello World")
text.setLeftonClickFunction(print,"dlrow olleH")
toolbox.add_Object(text)

invisBtn = Toolbox.Invisible_Button(50,100,100,50)

invisBtn.setLeftonClickFunction(print,"You found it")
toolbox.add_Object(invisBtn)


obj_list = [Toolbox.Text_button(pygame.Rect(110, 400, 100, 30)),Toolbox.Text_button(pygame.Rect(220, 400, 100, 30)),Toolbox.Text_button(pygame.Rect(330, 400, 100, 30)),Toolbox.Text_button(pygame.Rect(440, 400, 100, 30))]

toolbox.add_Object_List(obj_list)

while True:
    window.fill(Defines.background)

    toolbox.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                toolbox.left_click_events()
            if middle:
                toolbox.middle_click_events()
            if right:
                toolbox.right_click_events()

    pygame.display.update()
