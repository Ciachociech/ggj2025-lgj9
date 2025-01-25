import pygame

import common.Scene


class Pause(common.Scene):

    def __init__(self, window):
        super().__init__("PauseScene", window)

        self.keyboard_click_cooldown = None
        self.escape_key_pressed = None

        self.resume()

    def resume(self):
        self.keyboard_click_cooldown = 0
        self.escape_key_pressed = False

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        if self.keyboard_click_cooldown > 3 and keyboard_input[pygame.K_ESCAPE]:
            self.escape_key_pressed = True
            return

    def update(self):
        if self.escape_key_pressed:
            return 1

        self.keyboard_click_cooldown += 1

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        semitransparent_rectangle = pygame.Surface((1280, 720))
        semitransparent_rectangle.set_alpha(128)
        semitransparent_rectangle.fill(pygame.Color(128, 128, 128))
        self.window.window.blit(semitransparent_rectangle, (0, 0))
