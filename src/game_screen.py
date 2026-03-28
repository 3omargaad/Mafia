from kivy.animation import Animation

from kivymd.uix.screen import MDScreen, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from concurrency import run_concurrent

import narrative
import assets
import audio
import host

from host import wait


class GameScreen(MDScreen, Screen):
    rye_font = assets.RYE

    def on_enter(self):
        player_screen = self.manager.get_screen('player')

        fadein = Animation(opacity=1)

        for i in range(host.game.plr_num):
            n = str(i+1)
            card = self.ids["name" + n]

            card.text = player_screen.ids["name" + n].text
            card.disabled = False
            fadein.start(card)

        for i in range(16):
            n = str(i+1)
            card = self.ids["name" + n]

            if player_screen.ids["name" + n].text == "":
                card.opacity = 0
                card.disabled = True

    def start_game(self):
        game_screen = self.manager.get_screen('game')
        # action = game_screen.ids["action"]

        dialogue = game_screen.ids["dialogue"]

        def announce(text):
            dialogue.text = text

        # Clock.schedule_once(partial(announce, "I changed that sentence"), 3)
        # Clock.schedule_once(partial(announce, "EEEEEEEEEE"), 5)
        # Clock.schedule_once(partial(announce, "6767"), 6)
        # Clock.schedule_once(partial(announce, "sOME OTHER RANDOM "), 7)

        print(dialogue.text)

        def countdown(t):
            for i in range(t+1):
                announce(str(t-i))
                wait(1)

        def eliminate():
            print("Somebodies been eliminated!")

        # audio.play_audio(assets.WELCOME)
        wait(5)
        announce(narrative.intro)
        audio.play_audio(assets.INTRO)
        wait(5)
        wait(1)
        announce("The night approaches, everyone falls asleep.")
        audio.play_audio(assets.GOODNIGHT)
        wait(5)
        announce("The mafia wakes up and chooses who to eliminate tonight!")
        audio.play_audio(assets.MAFIA)
        wait(6)
        # action.disabled = False
        # action.on_press = eliminate()
        # action.text = "Eliminate"

    def click(self):
        run_concurrent(audio.play_audio, assets.UI_CLICK)

    def hover(self, widget):
        widget.bold = True

    def quit(self, widget):
        manager = widget.parent.parent
        continue_btn = MDFlatButton(
            text="Continue"
        )

        quit_btn = MDFlatButton(
            text="Quit",
            theme_text_color="Custom",
            text_color=self.theme_cls.primary_color,
        )

        popup = MDDialog(
            title="Quit Game",
            text=narrative.quit_msg,
            auto_dismiss=False,
            buttons=[continue_btn, quit_btn],

        )

        def complete_quit(manager):
            popup.dismiss()
            manager.transition.direction = "down"
            manager.current = 'setup'

        def quit_button_pressed(self):
            complete_quit(manager)

        continue_btn.bind(on_release=popup.dismiss)
        quit_btn.bind(on_release=quit_button_pressed)

        popup.open()
