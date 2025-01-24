import random

import pygame

import audio.Sound
import common.Scene
import drawable.Image
import game.objects.Background
import game.objects.Bubble


class Game(common.Scene):

    def __init__(self, window):
        super().__init__("GameMainScene", window)

        self.background = game.objects.Background()
        self.bubble_image = drawable.Image("bubble_image", "assets/sprites/bubble.png")
        self.bubbles = []

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        pass

    def update(self):
        for bubble in self.bubbles:
            bubble.update()
            if bubble.prepare_to_delete:
                self.bubbles.remove(bubble)
        if len(self.bubbles) < 300:
            new_bubble = game.objects.Bubble(random.randint(1, 5), random.randint(0, 359),
                                             self.bubble_image)
            self.bubbles.append(new_bubble)

    def render(self, color=pygame.Color(255, 255, 255, 255)):
        self.background.render(self.window.window)
        for bubble in self.bubbles:
            bubble_surface = pygame.transform.scale(self.bubble_image.image, (bubble.radius, bubble.radius))
            position = (bubble.center[0] - bubble.radius / 2, bubble.center[1] - bubble.radius / 2)
            self.window.window.blit(bubble_surface, position)