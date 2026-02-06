from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Define the first screen
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Home Screen'))
        btn = Button(text='Go to Settings')
        btn.bind(on_press=self.go_to_settings)
        layout.add_widget(btn)
        self.add_widget(layout)
        
    def go_to_settings(self, instance):
        self.manager.current = 'settings'

# Define the second screen
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Settings Screen'))
        btn = Button(text='Go to Home')
        btn.bind(on_press=self.go_to_home)
        layout.add_widget(btn)
        self.add_widget(layout)
        
    def go_to_home(self, instance):
        self.manager.current = 'home'

# Create the Screen Manager
class MyScreenManager(ScreenManager):
    pass

# Main App
class MyApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    MyApp().run()
