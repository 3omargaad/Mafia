from kivy.properties import StringProperty
from kivy.animation import Animation

from kivymd.uix.screen import Screen, MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.screenmanager import ScreenManager

from concurrency import run_concurrent
from narrative import description
from host import wait

import assets
import audio
import host
import narrative

sm = ScreenManager()


class LoginScreen(MDScreen, Screen):
    rye_font = assets.RYE

    def account(self):
        print("Pressed")
        popup = MDDialog(
            title='Error',
            text="Account creation is currently unavailable."
        )
        popup.open()
    # Creates a popup window to show account creation is unavaiable

    def hover_on(self, widget):
        widget.bold = True

    def hover_off(self, widget):
        widget.bold = False

    def click(self):
        run_concurrent(audio.play_audio, assets.UI_CLICK)


class SetupScreen(MDScreen, Screen):
    rye_font = assets.RYE
    plr_num = StringProperty("4")
    maf_num = StringProperty("1")
    max_maf = StringProperty("1")

    def hover_on(self, widget):
        widget.bold = True

    def hover_off(self, widget):
        widget.bold = False

    def slide(self):
        run_concurrent(audio.play_audio, assets.UI_POP)

    def toggle(self, widget):
        if widget.active:
            run_concurrent(audio.play_audio, assets.UI_ENABLE)
        else:
            run_concurrent(audio.play_audio, assets.UI_DISABLE)

    def on_plr_slider_value(self, widget):
        self.plr_num = str(int(widget.value))
        host.game.plr_num = int(widget.value)

        self.max_maf = str((host.game.plr_num // 2) - 1)  # Sets max mafia val
        print(self.max_maf)

    def on_maf_slider_value(self, widget):
        self.maf_num = str(int(widget.value))
        host.game.maf_num = int(widget.value)
        print(str(host.game.maf_num))

    def on_include_doc_switch_active(self, widget):
        host.game.include_doc = widget.active
        print(str(host.game.include_doc))

    def on_include_det_switch_active(self, widget):
        host.game.include_det = widget.active
        print(str(host.game.include_det))

    def on_continue(self, widget):
        print(self.ids)
        print(host.game.plr_num)

    def click(self):
        run_concurrent(audio.play_audio, assets.UI_CLICK)

    def hover(self, widget):
        widget.bold = True


class PlayerScreen(MDScreen, Screen):
    rye_font = assets.RYE

    def on_enter(self):
        player_screen = self.manager.get_screen('player')

        host.game.clear_player_list()
        fadein = Animation(opacity=1)

        for i in range(host.game.plr_num):
            text_field = self.ids["name" + str(i+1)]
            text_field.disabled = False
            fadein.start(text_field)

        for i in range(host.game.plr_num):
            text_field = self.ids["name" + str(i+1)]
            if text_field.text == "":
                player_screen.ids.play.disabled = True
                break
            else:
                player_screen.ids.play.disabled = False

    def validate_text(self, widget):
        player_screen = self.manager.get_screen('player')

        for i in range(host.game.plr_num):
            plr_name = self.ids["name" + str(i+1)].text

            if plr_name == "":
                player_screen.ids.play.disabled = True
                break
            else:
                player_screen.ids.play.disabled = False

    def on_leave(self):

        def create_players(self):
            for i in range(host.game.plr_num):
                plr_name = self.ids["name" + str(i+1)].text
                print(plr_name)
                host.game.create_player(plr_name)
                print(host.game.players)

        create_players(self)
        host.assign_roles()

        for plr in host.game.players:
            print(plr.name + "|" + plr.role)

        for i in range(16):
            self.ids["name" + str(i+1)].disabled = True
            self.ids["name" + str(i+1)].opacity = 0

    def click(self):
        run_concurrent(audio.play_audio, assets.UI_CLICK)

    def hover(self):
        self.bold = True


class RoleScreen(MDScreen, Screen):
    rye_font = assets.RYE

    def on_enter(self):
        player_screen = self.manager.get_screen('player')
        role_screen = self.manager.get_screen('role')
        print(host.game.players)
        role_screen.ids.play.disabled = True

        fade_in = Animation(opacity=1)

        for card in role_screen.ids["cards"].children:
            if card.value is not None and card.value <= host.game.plr_num:
                card.disabled = False
                fade_in.start(card)

        for i in range(host.game.plr_num):
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            n = str(i+1)
            initial = player_screen.ids["name" + n].text[0].lower()
            icon = self.ids["icon" + n]

            self.ids["name" + n].text = player_screen.ids["name" + n].text
            if initial in alphabet:
                icon.icon = "alpha-" + initial + "-circle-outline"
        # for i in range(host.game.plr_num):
        #     self.ids["name" + str(i+1)].disabled = False

    def on_leave(self):
        role_screen = self.manager.get_screen('role')

        for card in role_screen.ids["cards"].children:
            if card.value is not None:
                card.disabled = True
                card.opacity = 0

    def show_role(self, card):
        role_screen = self.manager.get_screen('role')

        print("Pressed")
        print(card.value)
        role = host.game.players[int(card.value) - 1].role
        extra = " Once this tab closes it won't open again."
        close_btn = MDFlatButton(
            text="Finish",
            theme_text_color="Custom",
            text_color=self.theme_cls.primary_color,
        )

        popup = MDDialog(
            title='You are ' + role,
            text=description[role] + extra,
            auto_dismiss=False,
            buttons=[close_btn],

        )

        close_btn.bind(on_release=popup.dismiss)

        popup.open()
        card.disabled = True
        print(role_screen.ids)
        for card in role_screen.ids["cards"].children:
            if card.value is not None:
                if bool(card.disabled) is False:
                    role_screen.ids.play.disabled = True
                    break
                else:
                    role_screen.ids.play.disabled = False
    # Creates a popup window to show account creation is unavaiable

    def click(self):
        run_concurrent(audio.play_audio, assets.UI_CLICK)

    def hover(self, widget):
        widget.bold = True


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

        dialogue = game_screen.ids["dialogue"]
        action = game_screen.ids["action"]

        def announce(text):
            dialogue.text = text

        def countdown(t):
            for i in range(t+1):
                announce(str(t-i))
                wait(1)

        def eliminate():
            print("Somebodies been eliminated!")

        print("The quick brown fox jumped over the lazy dog.")
        print("The quick brown fox jumped over the lazy dog.")
        # audio.play_audio(assets.WELCOME)
        wait(5)
        print(narrative.intro)
        # audio.play_audio(assets.INTRO)
        wait(5)
        countdown(15)
        wait(1)
        print("The night approaches, everyone falls asleep.")
        wait(5)
        print("The mafia wakes up and chooses who to eliminate tonight!")
        wait(6)
        action.disabled = False
        action.on_press = eliminate()
        action.text = "Eliminate"

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
