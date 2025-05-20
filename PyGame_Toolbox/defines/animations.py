import time
import pygame

class animations:

    def dropdown_animation(self,rectangle:pygame.rect.Rect,window:pygame.display,color:pygame.color,new_height:int):
        height = rectangle.height

        for i in range(new_height-height):
            rectangle.height = height+i
            pygame.draw.rect(window,color,rectangle)
            time.sleep(0.001)

    # TODO Animation Testen (Später) (Möglicherweise umprogrammieren)


# TODO Animationen wie Dropdown Fade-in oder Fade-out implementieren
