from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from pathlib import Path

class guiApp(App):
    def build(self):
        self.icon = str(Path("assets\\images\\mafia_logo.ico"))

class guiWidget(GridLayout):
    outputText = StringProperty("Welcome to Mafia! I am your host ChadGPT.")
    count = 0

    def on_play(self):
        self.count += 1
        print("Welcome to Mafia! I am your host ChadGPT.")
        self.outputText = str(self.count)

def setup():
    app = guiApp() 
    app.run()
    app.build()

setup()