from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from pathlib import Path

class guiApp(App):
    def build(self):
        self.icon = str(Path("assets\\images\\mafia_logo.ico"))

class guiWidget(Widget):
    outputText = StringProperty("Welcome to Mafia! I am your host ChadGPT.")
    count = 0
    state = BooleanProperty(False)
    #sliderVal = StringProperty("4")

    def on_play(self):
        self.count += 1
        print("Welcome to Mafia! I am your host ChadGPT.")
        self.outputText = str(self.count)
    
    def toggle(self):
        pass

    def on_swtich_active(self, widget):
        print("Switch: " + str(widget.active))
    
    
    #def on_slider_value(self, widget):
    #    self.sliderVal = str(int(widget.value))
    #    print("Value: " + str(int(widget.value)))

class guiMenu(Widget):
    pass

def setup():
    app = guiApp() 
    app.run()
    app.build()

#setup()