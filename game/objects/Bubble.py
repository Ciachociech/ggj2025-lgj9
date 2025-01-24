import pygame

import common.Object


class Bubble(common.Object):

    def __init__(self):
        super().__init__("BubbleObject", "assets/sprites/bubble.png")
        self.initial_position = (640, 360)
        self.position = self.initial_position
        self.lifetime = 0
        self.update()

    def update(self):
        self.lifetime += 1
        self.position = (640 - self.lifetime / 2, 360 - self.lifetime / 2)

    def render(self, window, position_translation = (0, 0)):
        image = pygame.transform.scale(self.img.image, (self.lifetime, self.lifetime))
        window.blit(image, self.position + position_translation)