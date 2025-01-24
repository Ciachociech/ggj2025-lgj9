import common.Object


class Bubble(common.Object):

    def __init__(self):
        super().__init__("BubbleObject", "assets/sprites/Bubble.png")
        self.position = (640, 360)

    def render(self, window, position_translation = (0, 0)):
        super().render(window, self.position + position_translation)