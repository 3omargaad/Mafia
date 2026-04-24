from kivymd.uix.screen import MDScreen, Screen
from kivymd.uix.dialog import MDDialog

from concurrency import run_concurrent
from vibe import vibrate

import assets
import audio


class LoginScreen(MDScreen, Screen):
    # rye_font = assets.RYE
    # roboto_font = assets.ROBOTO

    def account(self):
        print("Pressed")
        popup = MDDialog(
            title='Oops!',
            text="Account creation is currently unavailable."
        )
        popup.open()
    # Creates a popup window to show account creation is unavaiable

    def hover_on(self, widget):
        widget.bold = True

    def hover_off(self, widget):
        widget.bold = False

    def click(self):
        vibrate()
        run_concurrent(audio.play_audio, assets.UI_CLICK)
