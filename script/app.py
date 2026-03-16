from kivy.lang import Builder
# from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
from kivy import require
# Imports kivy sub-modules

from kivymd.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
# Imports kivymd sub-modules

from background import BackgroundManager

import screens

require('2.3.1')

Builder.load_file("app.kv")  # Loads kivy file


class MafiaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = 'Dark'  # Creates red/dark theme
        Window.size = (360, 640)

        root = BackgroundManager()
        sm = ScreenManager()

        sm.add_widget(screens.LoginScreen(name='login'))
        sm.add_widget(screens.SetupScreen(name='setup'))
        sm.add_widget(screens.PlayerScreen(name='player'))
        sm.add_widget(screens.RoleScreen(name='role'))
        sm.add_widget(screens.GameScreen(name='game'))
        # Sets up kivy screen manager

        root.add_widget(sm)

        return root


MafiaApp().run()
# Runs application GUI
