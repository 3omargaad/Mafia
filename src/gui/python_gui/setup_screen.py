from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen, Screen

from concurrency import run_concurrent
from game_setup import game
from vibe import vibrate

import assets
import audio


class SetupScreen(MDScreen, Screen):
    # rye_font = assets.RYE
    # roboto_font = assets.ROBOTO
    plr_num = StringProperty("4")
    maf_num = StringProperty("1")
    max_maf = StringProperty("1")

    def on_enter(self):
        plr_num_slider = self.ids['plr_num_slider']
        maf_num_slider = self.ids['maf_num_slider']
        add_doc_switch = self.ids['add_doc_switch']
        add_det_switch = self.ids['add_det_switch']

        game.plr_num = int(plr_num_slider.value)
        game.maf_num = int(maf_num_slider.value)
        game.bad_team_num = game.maf_num
        game.good_team_num = game.plr_num - game.bad_team_num

        game.include_doc = bool(add_doc_switch.active)
        game.include_det = bool(add_det_switch.active)

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
        game.plr_num = int(widget.value)
        game.good_team_num = game.plr_num - game.bad_team_num

        self.max_maf = str((game.plr_num // 2) - 1)  # Sets max mafia val
        print(self.max_maf)

    def on_maf_slider_value(self, widget):
        self.maf_num = str(int(widget.value))
        game.maf_num = int(widget.value)
        game.bad_team_num = int(widget.value)
        game.good_team_num = game.plr_num - game.bad_team_num
        print(str(game.maf_num))

    def on_include_doc_switch_active(self, widget):
        game.include_doc = widget.active
        print(str(game.include_doc))

    def on_include_det_switch_active(self, widget):
        game.include_det = widget.active
        print(str(game.include_det))

    def on_continue(self, widget):
        print(self.ids)
        print(game.plr_num)

    def click(self):
        vibrate()
        run_concurrent(audio.play_audio, assets.UI_CLICK)

    def hover(self, widget):
        widget.bold = True
