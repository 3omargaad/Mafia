# Program to Show how to create a switch 
# import kivy module    
import kivy  
    
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.stacklayout import StackLayout
from kivy.uix.popup import Popup
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

class ScreenThree(Screen, FloatLayout, GridLayout):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")
    roboto_font = get_path("assets", "fonts", "RobotoSlab-Medium.ttf")
    press_font = get_path("assets", "fonts", "PressStart2P-Regular.ttf")
    main_image = get_path("assets", "images", "mafia_logo.png")

    outputText = StringProperty("Welcome to Mafia! I am your host ChadGPT.")
    count = 0
    state = BooleanProperty(False)

    plr_num_val = StringProperty("4")
    maf_num_val = StringProperty("1")

    include_doc_val = BooleanProperty(False)
    include_det_val = BooleanProperty(False)

class ScreenFour(Screen):
    pass
 
 
# The ScreenManager controls moving between screens
screen_manager = ScreenManager()
 
# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name ="screen_one"))
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three"))
screen_manager.add_widget(ScreenFour(name ="screen_four"))

# Create the App class
class MafiaApp(App):
    def build(self):
        icon = get_path("assets", "images", "mafia_logo.ico")

        self.icon = icon
        return screen_manager

# run the app 
sample_app = MafiaApp()
sample_app.run()