from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRoundFlatButton, MDRectangleFlatButton, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd import GridLayout


Builder.load_file("gui.kv")

class Login(GridLayout):
    return

class Mafia(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = 'Dark' # Creates red/dark theme
        #screen = Screen()
        #btn = MDRoundFlatButton(text="Hello kivymd World!!", pos_hint={'center_x':0.5, 'center_y':0.5})
        #btn2 = MDRectangleFlatButton(text="Hello kivymd World!!", pos_hint={'center_x':0.5, 'center_y':0.4})
        #btn3 = MDIconButton(icon='language-python', pos_hint={'center_x':0.5, 'center_y':0.3})
        #tf = MDTextField(hint_text="Host Accent", text="uk", helper_text="(au, uk, us, ca, in, za, ng)", icon_right='speech', helper_text_mode="persistent", pos_hint={'center_x':0.5, 'center_y':0.2}, size_hint={0.5, 0.2})
        #screen.add_widget(btn)
        #screen.add_widget(btn2)
        #screen.add_widget(btn3)
        #screen.add_widget(tf)
    return Login()

Mafia().run()