from kivy.animation import Animation
from kivy.clock import Clock

from functools import partial

from screen_manager import sm
from game_setup import game

import narrative
import assets
import audio
import host


def night(*args):
    game_screen = sm.get_screen('game')
    dialogue = game_screen.ids["dialogue"]
    action = game_screen.ids["action"]

    def enable_checkboxes(action_text, *args):
        action.text = action_text
        fadein = Animation(opacity=1)
        for i in range(host.game.plr_num):
            check = game_screen.ids["check" + str(i+1)]
            check.disabled = False
            fadein.start(check)

    def announce(text, audio_file, clock_t):
        Clock.schedule_once(partial(display, text), clock_t)
        Clock.schedule_once(partial(audio.play_audio, audio_file), clock_t)

    def display(text, *args):
        dialogue.text = text

    announce(narrative.NIGHT, assets.NIGHT, 3)
    announce(narrative.MAFIA, assets.MAFIA, 7)
    game.set_stage("Mafia")
    Clock.schedule_once(partial(enable_checkboxes, "Eliminate"), 10)


def intro():
    player_screen = sm.get_screen('player')
    game_screen = sm.get_screen('game')
    dialogue = game_screen.ids["dialogue"]
    action = game_screen.ids["action"]

    def enable_checkboxes(action_text, *args):
        action.text = action_text
        fadein = Animation(opacity=1)
        for i in range(host.game.plr_num):
            check = game_screen.ids["check" + str(i+1)]
            check.disabled = False
            fadein.start(check)

    def announce(text, audio_file, clock_t):
        Clock.schedule_once(partial(display, text), clock_t)
        Clock.schedule_once(partial(audio.play_audio, audio_file), clock_t)

    def display(text, *args):
        dialogue.text = text

    fadein = Animation(opacity=1)

    for i in range(host.game.plr_num):
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

    def countdown(t, clock_t):
        for i in range(t+1):
            Clock.schedule_once(partial(display, str(t-i)), clock_t + i)
            Clock.schedule_once(
                partial(audio.play_audio, assets.UI_POP),
                clock_t + i
            )

    announce(narrative.WELCOME, assets.WELCOME, 3)
    announce(narrative.INTRO, assets.INTRO, 8)
    countdown(15, 13)
    announce(narrative.NIGHT, assets.NIGHT, 29)
    announce(narrative.MAFIA, assets.MAFIA, 35)
    game.set_stage("Mafia")
    Clock.schedule_once(partial(enable_checkboxes, "Eliminate"), 38)
