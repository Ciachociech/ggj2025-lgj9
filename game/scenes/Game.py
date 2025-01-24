import pygame

import audio.Sound
import common.Scene
import game.objects.Background
import game.objects.Bubble


class Game(common.Scene):

    def __init__(self, window):
        super().__init__("GameMainScene", window)

        self.background = game.objects.Background()
        self.bubble = game.objects.Bubble()

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        pass

    def update(self):
        return None

    def render(self, color=pygame.Color(255, 255, 255, 255)):
        self.background.render(self.window.window)
        self.bubble.render(self.window.window)
