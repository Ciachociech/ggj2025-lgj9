import pygame

import common.Object


class Animal(common.Object):

    def __init__(self, tag, size, image, x_pos):
        super().__init__(tag, image)
        self.size = size
        self.rect = pygame.Rect(x_pos, 592, 128, 128)

    def update_position(self):
        self.rect = pygame.Rect(self.rect[0] - 128, self.rect[1], self.rect[2], self.rect[3])

    def render(self, window, position = (0, 0)):
        super().render(window, (self.rect[0], self.rect[1]) + position)


class Cow(Animal):

    def __init__(self, x_pos):
        super().__init__("CowAnimalObject", 96, "assets/sprites/cow.png", x_pos)

    def render(self, window, position = (0, 0)):
        super().render(window, position)


class Chicken(Animal):

    def __init__(self, x_pos):
        super().__init__("ChickenAnimalObject", 32, "assets/sprites/chicken.png", x_pos)

    def render(self, window, position = (0, 0)):
        super().render(window, position)


class Fox(Animal):

    def __init__(self, x_pos):
        super().__init__("FoxAnimalObject", 56, "assets/sprites/fox.png", x_pos)

    def render(self, window, position = (0, 0)):
        super().render(window, position)


class Deer(Animal):

    def __init__(self, x_pos):
        super().__init__("DeerAnimalObject", 80, "assets/sprites/deer.png", x_pos)

    def render(self, window, position = (0, 0)):
        super().render(window, position)

class Rabbit(Animal):

    def __init__(self, spawn_value, x_pos):
        if spawn_value < 90:
            super().__init__("RabbitAnimalObject", 24, "assets/sprites/rabbit.png", x_pos)
        else:
            super().__init__("RabbitAnimalObject", 24, "assets/sprites/stefan.png", x_pos)

        def render(self, window, position=(0, 0)):
            super().render(window, position)

class Zubr(Animal):

    def __init__(self, x_pos):
        super().__init__("ZubrAnimalObject", 112, "assets/sprites/zubr.png", x_pos)

    def render(self, window, position = (0, 0)):
        super().render(window, position)