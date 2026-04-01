from kivy.animation import Animation

from kivymd.uix.screen import MDScreen, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from concurrency import run_concurrent
from narrative import ROLE_DESC

import assets
import audio
import host


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
            text=ROLE_DESC[role] + extra,
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
