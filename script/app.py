from kivy.lang import Builder
# from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
from kivy import require
# Imports kivy sub-modules

from kivymd.app import MDApp
# Imports kivymd sub-modules

from background import bg
from files import get_path

import screens

require('2.3.1')


Builder.load_file(get_path("script", "kivy_gui", "app.kv"))  # Loads kivy file


class MafiaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = 'Dark'  # Creates red/dark theme
        Window.size = (360, 640)

        root = bg

        screens.sm.add_widget(screens.LoginScreen(name='login'))
        screens.sm.add_widget(screens.SetupScreen(name='setup'))
        screens.sm.add_widget(screens.PlayerScreen(name='player'))
        screens.sm.add_widget(screens.RoleScreen(name='role'))
        screens.sm.add_widget(screens.GameScreen(name='game'))
        # Sets up kivy screen manager

        root.add_widget(screens.sm)

        return root


MafiaApp().run()
# Runs application GUI
