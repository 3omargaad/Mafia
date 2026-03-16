from kivy.graphics import Rectangle
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout

from kivy_gradient import Gradient


class BackgroundManager(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos,
                texture=Gradient.vertical(
                    get_color_from_hex("000505"),
                    get_color_from_hex("202020"),
                    get_color_from_hex("000505"),
                )
            )
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
