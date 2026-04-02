from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
OneLineListItem:
    text: "[size=48]One-line item with avatar[/size]"
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()   