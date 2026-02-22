from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen 
from kivymd.uix.dialog import MDDialog

from files import get_path

import game_setup

Builder.load_file("app.kv")

class LoginScreen(MDScreen, Screen):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")
    press_font = get_path("assets", "fonts", "PressStart2P-Regular.ttf")
    
    def account(self):
        print("Pressed")
        popup = MDDialog(title='Error', text="Account creation is currently unavailable.")
        popup.open()

    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")
    press_font = get_path("assets", "fonts", "PressStart2P-Regular.ttf")
    
    def account(self):
        print("Pressed")
        popup = MDDialog(title='Error', text="Account creation is currently unavailable.")
        popup.open()

class SetupScreen(MDScreen, Screen):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")
    plr_num = StringProperty("4")
    maf_num = StringProperty("1")

    def on_plr_slider_value(self, widget):
        self.plr_num = str(int(widget.value))
        game_setup.plr_num = int(widget.value)
        print(str(game_setup.plr_num))

    def on_maf_slider_value(self, widget):
        self.maf_num = str(int(widget.value))
        game_setup.maf_num = int(widget.value)
        print(str(game_setup.maf_num))

    def on_include_doc_switch_active(self, widget):
        game_setup.maf_num = widget.active
        print(str(game_setup.include_doc))

    def on_include_det_switch_active(self, widget):
        game_setup.maf_num = widget.active
        print(str(game_setup.include_det))
          
    #def on_maf_slider_value(self, widget):
    #    self.maf_num_val = str(int(widget.value))

class PlayerScreen(MDScreen, Screen):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")


class RoleScreen(MDScreen, Screen):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")


class GameScreen(MDScreen, Screen):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")

class MafiaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = 'Dark' # Creates red/dark theme
        Window.size = (360, 640)

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SetupScreen(name='setup'))
        sm.add_widget(PlayerScreen(name='player'))
        sm.add_widget(RoleScreen(name='role'))
        sm.add_widget(GameScreen(name='game'))

        return sm

#
#
MafiaApp().run()
