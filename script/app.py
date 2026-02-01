from kivy.lang import Builder
from kivy.core.window import Window
#from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from files import get_path

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

class MafiaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = 'Dark' # Creates red/dark theme
        Window.size = (360, 640)

        return LoginScreen()

#
#sm = ScreenManager()
#
#sm.add_widget(LoginScreen(name='login'))
#sm.add_widget(SetupScreen(name='setup'))
#
MafiaApp().run()
