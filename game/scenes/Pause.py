import pygame

import audio.Sound
import common.Scene
import drawable.Image
import game.objects.Button


class Pause(common.Scene):

    def __init__(self, window):
        super().__init__("PauseScene", window)

        self.background = game.objects.Background("assets/sprites/pauza.png")
        self.buttons = []
        self.buttons.append(game.objects.Button((480, 500), "powrót"))
        self.buttons.append(game.objects.Button((480, 600), "do menu"))

        self.keyboard_click_cooldown = None
        self.escape_key_pressed = None

        self.cursor_image = drawable.Image("pause-cursor", "assets/sprites/kursorUFO.png")
        self.cursor_image_rect = self.cursor_image.image.get_rect()
        self.is_left_mouse_clicked = None

        self.font = drawable.Font("MainMenuTitleFont")
        self.font.load_font_from_file("assets/fonts/Tektur-Regular.ttf", 96)
        self.text = "paused"

        self.se = audio.Sound("OptionsSE", "assets/audio/menu-hover.wav")
        self.last_played_sound = -1

        self.resume()

    def resume(self):
        pygame.mouse.set_visible(False)
        self.keyboard_click_cooldown = 0
        self.escape_key_pressed = False
        self.last_played_sound = -1

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        self.cursor_image_rect.center = pygame.mouse.get_pos()
        self.is_left_mouse_clicked = mouse_input[0]

        if self.keyboard_click_cooldown > 3 and keyboard_input[pygame.K_ESCAPE]:
            self.escape_key_pressed = True
            return

    def update(self):
        if self.escape_key_pressed:
            return 0

        self.keyboard_click_cooldown += 1

        is_any_hover = False
        for it in range(0, len(self.buttons)):
            self.buttons[it].update()
            if self.buttons[it].rect.collidepoint(self.cursor_image_rect.center):
                self.buttons[it].is_hovered = True
                is_any_hover = True
                if self.last_played_sound != it:
                    self.last_played_sound = it
                    self.se.sound.play()
                if self.is_left_mouse_clicked:
                    return it

        if not is_any_hover:
            self.last_played_sound = -1
        return None

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        self.background.render(self.window.window)

        for button in self.buttons:
            button.render(self.window.window)
        self.font.render_text(self.window.window, self.text, pygame.Color(255, 255, 255, 255),
                              (640, 250), "center")

        self.window.window.blit(self.cursor_image.image, self.cursor_image_rect)
