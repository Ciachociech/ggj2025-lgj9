import pygame

class Timer:

    def __init__(self, tag):
        self.tag = tag
        self.is_paused = False
        self.inner_timer = pygame.time.Clock()
        self.elapsed_time = 0

    def update_timer(self):
        if not self.is_paused:
            self.elapsed_time += self.inner_timer.tick()
        return self.elapsed_time

    def restart(self):
        time = self.update_timer()
        self.elapsed_time = 0
        return time

    def pause(self):
        self.update_timer()
        self.is_paused = True

    def resume(self):
        self.inner_timer.tick()
        self.is_paused = False
