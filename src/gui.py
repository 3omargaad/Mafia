# Program to Show how to create a switch 
# import kivy module    
import kivy  
    
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
# base Class of your App inherits from the App class.    
# app:always refers to the instance of your application   
from kivy.app import App 
from files import get_path
   
# this restrict the kivy version i.e  
# below this kivy version you cannot  
# use the app or software  
kivy.require('1.9.0')

# Builder is used when .kv file is
# to be used in .py file
from kivy.lang import Builder

# The screen manager is a widget
# dedicated to managing multiple screens for your application.
from kivy.uix.screenmanager import ScreenManager, Screen

import game_setup

Builder.load_file("login.kv")
Builder.load_file("account.kv")
Builder.load_file("setup.kv")
Builder.load_file("game.kv")

# class to call the popup function
class PopupWindow(Widget):
    def btn(self):
        popFun()

# class to build GUI for a popup window
class P(FloatLayout):
    pass

# function that displays the content
def popFun():
    show = P()
    window = Popup(title = "Error", content = show,
                   size_hint = (None, None), size = (300, 300))
    window.open()
 
# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenOne(Screen):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")
    roboto_font = get_path("assets", "fonts", "RobotoSlab-Medium.ttf")
    press_font = get_path("assets", "fonts", "PressStart2P-Regular.ttf")
    main_image = get_path("assets", "images", "mafia_logo.png")

    username = ""
    password = ""

    def accountSetup(self):
        #print(self.username.text + " | " + self.password.text)
        popFun()

    def userVal(self):
        pass

    def pwdVal(self):
        pass
 
class ScreenTwo(Screen):
    pass

play = False

class ScreenThree(Screen, FloatLayout, GridLayout):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")
    roboto_font = get_path("assets", "fonts", "RobotoSlab-Medium.ttf")
    press_font = get_path("assets", "fonts", "PressStart2P-Regular.ttf")

    outputText = StringProperty("Welcome to Mafia! I am your host ChadGPT.")
    count = 0
    state = BooleanProperty(False)

    plr_num_val = StringProperty("4")
    maf_num_val = StringProperty("1")
    discussion_time_val = StringProperty("30")

    def toggle(self):
        pass

    def on_plr_slider_value(self, widget):
        self.plr_num_val = str(int(widget.value))
        game_setup.plr_num = int(widget.value)
          
    def on_maf_slider_value(self, widget):
        self.maf_num_val = str(int(widget.value))
        game_setup.maf_num = int(widget.value)
        
    def on_time_slider_value(self, widget):
        self.discussion_time_val = str(int(widget.value))
        game_setup.discussion_time = int(widget.value)

    def on_doc_swtich_active(self, widget):
        game_setup.include_doc = widget.active
    
    def on_det_swtich_active(self, widget):
        game_setup.include_det = widget.active

    def on_anonymous_swtich_active(self, widget):
        game_setup.anonymous_voting = widget.active
        
    def on_skip_swtich_active(self, widget):
        game_setup.allow_skip = widget.active
    
    def on_execute_swtich_active(self, widget):
        game_setup.execute_if_tie = widget.active
    
    def on_host_name_enter(self, widget):
        game_setup.host_name = widget.text

    def on_host_accent_enter(self, widget):
        game_setup.host_accent = widget.text

    def on_play(self):
        print("Player Number:", game_setup.plr_num)
        print("Mafia Number:", game_setup.maf_num)
        print("Discussion Time:", game_setup.discussion_time)
        print("Include Doctor?", game_setup.include_doc)
        print("Include Detective?", game_setup.include_det)
        print("Anonymous Voting?", game_setup.anonymous_voting)
        print("Allow Skip?", game_setup.allow_skip)
        print("Execute If Tie?", game_setup.execute_if_tie)
        print("Host Name:", game_setup.host_name)
        print("Host Accent:", game_setup.host_accent)

class ScreenFour(Screen, StackLayout):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")
    roboto_font = get_path("assets", "fonts", "RobotoSlab-Medium.ttf")
    press_font = get_path("assets", "fonts", "PressStart2P-Regular.ttf")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        for i in range(game_setup.plr_num):
            x = 0.3
            y = 0.85 - (i/15)
            match (i+1):
                case 1 | 2 | 3:
                    y = 0.85 - (1/15)
                case 4 | 5 | 6:
                    y = 0.85 - (2/15)
                case 7 | 8 | 9:
                    y = 0.85 - (3/15)
                case 10 | 11 | 12:
                    y = 0.85 - (4/15)
                case 13 | 14 | 15:
                    y = 0.85 - (5/15)

            if (i+1)%3 == 0:
                x=0.7
            elif (i+2)%3 == 0:
                x=0.5

            print(str(x), str(y))
            t = TextInput(
                hint_text="Player #"+str(i+1)+" Name",
                size_hint= (0.2, 0.05),
                width= "100dp",
                multiline= False,
                pos_hint={'center_x': x, 'center_y': y}
                )
            self.add_widget(t)

class ScreenFive(Screen):
    pass
 
# The ScreenManager controls moving between screens
screen_manager = ScreenManager()
 
# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name ="screen_one"))
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three"))
screen_manager.add_widget(ScreenFour(name ="screen_four"))
screen_manager.add_widget(ScreenFour(name ="screen_five"))

# Create the App class
class MafiaApp(App):
    def build(self):
        icon = get_path("assets", "images", "mafia_logo.ico")

        self.icon = icon
        return screen_manager

# run the app 
sample_app = MafiaApp()
sample_app.run()