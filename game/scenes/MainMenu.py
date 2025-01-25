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

        self.title_font = drawable.Font("MainMenuTitleFont")
        self.title_font.load_font_from_file("assets/fonts/Tektur-Medium.ttf", 64)
        self.bonus_font = drawable.Font("MainMenuBonusFont")
        self.bonus_font.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 20)
        self.title_text = "Tajemnicze bąbelki z kosmosu"
        self.bonus_text = "Jak nazwiemy team to coś tu wstawimy"

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
        self.title_font.render_text(self.window.window, self.title_text, pygame.Color(255, 255, 128, 255),
                              (644, 164), "center")
        self.title_font.render_text(self.window.window, self.title_text, pygame.Color(0, 255, 0, 255),
                              (640, 160), "center")
        self.bonus_font.render_text(self.window.window, self.bonus_text, pygame.Color(255, 255, 255, 255),
                              (1268, 708), "bottomright")

        self.window.window.blit(self.cursor_image.image, self.cursor_image_rect)