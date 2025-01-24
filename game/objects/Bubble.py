import math
import pygame

import common.Object


class Bubble(common.Object):

    def __init__(self, velocity, angle, image):
        super().__init__("BubbleObject", image)
        self.center = (640, 360)
        self.velocity = velocity
        self.angle = math.radians(angle)

        self.lifetime = 0
        self.update()

    def update(self):
        self.lifetime += 1
        self.center = (self.center[0] + self.velocity * math.cos(self.angle),
                       self.center[1] + self.velocity * math.sin(self.angle))

    def render(self, window, position_translation = (0, 0)):
        image = pygame.transform.scale(self.img.image, (self.lifetime, self.lifetime))
        position = (self.center[0] - self.lifetime / 2, self.center[1] - self.lifetime / 2)
        window.blit(image, position + position_translation)