# Program to Show how to create a switch 
# import kivy module    
import kivy  
    
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition, SwapTransition, SlideTransition
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
        game_setup.good_team_num = int(widget.value) - game_setup.bad_team_num
          
    def on_maf_slider_value(self, widget):
        self.maf_num_val = str(int(widget.value))
        game_setup.maf_num = int(widget.value)
        game_setup.bad_team_num = int(widget.value)
        
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
        print(s4)
        count = 1
        for child in s4.children:
            if isinstance(child, TextInput):
                child.disabled = True
                if count == (15 - game_setup.plr_num):
                   break
                count += 1

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
        roboto_font = get_path("assets", "fonts", "RobotoSlab-Medium.ttf")
        
        for i in range(15):
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

            t = TextInput(
                hint_text="Player #"+str(i+1)+" Name",
                size_hint= (0.2, 0.05),
                width= "100dp",
                multiline= False,
                font_name= roboto_font,
                pos_hint={'center_x': x, 'center_y': y},
                disabled= False
                )
            self.add_widget(t)

    def start_game(self):
        count = 0
        for child in s4.children:
            if child.disabled == False and isinstance(child, TextInput):
                print(child.text)
                game_setup.players.append(child.text)
        
        
        #App.get_running_app().stop()
        #app.stop()

class ScreenFive(Screen):
    pass


class Role1(Screen):
    def __init__(self, **kwargs):
        i = 1
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        super().__init__(**kwargs)
        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 2
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 3
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 4
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 5
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role6(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 6
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role7(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 7
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role8(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 8
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role9(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 9
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role10(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 10
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role11(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 11
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role12(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 12
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role13(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 13
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role14(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 14
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )
class Role15(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i = 15
        #def reveal():
        #    root.manager.transition.direction = 'left'
        #    root.manager.transition.duration = 1
        #    root.manager.current = 'role'+str(i+1)

        b = Button(
            text="[Player Name] Press to Check Role"#,
            #on_press= reveal()
        )

class ScreenSix(Screen):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")
    roboto_font = get_path("assets", "fonts", "RobotoSlab-Medium.ttf")
    press_font = get_path("assets", "fonts", "PressStart2P-Regular.ttf")

    info = "Players in game: "

    for plr in game_setup.players:
        info = plr + "Press to check your role..."
        print(plr)

 
# The ScreenManager controls moving between screens
screen_manager = ScreenManager(transition=SlideTransition())

s4 = ScreenFour(name ="screen_four")
 
# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name ="screen_one"))
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three"))
screen_manager.add_widget(s4)
screen_manager.add_widget(ScreenFive(name="screen_five"))
screen_manager.add_widget(ScreenSix(name="screen_six"))

screen_manager.add_widget(Role1(name="role1"))
screen_manager.add_widget(Role2(name="role2"))
screen_manager.add_widget(Role3(name="role3"))
screen_manager.add_widget(Role4(name="role4"))
screen_manager.add_widget(Role5(name="role5"))
screen_manager.add_widget(Role6(name="role6"))
screen_manager.add_widget(Role7(name="role7"))
screen_manager.add_widget(Role8(name="role8"))
screen_manager.add_widget(Role9(name="role9"))
screen_manager.add_widget(Role10(name="role10"))
screen_manager.add_widget(Role11(name="role11"))
screen_manager.add_widget(Role12(name="role12"))
screen_manager.add_widget(Role13(name="role13"))
screen_manager.add_widget(Role14(name="role14"))
screen_manager.add_widget(Role15(name="role15"))

# Create the App class
class MafiaApp(App):
    def build(self):
        icon = get_path("assets", "images", "mafia_logo.ico")

        self.icon = icon
        return screen_manager

app = MafiaApp()
# run the app 
def setup():
    app.run()

setup()