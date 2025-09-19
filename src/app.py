from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from pathlib import Path
from kivy.core.window import Window
from kivy.config import Config

from files import get_path
#Window.fullscreen = 'auto'  # Let Kivy choose best full screen mode

class guiApp(App):
    def build(self):
        icon = get_path("assets", "images", "mafia_logo.ico")

        self.icon = icon

    def on_stop(self):
        print("App is closing. Cleaning up...")
        # Perform any necessary cleanup here (e.g., closing files, saving data, etc.)
        return super().on_stop()

    def on_request_close(self, instance, value):
        print("Window close requested")
        self.stop()  # Stops the app cleanly
        return True  # Return True to indicate that the close event is handled

#class stackLayout(StackLayout):
#    def __init__(self, **kwargs):
#        super().__init__(**kwargs)
#        b = Button(text="Z")
#        self.add_widget(b)

class guiWidget(FloatLayout):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")
    roboto_font = get_path("assets", "fonts", "RobotoSlab-Medium.ttf")
    press_font = get_path("assets", "fonts", "PressStart2P-Regular.ttf")

    outputText = StringProperty("Welcome to Mafia! I am your host ChadGPT.")
    count = 0
    state = BooleanProperty(False)

    plr_num_val = StringProperty("4")
    maf_num_val = StringProperty("1")

    include_doc_val = BooleanProperty(False)
    include_det_val = BooleanProperty(False)

    def on_play(self):
        global plr_num_val
        global maf_num_val
        #global include_doc_val
        #global include_det_val
        plr_num_val = int(self.plr_num_val)
        maf_num_val = int(self.maf_num_val)
        include_doc_val = bool(self.include_doc_val)
        include_det_val = bool(self.include_det_val)
        app.stop()
        
    def toggle(self):
        pass

    def on_doc_swtich_active(self, widget):
        print("Include Doctor? " + str(widget.active))
        global include_doc_val
        include_doc_val = widget.active
    
    def on_det_swtich_active(self, widget):
        print("Include Detective? " + str(widget.active))
        global include_det_val
        include_det_val = widget.active
    
    def on_plr_slider_value(self, widget):
        self.plr_num_val = str(int(widget.value))
          
    def on_maf_slider_value(self, widget):
        self.maf_num_val = str(int(widget.value))

class guiMenu(FloatLayout):
    pass


def start():
    return (plr_num_val, maf_num_val, include_doc_val, include_det_val)

def setup():
    global app
    app = guiApp() 
    app.run()
    app.build()