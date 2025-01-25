import random

import pygame

import audio.Sound
import common.Scene
import drawable.Image
import game.objects.Animal
import game.objects.Background
import game.objects.Bubble

def resolve_collision(bubble1, bubble2):
    if bubble1.rect.colliderect(bubble2.rect):
        if bubble1.radius > bubble2.radius:
            bubble1.prepare_to_delete = True
        elif bubble2.radius > bubble1.radius:
            bubble2.prepare_to_delete = True
        else:
            bubble1.prepare_to_delete = True
            bubble2.prepare_to_delete = True

class Game(common.Scene):

    def __init__(self, window):
        super().__init__("GameMainScene", window)

        self.frames_per_beginning = 0
        self.score = 0

        self.background = game.objects.Background()
        self.bubble_image = drawable.Image("bubble_image", "assets/sprites/bubble.png")
        self.bubbles = []
        self.animals = []

        self.font = drawable.Font("GameFont")
        self.font.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 48)
        self.score_text = "Wynik:"

        pygame.mouse.set_visible(False)
        self.is_mouse_clicked = False
        self.cursor_image = None
        self.cursor_image_rect = None
        self.update()

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        self.cursor_image_rect.center = pygame.mouse.get_pos()
        self.is_mouse_clicked = mouse_input[0]

    def update(self):
        while len(self.animals) < 5:
            match random.randint(1, 2):
                case 1:
                    self.animals.append(game.objects.Cow())
                case 2:
                    self.animals.append(game.objects.Chicken())
                case _:
                    pass
            if len(self.animals) == 5:
                self.cursor_image = self.animals[0].img
                self.cursor_image_rect = self.cursor_image.image.get_rect()

        for it in range (0, len(self.bubbles) - 1):
            for jt in range(it + 1, len(self.bubbles)):
                resolve_collision(self.bubbles[it], self.bubbles[jt])
        for bubble in self.bubbles:
            bubble.update()
            if self.is_mouse_clicked and pygame.Rect(bubble.center[0] - self.animals[0].size / 2, bubble.center[1] - self.animals[0].size / 2, self.animals[0].size, self.animals[0].size).collidepoint(self.cursor_image_rect.center):
                bubble.prepare_to_delete = True
                if self.animals[0].size < bubble.radius:
                    self.animals = self.animals[1:]
                    self.score += 1
                    return
            if bubble.prepare_to_delete:
                self.bubbles.remove(bubble)

        if len(self.bubbles) < 300:
            new_bubble = game.objects.Bubble(random.randint(1, 5), random.randint(0, 359),
                                             self.bubble_image)
            self.bubbles.append(new_bubble)

        self.frames_per_beginning += 1

    def render(self, color=pygame.Color(255, 255, 255, 255)):
        self.background.render(self.window.window)
        for bubble in self.bubbles:
            bubble_surface = pygame.transform.scale(self.bubble_image.image, (bubble.radius, bubble.radius))
            position = (bubble.center[0] - bubble.radius / 2, bubble.center[1] - bubble.radius / 2)
            self.window.window.blit(bubble_surface, position)

        self.window.window.blit(self.cursor_image.image, self.cursor_image_rect)
        self.font.render_text(self.window.window, self.score_text + str(self.score), pygame.Color(255, 255, 255, 255), (100, 50))