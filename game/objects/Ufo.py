import pygame


import common.Object

class Ufo(common.Object):

    def __init__(self):
        super().__init__("UfoObject", "assets/sprites/ufo.png")
        self.position = (640 - (self.img.image.get_rect()[2] / 2), (360 - self.img.image.get_rect()[3] / 2))

    def render(self, window, position = (0, 0)):
        super().render(window, self.position + position)