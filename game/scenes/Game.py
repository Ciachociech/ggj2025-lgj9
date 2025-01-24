import pygame

import audio.Sound
import common.Object
import common.Scene


class Game(common.Scene):

    def __init__(self, window):
        super().__init__("GameMainScene", window)

        self.background = None
        self.bubble_texture = common.Object("bubble", "assets/sprites/PLACEHOLDER_bubble.png")
        self.position = (640, 360)

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        pass

    def update(self):
        return None

    def render(self, color=pygame.Color(255, 255, 255, 255)):
        self.bubble_texture.render(self.window.window, self.position)
