from kivy.animation import Animation
from kivy.clock import Clock

from functools import partial

from screen_manager import sm
from game_setup import game

import narrative
import assets
import ui_control


def night(*args):
    ui_control.announce(narrative.NIGHT, assets.NIGHT, 3)
    ui_control.announce(narrative.MAFIA, assets.MAFIA, 7)
    game.set_stage("Mafia")
    Clock.schedule_once(partial(ui_control.enable_checkboxes, "Eliminate"), 10)


def intro():
    player_screen = sm.get_screen('player')
    game_screen = sm.get_screen('game')

    fadein = Animation(opacity=1)

    for i in range(game.plr_num):
        n = str(i+1)
        card = game_screen.ids["name" + n]
        card.text = player_screen.ids["name" + n].text
        card.disabled = False
        fadein.start(card)

    for i in range(16):
        n = str(i+1)
        card = game_screen.ids["name" + n]
        if player_screen.ids["name" + n].text == "":
            card.opacity = 0
            card.disabled = True

    ui_control.announce(narrative.WELCOME, assets.WELCOME, 3)
    ui_control.announce(narrative.INTRO, assets.INTRO, 8)
    ui_control.countdown(15, 13)
    ui_control.announce(narrative.NIGHT, assets.NIGHT, 29)
    ui_control.announce(narrative.MAFIA, assets.MAFIA, 35)
    game.set_stage("Mafia")
    Clock.schedule_once(partial(ui_control.enable_checkboxes, "Eliminate"), 38)
