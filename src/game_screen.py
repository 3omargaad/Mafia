from kivy.animation import Animation
from kivy.clock import Clock

from kivymd.uix.screen import MDScreen, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from functools import partial
from concurrency import run_concurrent
from game_setup import game

import narrative
import assets
import audio
import host

# from host import wait


class GameScreen(MDScreen, Screen):
    rye_font = assets.RYE
    selected_player = ""

    def on_enter(self):
        player_screen = self.manager.get_screen('player')
        game_screen = self.manager.get_screen('game')

        dialogue = game_screen.ids["dialogue"]
        action = game_screen.ids["action"]

        def display(text, *args):
            dialogue.text = text

        def enable_checkboxes(action_text, *args):
            action.text = action_text
            fadein = Animation(opacity=1)

            for i in range(host.game.plr_num):
                check = self.ids["check" + str(i+1)]
                check.disabled = False
                fadein.start(check)

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

        def countdown(t, clock_t):
            for i in range(t+1):
                Clock.schedule_once(partial(display, str(t-i)), clock_t + i)
                Clock.schedule_once(partial(audio.play_audio, assets.UI_POP), clock_t + i)

        def announce(text, audio_file, clock_t):
            Clock.schedule_once(partial(display, text), clock_t)
            Clock.schedule_once(partial(audio.play_audio, audio_file), clock_t)

        announce(narrative.WELCOME, assets.WELCOME, 3)
        announce(narrative.INTRO, assets.INTRO, 8)
        countdown(15, 13)
        announce(narrative.GOODNIGHT, assets.GOODNIGHT, 29)
        announce(narrative.MAFIA, assets.MAFIA, 35)

        Clock.schedule_once(partial(enable_checkboxes, "Eliminate"), 38)

    def on_checkbox_active(self, checkbox, value):

        game_screen = self.manager.get_screen('game')
        action = game_screen.ids["action"]
        action.disabled = not value
        print(str(checkbox.parent.text) + str(value))
        global selected_player
        selected_player = game.get_player(checkbox.parent.text)

    def on_press(self):
        game_screen = self.manager.get_screen('game')
        action = game_screen.ids["action"]
        dialogue = game_screen.ids["dialogue"]

        def display(text, *args):
            dialogue.text = text

        action.disabled = True

        def investigate():
            display(selected_player.name + " is a " + selected_player.role)

        def eliminate():
            selected_player.die()
            display(selected_player.name + " has been eliminated!")

        def heal():
            selected_player.heal()
            display(selected_player.name + " has been healed!")

        match (action.text):
            case "Eliminate":
                eliminate()
                return
            case "Heal":
                heal()
                return
            case "Investigate":
                investigate()
                return

    def on_release(self):
        game_screen = self.manager.get_screen('game')

        dialogue = game_screen.ids["dialogue"]

        def display(text, *args):
            dialogue.text = text

        def announce(text, audio_file, clock_t):
            Clock.schedule_once(partial(display, text), clock_t)
            Clock.schedule_once(partial(audio.play_audio, audio_file), clock_t)

        def disable_checkboxes(*args):
            fadein = Animation(opacity=0)

            for i in range(host.game.plr_num):
                check = self.ids["check" + str(i+1)]
                check.disabled = True
                check.value = False
                fadein.start(check)

        print("Continuing game...")
        disable_checkboxes()
        announce(narrative.MAFIA_SLEEP, assets.MAFIA_SLEEP, 3)

        # print(dialogue.text)
        # def countdown(t):
        #     for i in range(t+1):
        #         dialogue(str(t-i))
        #         wait(1)
        # def eliminate():
        #     print("Somebodies been eliminated!")
        # # audio.play_audio(assets.WELCOME)
        # wait(5)
        # dialogue(narrative.intro)
        # audio.play_audio(assets.INTRO)
        # wait(5)
        # wait(1)
        # dialogue("The night approaches, everyone falls asleep.")
        # audio.play_audio(assets.GOODNIGHT)
        # wait(5)
        # dialogue("The mafia wakes up and chooses who to eliminate tonight!")
        # audio.play_audio(assets.MAFIA)
        # wait(6)
        # # action.disabled = False
        # # action.on_press = eliminate()
        # # action.text = "Eliminate"

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
            text=narrative.QUIT_MSG,
            auto_dismiss=False,
            buttons=[continue_btn, quit_btn],

        )

        def complete_quit(manager):
            popup.dismiss()
            manager.transition.direction = "down"
            manager.current = 'setup'

        def quit_button_pressed(self):
            complete_quit(manager)
            for event in list(Clock._events):
                try:
                    event.cancel()
                except Exception:
                    pass
            Clock._events.clear()

        continue_btn.bind(on_release=popup.dismiss)
        quit_btn.bind(on_release=quit_button_pressed)

        popup.open()
