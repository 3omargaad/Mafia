from kivy.animation import Animation
from kivy.clock import Clock

from functools import partial

from screen_manager import sm
from game_setup import game

import narrative
import assets
import audio
import host


def intro():
    player_screen = sm.get_screen('player')
    game_screen = sm.get_screen('game')
    dialogue = game_screen.ids["dialogue"]
    action = game_screen.ids["action"]

    def display(text, *args):
        dialogue.text = text

    def enable_checkboxes(action_text, *args):
        action.text = action_text
        fadein = Animation(opacity=1)
        for i in range(host.game.plr_num):
            check = game_screen.ids["check" + str(i+1)]
            check.disabled = False
            fadein.start(check)

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

    def announce(text, audio_file, clock_t):
        Clock.schedule_once(partial(display, text), clock_t)
        Clock.schedule_once(partial(audio.play_audio, audio_file), clock_t)

    announce(narrative.WELCOME, assets.WELCOME, 3)
    announce(narrative.INTRO, assets.INTRO, 8)
    countdown(15, 13)
    announce(narrative.NIGHT, assets.NIGHT, 29)
    announce(narrative.MAFIA, assets.MAFIA, 35)
    game.set_stage("Mafia")
    Clock.schedule_once(partial(enable_checkboxes, "Eliminate"), 38)

def stage():
    game_screen = self.manager.get_screen('game')
    action = game_screen.ids["action"]
    dialogue = game_screen.ids["dialogue"]

    def display(text, *args):
        dialogue.text = text

    def countdown(t, clock_t):
        for i in range(t+1):
            Clock.schedule_once(partial(display, "[size=50]" + str(t-i) + "[/size]"), clock_t + i)
            Clock.schedule_once(
                partial(audio.play_audio, assets.UI_POP),
                clock_t + i
            )

    def announce(text, audio_file, clock_t):
        Clock.schedule_once(partial(display, text), clock_t)
        if audio_file:
            Clock.schedule_once(partial(audio.play_audio, audio_file), clock_t)

    def disable_checkboxes(*args):
        fadein = Animation(opacity=0)
        for i in range(host.game.plr_num):
            check = self.ids["check" + str(i+1)]
            check.active = False
            check.state = "normal"
            check.disabled = True
            check.value = False
            fadein.start(check)

    def enable_checkboxes(action_text, *args):
        action.text = action_text
        fadein = Animation(opacity=1)
        for i in range(host.game.plr_num):
            check = self.ids["check" + str(i+1)]
            check.disabled = False
            fadein.start(check)

    def remove_card(*args):
        fadeout = Animation(opacity=0)
        for i in range(host.game.plr_num):
            n = str(i+1)
            card = self.ids["name" + n]
            if game.get_player(card.text).is_alive is False:
                card.disabled = True
                fadeout.start(card)
                game_screen.remove_widget(card)

    disable_checkboxes()
    if game.game_stage == "Mafia":
        announce(narrative.MAFIA_SLEEP, assets.MAFIA_SLEEP, 3)
        announce(narrative.DOCTOR, assets.DOCTOR, 9)
        game.set_stage("Doctor")
        Clock.schedule_once(partial(enable_checkboxes, "Heal"), 12)
    elif game.game_stage == "Doctor":
        announce(narrative.DOCTOR_SLEEP, assets.DOCTOR_SLEEP, 3)
        announce(narrative.DETECTIVE, assets.DETECTIVE, 9)
        game.set_stage("Detective")
        Clock.schedule_once(partial(enable_checkboxes, "Investigate"), 12)
    elif game.game_stage == "Detective":
        announce(narrative.DETECTIVE_SLEEP, assets.DETECTIVE_SLEEP, 3)
        announce(narrative.MORNING, assets.MORNING, 7)
        game.remove_dead_players()
        if len(game.living_players) == len(game.players):
            announce(narrative.FORTUNATELY, assets.FORTUNATELY, 11)
        else:
            announce(narrative.UNFORTUNATELY, assets.UNFORTUNATELY, 11)
            dead_list = "| "
            for plr in game.dead_players:
                dead_list += plr.name + " | "
            announce(dead_list, None, 15)
            Clock.schedule_once(remove_card, 15)
        announce(narrative.VOTE, assets.VOTE, 18)
        announce(game.living_players[game.vote_count].name + "'s turn to vote.", None, 22)
        enable_checkboxes("Vote")
        game.set_stage("Voting")
    elif game.game_stage == "Voting":
        game.vote_count += 1
        if game.vote_count == len(game.living_players):
            for plr in game.living_players:
                print(plr.name + " has " + str(plr.votes))
        else:
            announce(game.living_players[game.vote_count].name + "'s turn to vote.", None, 3)
            enable_checkboxes("Vote")