import math

import pygame

import common.Object

bubble_start_distance = 48

def check_containing(bubble):
    area_rect = None
    if bubble.captured_animal_image is None:
        area_rect = pygame.Rect(0, 0, 1280, 592)
    else:
        area_rect = pygame.Rect(0, -bubble.radius, 1280, 592 + bubble.radius)

    check_result = area_rect[0] < bubble.center[0] - bubble.radius / 2
    check_result &= area_rect[1] < bubble.center[1] - bubble.radius / 2
    check_result &= area_rect[2] > bubble.center[0] + bubble.radius / 2
    check_result &= area_rect[3] > bubble.center[1] + bubble.radius / 2
    return check_result

class Bubble(common.Object):

    def __init__(self, pos_angle, velocity, vel_angle, image):
        super().__init__("BubbleObject", image)
        self.center = (640 + bubble_start_distance * math.cos(math.radians(pos_angle)),
                       360 + bubble_start_distance * math.sin(math.radians(pos_angle)))
        self.velocity = velocity
        self.angle = math.radians(vel_angle)
        self.rect = pygame.Rect(self.center[0], self.center[1], 0, 0)

        self.radius = 0
        self.prepare_to_delete = False
        self.is_bubble_hovered = False

        self.captured_animal_image = None
        self.update()

    def update(self):
        self.is_bubble_hovered = False
        if self.captured_animal_image is None:
            self.radius += 1

        self.center = (self.center[0] + self.velocity * math.cos(self.angle),
                       self.center[1] + self.velocity * math.sin(self.angle))

        self.rect = pygame.Rect(self.center[0], self.center[1], self.radius, self.radius)
        if not check_containing(self):
            self.prepare_to_delete = True

    def change_movement_when_capture(self):
        self.angle = math.radians(270)
        self.velocity = 1

    def render(self, window, position_translation = (0, 0)):
        pass