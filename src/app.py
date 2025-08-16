from kivy.app import App
from kivy.uix.widget import Widget
from pathlib import Path

class guiApp(App):
    def build(self):
        self.icon = str(Path("assets\\images\\mafia_logo.ico"))

class guiWidget(Widget):
    pass

if __name__ == "__main__":
    app = guiApp() 
    app.run()
    app.build()