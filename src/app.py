from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from pathlib import Path

class guiApp(App):
    def build(self):
        self.icon = str(Path("assets\\images\\mafia_logo.ico"))

class guiWidget(GridLayout):
    def on_play(self):
        print("Welcome to Mafia! I am your host ChadGPT.")

def setup():
    app = guiApp() 
    app.run()
    app.build()

setup()