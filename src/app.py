from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from pathlib import Path
from kivy.core.window import Window
from kivy.config import Config

#Window.fullscreen = 'auto'  # Let Kivy choose best full screen mode

class guiApp(App):
    def build(self):
        self.icon = str(Path("assets\\images\\mafia_logo.ico"))

    def on_stop(self):
        print("App is closing. Cleaning up...")
        # Perform any necessary cleanup here (e.g., closing files, saving data, etc.)
        return super().on_stop()

    def on_request_close(self, instance, value):
        print("Window close requested")
        self.stop()  # Stops the app cleanly
        return True  # Return True to indicate that the close event is handled


class guiWidget(FloatLayout):
    outputText = StringProperty("Welcome to Mafia! I am your host ChadGPT.")
    count = 0
    state = BooleanProperty(False)

    plr_num_val = StringProperty("4")
    maf_num_val = StringProperty("1")

    def on_play(self):
        global plr_num_val
        global maf_num_val
        plr_num_val = int(self.plr_num_val)
        maf_num_val = int(self.maf_num_val)
        app.stop()
        
    def toggle(self):
        pass

    def on_swtich_active(self, widget):
        print("Switch: " + str(widget.active))
    
    
    def on_plr_slider_value(self, widget):
        self.plr_num_val = str(int(widget.value))
    
    def on_maf_slider_value(self, widget):
        self.maf_num_val = str(int(widget.value))

class guiMenu(FloatLayout):
    pass


def start():
    return (plr_num_val, maf_num_val)

def setup():
    global app
    app = guiApp() 
    app.run()
    app.build()
