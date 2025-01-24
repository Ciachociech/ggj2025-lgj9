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
        if len(self.bubbles) < 300:
            new_bubble = game.objects.Bubble(random.randint(1, 5), random.randint(0, 359),
                                             self.bubble_image)
            self.bubbles.append(new_bubble)

    def render(self, color=pygame.Color(255, 255, 255, 255)):
        self.background.render(self.window.window)
        for bubble in self.bubbles:
            bubble.render(self.window.window)
