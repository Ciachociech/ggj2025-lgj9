import pygame

import common.Scene
import game.objects.Background


class MainMenu(common.Scene):

    def __init__(self, window):
        super().__init__("PauseScene", window)

        self.background = game.objects.Background("assets/sprites/menu.png")
        self.resume()

    def resume(self):
        pass

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        pass

    def update(self):
        pass

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        self.background.render(self.window.window)

        pygame.draw.rect(self.window.window, pygame.Color(128, 128, 128, 255), pygame.Rect(480, 300, 320, 80))
        pygame.draw.rect(self.window.window, pygame.Color(128, 128, 128, 255), pygame.Rect(480, 400, 320, 80))
        pygame.draw.rect(self.window.window, pygame.Color(128, 128, 128, 255), pygame.Rect(480, 500, 320, 80))
        pygame.draw.rect(self.window.window, pygame.Color(128, 128, 128, 255), pygame.Rect(480, 600, 320, 80))