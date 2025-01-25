import pygame

import common.Object


class Animal(common.Object):

    def __init__(self, tag, size, image):
        super().__init__(tag, image)
        self.size = size

    def render(self, window, position):
        super().render(window, position)
        '''
        pygame.draw.rect(window.window, pygame.Color(255, 255, 255, 255),
                         pygame.Rect(position[0] - self.size / 2, position[1] - self.size / 2,
                                     position[0] + self.size / 2, position[1] + self.size / 2), 1)
        '''


class Cow(Animal):

    def __init__(self):
        super().__init__("CowAnimalObject", 96, "assets/sprites/cow.png")

    def render(self, window, position):
        super().render(window, position)


class Chicken(Animal):

    def __init__(self):
        super().__init__("ChickenAnimalObject", 64, "assets/sprites/chicken.png")

    def render(self, window, position):
        super().render(window, position)