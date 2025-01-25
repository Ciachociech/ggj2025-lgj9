import pygame

import common.Scene
import drawable.Image
import game.objects.Button
from game.scenes.Game import GameMode


class Gameover(common.Scene):

    def __init__(self, window):
        super().__init__("GameoverScene", window)
        self.button = game.objects.Button((480, 600), "do menu")

        self.cursor_image = drawable.Image("mainmenu-cursor", "assets/cursors/kursorUFO.ico")
        self.cursor_image_rect = self.cursor_image.image.get_rect()
        self.is_left_mouse_clicked = None

        self.result_font = drawable.Font("MainMenuTitleFont")
        self.result_font.load_font_from_file("assets/fonts/Tektur-Regular.ttf", 96)
        self.stats_font = drawable.Font("MainMenuBonusFont")
        self.stats_font.load_font_from_file("assets/fonts/Tektur-Regular.ttf", 64)
        self.main_result_text = None
        self.score_text = None
        self.time_text = None

    def set(self, game_mode, data):
        pygame.mouse.set_visible(False)
        self.is_left_mouse_clicked = False

        self.score_text = "wynik: "
        self.time_text = None

        match game_mode:
            case GameMode.time_limit:
                self.main_result_text = "koniec gry"
                self.score_text += str(data[0])
            case GameMode.mixed_limit:
                self.score_text += str(data[0])
                if data[1] != -1:
                    self.main_result_text = "sukces"
                    self.time_text = "czas: " + "{:4.2f}".format(data[1] / 1000) + "s"
                else:
                    self.main_result_text = "porażka"

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        self.cursor_image_rect.center = pygame.mouse.get_pos()
        self.is_left_mouse_clicked = mouse_input[0]

    def update(self):
        self.button.update()
        if self.button.rect.collidepoint(self.cursor_image_rect.center):
                self.button.is_hovered = True
                if self.is_left_mouse_clicked:
                    return True
        return False

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        semitransparent_rectangle = pygame.Surface((1280, 720))
        semitransparent_rectangle.set_alpha(128)
        semitransparent_rectangle.fill(pygame.Color(128, 128, 128))
        self.window.window.blit(semitransparent_rectangle, (0, 0))

        self.result_font.render_text(self.window.window, self.main_result_text, pygame.Color(255, 255, 0, 255),
                              (640, 80), "center")
        self.stats_font.render_text(self.window.window, self.score_text, pygame.Color(255, 255, 255, 255),
                              (640, 200), "center")
        if self.time_text is not None:
            self.stats_font.render_text(self.window.window, self.time_text, pygame.Color(255, 255, 255, 255),
                                  (640, 288), "center")

        self.button.render(self.window.window)
        self.window.window.blit(self.cursor_image.image, self.cursor_image_rect)
