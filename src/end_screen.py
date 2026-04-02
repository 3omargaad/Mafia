from kivy.clock import Clock

from kivymd.uix.screen import MDScreen, Screen

from functools import partial

from concurrency import run_concurrent

import assets
import audio


class EndScreen(MDScreen, Screen):
    rye_font = assets.RYE
    roboto_font = assets.ROBOTO
    result_image = assets.WIN_IMG

    def on_enter(self):
        Clock.schedule_once(partial(audio.play_audio, assets.WIN), 3)
        # Clock.schedule_once(partial(audio.play_audio, assets.LOSE), 8)

    def click(self):
        run_concurrent(audio.play_audio, assets.UI_CLICK)
