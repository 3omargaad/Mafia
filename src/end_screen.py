from kivy.animation import Animation
from kivy.clock import Clock

from kivymd.uix.screen import MDScreen, Screen

from functools import partial

from concurrency import run_concurrent
from game_setup import game

import assets
import audio


class EndScreen(MDScreen, Screen):
    rye_font = assets.RYE
    roboto_font = assets.ROBOTO
    win_img = assets.WIN_IMG
    lose_img = assets.LOSE_IMG
    winning_team = game.winning_team

    def on_enter(self):
        fadein = Animation(opacity=1)

        win = self.ids["win"]
        lose = self.ids["lose"]
        good = self.ids["good"]
        bad = self.ids["bad"]

        winning_team = game.winning_team
        if winning_team == "Good":
            self.result_image = assets.WIN_IMG
            fadein.start(win)
            fadein.start(good)
            Clock.schedule_once(partial(audio.play_audio, assets.WIN), 3)
            print("Good Team win")
        elif winning_team == "Bad":
            self.result_image = assets.LOSE_IMG
            fadein.start(lose)
            fadein.start(bad)
            Clock.schedule_once(partial(audio.play_audio, assets.LOSE), 3)
            print("Bad Team win")

        game.__init__()  # Resets game for the next one

    def click(self):
        run_concurrent(audio.play_audio, assets.UI_CLICK)
