from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock


class TestScreen(Label):
    def __init__(self, string, **kwargs):
        super(TestScreen, self).__init__(**kwargs)
        self.font_size = 26
        self.string = string
        self.typewriter = Clock.create_trigger(self.typeit, 0.01)
        self.typewriter()

    def typeit(self, dt):
        self.text += self.string[0]
        self.string = self.string[1:]
        if len(self.string) > 0:
            self.typewriter()


class TestApp(App):
    title = "Kivy Typewriter"

    def build(self):
        return TestScreen("That is my Kivy Typewriter demo")


if __name__ == "__main__":
    TestApp().run()
