# Program to Show how to create a switch 
# import kivy module    
import kivy  
     
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
 
# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenOne(Screen):
    pass
 
class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

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