from kivy.animation import Animation

from kivymd.uix.screen import MDScreen, Screen

from concurrency import run_concurrent

import assets
import audio
import host


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
        names = []

        for i in range(host.game.plr_num):
            plr_name = self.ids["name" + str(i+1)].text
            names.append(plr_name)

        # Places all the names in a list for easier duplicate checking

        for plr_name in names:
            blank = plr_name == ""  # Condition for blank
            duplicate = names.count(plr_name) > 1  # Condition for duplicate
            print("blank:" + str(blank))
            print("duplicate: " + str(duplicate))
            if blank or duplicate:
                player_screen.ids.play.disabled = True
                break
                # Disables play button
            else:
                player_screen.ids.play.disabled = False
                # Enabled play button

        # Validation to prevent empty names and duplicate names

        names.clear()  # Clears list to prevent errors

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
