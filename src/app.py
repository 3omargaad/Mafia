from kivy.app import App
from pathlib import Path

class mainApp(App):
    def build(self):
        self.icon = str(Path("assets\\images\\mafia_logo.ico"))


if __name__ == "__main__":
    app = mainApp()
    app.run()