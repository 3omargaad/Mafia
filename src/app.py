from kivy.lang import Builder
from kivy.core.window import Window
from kivy import require
# Imports kivy sub-modules

from kivymd.app import MDApp
# Imports kivymd sub-modules

from background import bg

from screen_manager import sm

from screens import setup_screens


require('2.3.1')


Builder.load_file("gui/kivy_gui/app.kv")  # Loads kivy file


class MafiaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = 'Dark'  # Creates red/dark theme
        Window.size = (360, 640)

        root = bg

        setup_screens()

        # Sets up kivy screen manager

        root.add_widget(sm)

        return root


def run():
    MafiaApp().run()
# Runs application GUI
