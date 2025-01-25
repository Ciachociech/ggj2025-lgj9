import pygame

import common.Scene
import drawable.Image
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

        self.cursor_image = drawable.Image("mainmenu-cursor", "assets/sprites/kursorUFO.png")
        self.cursor_image_rect = self.cursor_image.image.get_rect()
        self.is_left_mouse_clicked = None

        self.resume()

    def resume(self):
        pygame.mouse.set_visible(False)
        self.is_left_mouse_clicked = False

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        self.cursor_image_rect.center = pygame.mouse.get_pos()
        self.is_left_mouse_clicked = mouse_input[0]

    def update(self):
        for it in range(0, len(self.buttons)):
            self.buttons[it].update()
            if self.buttons[it].rect.collidepoint(self.cursor_image_rect.center):
                self.buttons[it].is_hovered = True
                if self.is_left_mouse_clicked:
                    return it
        return None

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        self.background.render(self.window.window)
        for button in self.buttons:
            button.render(self.window.window)

        self.window.window.blit(self.cursor_image.image, self.cursor_image_rect)