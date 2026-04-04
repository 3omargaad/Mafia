from kivy.clock import Clock
from kivy.animation import Animation

from functools import partial

from game_setup import game

import audio
import assets

current_screen = None


def display(text, *args):
    dialogue = current_screen.ids["dialogue"]

    dialogue.text = text


def countdown(t, clock_t):
    for i in range(t+1):
        Clock.schedule_once(partial(display, str(t-i)), clock_t + i)
        Clock.schedule_once(
            partial(audio.play_audio, assets.UI_POP),
            clock_t + i
        )


def disable_checkboxes(*args):
    fadein = Animation(opacity=0)

    for i in range(game.plr_num):
        check = current_screen.ids["check" + str(i+1)]
        check.active = False
        check.state = "normal"
        check.disabled = True
        check.value = False
        fadein.start(check)


def enable_checkboxes(action_text, *args):
    action = current_screen.ids["action"]

    action.text = action_text
    fadein = Animation(opacity=1)

    for i in range(game.plr_num):
        check = current_screen.ids["check" + str(i+1)]
        check.disabled = False
        fadein.start(check)


def announce(text, audio_file, clock_t):
    Clock.schedule_once(partial(display, text), clock_t)
    if audio_file:
        Clock.schedule_once(partial(audio.play_audio, audio_file), clock_t)


def reveal_votes(*args):
    fadein = Animation(opacity=1)

    for i in range(game.plr_num):
        n = str(i+1)
        card = current_screen.ids["name" + n]
        vote = current_screen.ids["vote" + n]
        if not card.disabled:
            vote_num = game.get_player(card.text).votes
            if vote_num > 9:
                vote.icon = "numeric-9-plus-circle-outline"
            else:
                vote.icon = "numeric-" + str(vote_num) + "-circle-outline"
            fadein.start(vote)


def remove_votes(*args):
    fadeout = Animation(opacity=0)

    for i in range(game.plr_num):
        n = str(i+1)
        card = current_screen.ids["name" + n]
        vote = current_screen.ids["vote" + n]
        if not card.disabled:
            fadeout.start(vote)

    game.reset_votes()


def remove_card(*args):
    fadeout = Animation(opacity=0)

    for i in range(game.plr_num):
        n = str(i+1)
        card = current_screen.ids["name" + n]
        if game.get_player(card.text).is_alive is False:
            card.disabled = True
            fadeout.start(card)
