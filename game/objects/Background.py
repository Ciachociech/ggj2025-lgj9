import common.Object

class Background(common.Object):

    def __init__(self):
        super().__init__("BackgroundObject", "assets/sprites/background.png")
        self.position = (0, 0)

    def render(self, window, position = (0, 0)):
        super().render(window, position)
