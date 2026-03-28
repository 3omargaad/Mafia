from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen, Screen

from concurrency import run_concurrent

import assets
import audio
import host


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
