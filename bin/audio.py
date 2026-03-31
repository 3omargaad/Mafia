from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


class T(App):
    def build(self):
        btn = Button(text='Play')
        self.sound = SoundLoader.load('assets/audio/preset/common/test.ogg')
        btn.bind(on_press=lambda *a: self.sound.play())
        return btn


if __name__ == '__main__':
    T().run()
