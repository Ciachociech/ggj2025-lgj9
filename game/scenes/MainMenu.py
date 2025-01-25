import pygame

import common.Scene
import game.objects.Background
import game.objects.Button


class MainMenu(common.Scene):

    def __init__(self, window):
        super().__init__("PauseScene", window)

        self.background = game.objects.Background("assets/sprites/menu.png")
        self.buttons = []
        self.buttons.append(game.objects.Button((480, 300), "bez limitu"))
        self.buttons.append(game.objects.Button((480, 400), "na czas"))
        self.buttons.append(game.objects.Button((480, 500), "wyzwanie"))
        self.buttons.append(game.objects.Button((480, 600), "wyjście"))

        self.resume()

    def resume(self):
        pass

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        pass

    def update(self):
        pass

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        self.background.render(self.window.window)
        for button in self.buttons:
            button.render(self.window.window)