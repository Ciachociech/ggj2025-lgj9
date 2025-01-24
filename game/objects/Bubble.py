import math
from tabnanny import check

import pygame

import common.Object

def check_containing(bubble):
    area_rect = pygame.Rect(0, 0, 1280, 720)
    check_result = area_rect[0] < bubble.center[0] - bubble.radius / 2
    check_result &= area_rect[1] < bubble.center[1] - bubble.radius / 2
    check_result &= area_rect[2] > bubble.center[0] + bubble.radius / 2
    check_result &= area_rect[3] > bubble.center[1] + bubble.radius / 2
    return check_result

class Bubble(common.Object):

    def __init__(self, velocity, angle, image):
        super().__init__("BubbleObject", image)
        self.center = (640, 360)
        self.velocity = velocity
        self.angle = math.radians(angle)

        self.radius = 0
        self.prepare_to_delete = False

        self.update()

    def update(self):
        self.radius += 1
        self.center = (self.center[0] + self.velocity * math.cos(self.angle),
                       self.center[1] + self.velocity * math.sin(self.angle))

        area_rect = pygame.Rect(0, 0, 1280, 720)
        if not check_containing(self):
            self.prepare_to_delete = True

    def render(self, window, position_translation = (0, 0)):
        image = pygame.transform.scale(self.img.image, (self.radius, self.radius))
        position = (self.center[0] - self.radius / 2, self.center[1] - self.radius / 2)
        window.blit(image, position + position_translation)