from kivy.animation import Animation
from kivy.clock import Clock

from kivymd.uix.screen import MDScreen, Screen

from functools import partial

from concurrency import run_concurrent
from game_setup import game

import assets
import audio


class EndScreen(MDScreen, Screen):
    # rye_font = assets.RYE
    # roboto_font = assets.ROBOTO
    win_img = assets.WIN_IMG
    lose_img = assets.LOSE_IMG
    winning_team = game.winning_team

    def on_enter(self):
        fadein = Animation(opacity=1)

        win = self.ids["win"]
        lose = self.ids["lose"]
        good = self.ids["good"]
        bad = self.ids["bad"]
        info = self.ids["info"]

        maf = ""
        doc = "N/A"
        det = "N/A"

        for plr in game.mafia_players:
            maf += plr.name + " "

        if game.doctor_player:
            doc = game.doctor_player.name

        if game.detective_player:
            det = game.detective_player.name

        info.text = """
        Mafia: """ + maf + """
        Doctor: """ + doc + """
        Detective: """ + det

        winning_team = game.winning_team
        if winning_team == "Good":
            self.result_image = assets.WIN_IMG
            Clock.schedule_once(partial(audio.play_audio, assets.WIN), 1)
            fadein.start(win)
            fadein.start(good)
            print("Good Team win")
        elif winning_team == "Bad":
            self.result_image = assets.LOSE_IMG
            Clock.schedule_once(partial(audio.play_audio, assets.LOSE), 1)
            fadein.start(lose)
            fadein.start(bad)
            print("Bad Team win")

        game.__init__()  # Resets game for the next one

    def on_leave(self):
        fadeout = Animation(opacity=0)

        win = self.ids["win"]
        lose = self.ids["lose"]
        good = self.ids["good"]
        bad = self.ids["bad"]

        fadeout.start(win)
        fadeout.start(good)
        fadeout.start(lose)
        fadeout.start(bad)

    def click(self):
        run_concurrent(audio.play_audio, assets.UI_CLICK)
