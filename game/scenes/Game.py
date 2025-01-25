import math
import random
from enum import IntEnum

import pygame

import audio.Sound
import common.Scene
import drawable.Image
import game.objects.Animal
import game.objects.Background
import game.objects.Bubble
import system.Timer

def resolve_collision(bubble1, bubble2):
    if bubble1.captured_animal_image or bubble2.captured_animal_image:
        return
    if bubble1.rect.colliderect(bubble2.rect):
        if bubble1.radius > bubble2.radius:
            bubble1.prepare_to_delete = True
        elif bubble2.radius > bubble1.radius:
            bubble2.prepare_to_delete = True
        else:
            bubble1.prepare_to_delete = True
            bubble2.prepare_to_delete = True


class GameMode(IntEnum):
    none = 0
    no_limit = 1
    time_limit = 2
    mixed_limit = 3


def calculate_score(size):
    value = int(size / 8)
    value = int(round(value * value / 5))
    if value > 20:
        return value + 1
    return value


class Game(common.Scene):

    def __init__(self, window):
        super().__init__("GameMainScene", window)

        self.frames_per_beginning = 0
        self.score = 0

        self.background = game.objects.Background("assets/sprites/background.png")
        self.ufo = game.objects.Ufo()
        self.bubble_image = drawable.Image("bubble_image", "assets/sprites/bubble.png")
        self.hovered_bubble_image = drawable.Image("bubble_image", "assets/sprites/h_bubble.png")
        self.bubble_boom_tileset = drawable.Image("BoomTilesetImage", "assets/tilesets/bubbleboom.png")
        self.bubbles = []
        self.animals = []

        self.font = drawable.Font("GameFont")
        self.font.load_font_from_file("assets/fonts/Tektur-Regular.ttf", 48)
        self.score_text = "Wynik: "
        self.time_text = "Czas: "

        self.is_left_mouse_clicked = False
        self.is_right_mouse_clicked = False
        self.animal_chosen = -1
        self.mouse_click_cooldown = 0
        self.cursor_image = None
        self.cursor_image_rect = pygame.Rect(0, 0, 0, 0)

        self.keyboard_click_cooldown = None
        self.escape_key_pressed = None

        self.game_mode = None
        self.timer = system.Timer("GameTimer")
        self.time_limit = -1
        self.animals_left = -1

    def set(self, game_mode):
        self.bubbles = []
        self.animals = []
        self.game_mode = game_mode
        self.timer.restart()

        match self.game_mode:
            case GameMode.no_limit:
                self.time_limit = -1
                self.animals_left = -1
            case GameMode.time_limit:
                self.time_limit = 60
                self.animals_left = -1
            case GameMode.mixed_limit:
                self.time_limit = 0
                self.animals_left = 10
            case _:
                self.time_limit = -1
                self.animals_left = -1

        self.resume()
        self.update()

    def resume(self):
        self.keyboard_click_cooldown = 0
        self.escape_key_pressed = False

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        if self.keyboard_click_cooldown > 3 and keyboard_input[pygame.K_ESCAPE]:
            self.escape_key_pressed = True
            return

        self.cursor_image_rect.center = pygame.mouse.get_pos()
        if self.mouse_click_cooldown > 3:
            self.is_left_mouse_clicked = mouse_input[0]
            self.is_right_mouse_clicked = mouse_input[2]

    def update(self):
        # if escape key is pressed
        if self.escape_key_pressed:
            return 1

        # if less than 10 animals, spawn to fill this limit
        while len(self.animals) < 10 and self.animals_left != 0:
            match random.randint(1, 6):
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
                case 6:
                    self.animals.append(game.objects.Zubr(128 * len(self.animals)))
                case _:
                    pass
            if self.game_mode == GameMode.mixed_limit:
                self.time_limit += (self.animals[-1].size // 16)
            self.animals_left -= 1

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
            if bubble.prepare_to_delete and bubble.boom_animation_frames < bubble.bubble_boom_frames_limit:
                continue
            if bubble.captured_animal_image is not None:
                continue
            if pygame.Rect(bubble.center[0] - bubble.radius, bubble.center[1] - bubble.radius, 2 * bubble.radius, 2 * bubble.radius).collidepoint(self.cursor_image_rect.center):
                if self.animal_chosen != -1 and bubble.radius > 2 * self.animals[self.animal_chosen].size / math.sqrt(2):
                    bubble.is_bubble_hovered = True
                    if self.is_left_mouse_clicked:
                        for it in range(self.animal_chosen, len(self.animals)):
                            self.animals[it].update_position()
                        self.score += calculate_score(self.animals[self.animal_chosen].size)
                        bubble.captured_animal_image = self.animals[self.animal_chosen].img.image
                        bubble.change_movement_when_capture()
                        bubble.prepare_to_delete = False

                        del self.animals[self.animal_chosen]
                        self.animal_chosen = -1
                if self.is_left_mouse_clicked and bubble.captured_animal_image is None:
                    bubble.prepare_to_delete = True
                    self.is_left_mouse_clicked = False
                    self.mouse_click_cooldown = 0
            if bubble.prepare_to_delete and bubble.boom_animation_frames >= bubble.bubble_boom_frames_limit:
                self.bubbles.remove(bubble)
        if len(self.bubbles) < 300:
            new_bubble = game.objects.Bubble(random.randint(0, 359), random.randint(1, 5), random.randint(0, 359),
                                             self.bubble_image)
            self.bubbles.append(new_bubble)

        # manage animals
        if self.is_right_mouse_clicked:
            self.animal_chosen = -1
        for it in range (0, len(self.animals)):
            if self.animals[it].rect.collidepoint(pygame.mouse.get_pos()) and self.is_left_mouse_clicked:
                self.animal_chosen = it
                self.cursor_image = self.animals[it].img
                self.cursor_image_rect = self.cursor_image.image.get_rect()

        # increment other variables
        self.frames_per_beginning += 1
        self.mouse_click_cooldown += 1
        self.keyboard_click_cooldown += 1
        self.timer.update_timer()

        # check win and lose conditions
        if self.timer.elapsed_time / 1000 >= self.time_limit:
            match self.game_mode:
                case GameMode.time_limit:
                    return 2
                case GameMode.mixed_limit:
                    return 3

        if self.animals_left == 0 and len(self.animals) == 0:
            return 4

        return 0


    def render(self, color=pygame.Color(255, 255, 255, 255)):
        self.background.render(self.window.window)
        self.ufo.render(self.window.window)
        for bubble in self.bubbles:
            position = None
            if bubble.captured_animal_image:
                self.window.window.blit(bubble.captured_animal_image,
                                        (bubble.center[0] - 64, bubble.center[1] - 64))
            if bubble.is_bubble_hovered and self.animal_chosen != -1 and not bubble.captured_animal_image:
                bubble_surface = pygame.transform.scale(self.hovered_bubble_image.image,
                                                        (1.2 * bubble.radius, 1.2 * bubble.radius))
                position = (bubble.center[0] - 0.6 * bubble.radius, bubble.center[1] - 0.6 * bubble.radius)
                self.window.window.blit(bubble_surface, position)
            elif bubble.prepare_to_delete:
                bubble_surface = pygame.transform.scale(self.bubble_boom_tileset.image,
                                                        (4 * bubble.radius, bubble.radius))
                position = (bubble.center[0] - bubble.radius / 2, bubble.center[1] - bubble.radius / 2)

                rect = (bubble.radius * (bubble.boom_animation_frames // (bubble.bubble_boom_frames_limit // 4)), 0, bubble.radius, bubble.radius)
                self.window.window.blit(bubble_surface, position, rect)
            else:
                bubble_surface = pygame.transform.scale(self.bubble_image.image,
                                                        (bubble.radius, bubble.radius))
                position = (bubble.center[0] - bubble.radius / 2, bubble.center[1] - bubble.radius / 2)
                self.window.window.blit(bubble_surface, position)


        for it in range (0, len(self.animals)):
            if self.animal_chosen != it:
                self.animals[it].render(self.window.window)

        if self.animal_chosen != -1:
            self.window.window.blit(self.cursor_image.image, self.cursor_image_rect)
        self.font.render_text(self.window.window, self.score_text + str(self.score), pygame.Color(255, 255, 255, 255), (8, 8))
        if (self.game_mode is GameMode.time_limit or self.game_mode is GameMode.mixed_limit) and self.timer.elapsed_time / 1000 < self.time_limit:
            self.font.render_text(self.window.window,
                                  self.time_text + "{:4.2f}".format(self.time_limit - self.timer.elapsed_time / 1000) + "s",
                                  pygame.Color(255, 255, 255, 255), (8, 64))