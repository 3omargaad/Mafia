from kivy.animation import Animation
from kivy.clock import Clock

from functools import partial
from random import randint

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


def doctor_stage(*args):
    ui_control.announce(narrative.DOCTOR, assets.DOCTOR, 9)
    game.set_stage("Doctor")
    if game.doctor_player in game.living_players:
        Clock.schedule_once(partial(ui_control.enable_checkboxes, "Heal"), 12)
    else:
        ui_control.announce("Doctor is dead.", None, 15)
        if game.include_det:
            Clock.schedule_once(detective_stage, 15 + randint(1, 7))
        else:
            Clock.schedule_once(voting, 15 + randint(1, 7))


def detective_stage(*args):
    ui_control.announce(narrative.DETECTIVE, assets.DETECTIVE, 9)
    game.set_stage("Detective")
    if game.detective_player in game.living_players:
        Clock.schedule_once(
            partial(ui_control.enable_checkboxes, "Investigate"), 12
        )
    else:
        ui_control.announce("Detective is dead.", None, 15)
        Clock.schedule_once(voting, 15 + randint(1, 7))


def end(*args):
    if game.game_is_over():
        ui_control.announce(narrative.GAME_OVER, assets.GAME_OVER, 1)
        Clock.schedule_once(ui_control.leave, 6)
    else:
        ui_control.announce(narrative.GAME_CONTINUES, assets.GAME_CONTINUES, 1)
        Clock.schedule_once(night, 6)


def voting(*args):
    ui_control.announce(narrative.MORNING, assets.MORNING, 7)
    game.remove_dead_players()
    if len(game.living_players) == len(game.players):
        ui_control.announce(narrative.FORTUNATELY, assets.FORTUNATELY, 11)
    else:
        ui_control.announce(narrative.UNFORTUNATELY, assets.UNFORTUNATELY, 11)
        ui_control.announce(game.last_player_eliminated.name, None, 15)
        Clock.schedule_once(ui_control.remove_card, 15)
        ui_control.announce(narrative.DISCUSS, assets.DISCUSS, 18)
        ui_control.countdown(30, 24)
        Clock.schedule_once(ui_control.remove_card, 55)
    ui_control.announce(narrative.VOTE, assets.VOTE, 58)
    ui_control.announce(
        game.living_players[game.vote_count].name + "'s turn to vote.",
        None,
        62
    )
    Clock.schedule_once(partial(ui_control.enable_checkboxes, "Vote"), 60)
    game.set_stage("Voting")
