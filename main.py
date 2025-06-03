import PyGame_Toolbox as tb
import pygame
import sys

from PyGame_Toolbox import fonts, specfonts
from PyGame_Toolbox.Objects import TextBox


def test(i,j):
    print(i+j)

pygame.init()

toolbox = tb.Toolbox()

size = width, height = 800, 430
window = pygame.display.set_mode(size)

button = tb.Text_button(pygame.Rect(200, 300, 100, 30))
button.setLeftonClickFunction(print, "On")

toolbox.add_Object(button)
toolbar = tb.Toolbar(30, 5, 20)
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
toolbar.Option_set_leftClick_Function(0, 0, print, "Hello")
toolbar.Option_set_leftClick_Function(0, 1, print, "Cool")
toolbar.Option_set_leftClick_Function(0, 2, print, "World")
toolbar.Option_set_rightClick_Function(0, 0, print, "World")
toolbar.Option_set_rightClick_Function(0, 1, print, "Cool")
toolbar.Option_set_rightClick_Function(0, 2, print, "Hello")
toolbar.Option_set_middleClick_Function(0, 0, print, "Middle Click")
toolbar.Option_set_middleClick_Function(0, 1, print, "is")
toolbar.Option_set_middleClick_Function(0, 2, print, "Cool")

toolbox.add_Object(toolbar)


#img = tb.PictureBox(200, 50, 'testimg.png')
#img.setScale(0.2)
#img.setLeftonClickFunction(print, "Its Me")
#toolbox.add_Object(img)

#img.setVisibility(False)
#img.setDisable(True)

text = tb.Label(50, 50, tb.fonts.medium_text_font, "Hello World")
text.setLeftonClickFunction(print,"dlrow olleH")
toolbox.add_Object(text)

invisBtn = tb.Text_button(pygame.Rect(50, 100, 100, 50))

invisBtn.setVisibility(False)
invisBtn.setLeftonClickFunction(print,"You found it")
toolbox.add_Object(invisBtn)

textbox = TextBox(100,100,200,50,text_mode=tb.Modes.Any,max_chars=10)


obj_list = [tb.Text_button(pygame.Rect(110, 400, 100, 30)), tb.Text_button(pygame.Rect(220, 400, 100, 30)),
            tb.Text_button(pygame.Rect(330, 400, 100, 30)), tb.Text_button(pygame.Rect(440, 400, 100, 30))]

toolbox.add_Object_List(obj_list)
toolbox.add_Object(textbox)
while True:
    window.fill(tb.colors.background)

    toolbox.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            toolbox.key_down_events(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                toolbox.left_click_events()
            if middle:
                toolbox.middle_click_events()
            if right:
                toolbox.right_click_events()

    pygame.display.update()
