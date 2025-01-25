import pygame
from pygame.examples.cursors import image

import common.Object
import drawable.Font


class Button(common.Object):

    def __init__(self, position, text):
        super().__init__("ButtonObject", "assets/sprites/button_background.png")
        self.position = position
        self.size = self.img.image.get_size()
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.is_hovered = False
        self.button_hover_highlight = drawable.Image("mainmenu-highlight", "assets/sprites/button_background_hover.png")

        self.font = drawable.Font("GameFont")
        self.font.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 48)
        self.button_text = text

    def update(self):
        self.is_hovered = False

    def render(self, window, position = (0, 0)):
        super().render(window, self.position + position)

        if self.is_hovered:
            window.blit(self.button_hover_highlight.image, self.position)
        self.font.render_text(window, self.button_text, pygame.Color(255, 255, 255, 255),
                              (self.position[0] + self.size[0] / 2, self.position[1] - 2 + self.size[1] / 2), "center")