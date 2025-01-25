import pygame

import common.Object


class Animal(common.Object):

    def __init__(self, tag, size, image, x_pos):
        super().__init__(tag, image)
        self.size = size
        self.position = (x_pos, 592)

    def update(self):
        self.position = (self.position[0] - 128, self.position[1])

    def render(self, window, position = (0, 0)):
        super().render(window, self.position + position)


class Cow(Animal):

    def __init__(self, x_pos):
        super().__init__("CowAnimalObject", 108, "assets/sprites/cow.png", x_pos)

    def render(self, window, position = (0, 0)):
        super().render(window, position)


class Chicken(Animal):

    def __init__(self, x_pos):
        super().__init__("ChickenAnimalObject", 32, "assets/sprites/chicken.png", x_pos)

    def render(self, window, position = (0, 0)):
        super().render(window, position)


class Fox(Animal):

    def __init__(self, x_pos):
        super().__init__("FoxAnimalObject", 64, "assets/sprites/fox.png", x_pos)

    def render(self, window, position = (0, 0)):
        super().render(window, position)


class Deer(Animal):

    def __init__(self, x_pos):
        super().__init__("DeerAnimalObject", 96, "assets/sprites/deer.png", x_pos)

    def render(self, window, position = (0, 0)):
        super().render(window, position)

class Rabbit(Animal):

    def __init__(self, spawn_value, x_pos):
        if spawn_value < 90:
            super().__init__("RabbitAnimalObject", 24, "assets/sprites/rabbit.png", x_pos)
        else:
            super().__init__("RabbitAnimalObject", 16, "assets/sprites/stefan.png", x_pos)

        def render(self, window, position=(0, 0)):
            super().render(window, position)

