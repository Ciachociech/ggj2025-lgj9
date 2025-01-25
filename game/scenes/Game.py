import math
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
        self.ufo = game.objects.Ufo()
        self.bubble_image = drawable.Image("bubble_image", "assets/sprites/bubble.png")
        self.hovered_bubble_image = drawable.Image("bubble_image", "assets/sprites/h_bubble.png")
        self.bubbles = []
        self.animals = []

        self.font = drawable.Font("GameFont")
        self.font.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 48)
        self.score_text = "Wynik:"

        self.is_left_mouse_clicked = False
        self.is_right_mouse_clicked = False
        self.animal_chosen = -1
        self.mouse_click_cooldown = 0
        self.cursor_image = None
        self.cursor_image_rect = pygame.Rect(0, 0, 0, 0)
        self.update()

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        self.cursor_image_rect.center = pygame.mouse.get_pos()
        if self.mouse_click_cooldown > 3:
            self.is_left_mouse_clicked = mouse_input[0]
            self.is_right_mouse_clicked = mouse_input[2]

    def update(self):
        # if less than 10 animals, spawn to fill this limit
        while len(self.animals) < 10:
            match random.randint(1, 5):
                case 1:
                    self.animals.append(game.objects.Cow(128 * len(self.animals)))
                case 2:
                    self.animals.append(game.objects.Chicken(128 * len(self.animals)))
                case 3:
                    self.animals.append(game.objects.Fox(128 * len(self.animals)))
                case 4:
                    self.animals.append(game.objects.Deer(128 * len(self.animals)))
                case 5:
                    self.animals.append(game.objects.Rabbit(random.randint(0, 99), 128 * len(self.animals)))
                case _:
                    pass

        # set cursor when any animal is chosen
        if self.animal_chosen != -1:
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)

        # check collision
        for it in range (0, len(self.bubbles) - 1):
            for jt in range(it + 1, len(self.bubbles)):
                resolve_collision(self.bubbles[it], self.bubbles[jt])

        # manage bubbles
        for bubble in self.bubbles:
            bubble.update()
            if pygame.Rect(bubble.center[0] - bubble.radius, bubble.center[1] - bubble.radius, 2 * bubble.radius, 2 * bubble.radius).collidepoint(self.cursor_image_rect.center):
                if bubble.radius > 2 * self.animals[0].size / math.sqrt(2):
                    bubble.is_bubble_hovered = True
                    if self.is_left_mouse_clicked:
                        self.animals = self.animals[1:]
                        self.score += 1
                        self.animal_chosen = -1
                        for animal in self.animals:
                            animal.update_position()
                if self.is_left_mouse_clicked:
                    bubble.prepare_to_delete = True
                    self.is_left_mouse_clicked = False
                    self.mouse_click_cooldown = 0
            if bubble.prepare_to_delete:
                self.bubbles.remove(bubble)
        if len(self.bubbles) < 300:
            new_bubble = game.objects.Bubble(random.randint(0, 359), random.randint(1, 5), random.randint(0, 359),
                                             self.bubble_image)
            self.bubbles.append(new_bubble)

        # manage animals
        if self.is_right_mouse_clicked:
            self.animal_chosen = -1
        for it in range (1, len(self.animals)):
            if self.animals[it].rect.collidepoint(pygame.mouse.get_pos()) and self.is_left_mouse_clicked:
                self.animal_chosen = it
                self.cursor_image = self.animals[it].img
                self.cursor_image_rect = self.cursor_image.image.get_rect()

        # increment other variables
        self.frames_per_beginning += 1
        self.mouse_click_cooldown += 1


    def render(self, color=pygame.Color(255, 255, 255, 255)):
        self.background.render(self.window.window)
        self.ufo.render(self.window.window)
        for bubble in self.bubbles:
            if bubble.is_bubble_hovered:
                bubble_surface = pygame.transform.scale(self.hovered_bubble_image.image, (bubble.radius, bubble.radius))
            else:
                bubble_surface = pygame.transform.scale(self.bubble_image.image, (bubble.radius, bubble.radius))
            position = (bubble.center[0] - bubble.radius / 2, bubble.center[1] - bubble.radius / 2)
            self.window.window.blit(bubble_surface, position)

        for it in range (0, len(self.animals)):
            if self.animal_chosen != it:
                self.animals[it].render(self.window.window)

        if self.animal_chosen != -1:
            self.window.window.blit(self.cursor_image.image, self.cursor_image_rect)
        self.font.render_text(self.window.window, self.score_text + str(self.score), pygame.Color(255, 255, 255, 255), (100, 50))