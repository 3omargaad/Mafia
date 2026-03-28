from kivy.lang import Builder
from kivy.core.window import Window
from kivy import require
# Imports kivy sub-modules

from kivymd.app import MDApp
# Imports kivymd sub-modules

from background import bg

import screen_manager

# import screens


require('2.3.1')


Builder.load_file("kivy_gui/app.kv")  # Loads kivy file


class MafiaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = 'Dark'  # Creates red/dark theme
        Window.size = (360, 640)

        root = bg

        screen_manager.setup_screens()

        # Sets up kivy screen manager

        root.add_widget(screen_manager.sm)

        return root


def run():
    MafiaApp().run()
# Runs application GUI
