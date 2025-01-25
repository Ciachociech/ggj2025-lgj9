import pygame

import common.Object


class Animal(common.Object):

    def __init__(self, tag, size, image):
        super().__init__(tag, image)
        self.size = size

    def render(self, window, position):
        super().render(window, position)


class Cow(Animal):

    def __init__(self):
        super().__init__("CowAnimalObject", 80, "assets/sprites/cow.png")

    def render(self, window, position):
        super().render(window, position)


class Chicken(Animal):

    def __init__(self):
        super().__init__("ChickenAnimalObject", 64, "assets/sprites/chicken.png")

    def render(self, window, position):
        super().render(window, position)