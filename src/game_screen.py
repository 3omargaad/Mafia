from kivy.animation import Animation
from kivy.clock import Clock

from kivymd.uix.screen import MDScreen, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from functools import partial
from concurrency import run_concurrent
from game_setup import game
from screen_manager import sm

from random import randint

import narrative
import assets
import audio
import game_stages

# from host import wait


class GameScreen(MDScreen, Screen):
    rye_font = assets.RYE
    roboto_font = assets.ROBOTO
    selected_player = ""

    def on_enter(self):
        game_stages.intro()

    def on_checkbox_active(self, checkbox, value):

        game_screen = self.manager.get_screen('game')
        action = game_screen.ids["action"]
        action.disabled = not value
        print(str(checkbox.parent.text) + str(value))
        global selected_player
        selected_player = game.get_player(checkbox.parent.text)

        match (action.text):
            case "Eliminate":
                if selected_player.role == "Mafia":
                    action.disabled = value
                else:
                    action.disabled = not value
                return
            case "Heal":
                if selected_player.role == "Doctor":
                    action.disabled = value
                else:
                    action.disabled = not value
                return
            case "Investigate":
                if selected_player.role == "Detective":
                    action.disabled = value
                else:
                    action.disabled = not value
                return
        # Ensures Mafia, Doctor & Detective cannot use their role on themselves

    def on_press(self):
        game_screen = self.manager.get_screen('game')
        action = game_screen.ids["action"]
        dialogue = game_screen.ids["dialogue"]

        def display(text, *args):
            dialogue.text = text

        action.disabled = True

        def investigate():
            display(selected_player.name + " is a " + selected_player.role)

        def eliminate():
            selected_player.die()
            game.last_player_eliminated = selected_player
            display(selected_player.name + " has been eliminated!")

        def heal():
            selected_player.heal()
            display(selected_player.name + " has been healed!")

        def vote():
            selected_player.add_vote()
            display(selected_player.name + " has been voted!")

        match (action.text):
            case "Eliminate":
                eliminate()
                return
            case "Heal":
                heal()
                return
            case "Investigate":
                investigate()
                return
            case "Vote":
                vote()
                return

    def on_release(self):
        game_screen = self.manager.get_screen('game')
        action = game_screen.ids["action"]
        dialogue = game_screen.ids["dialogue"]

        def display(text, *args):
            dialogue.text = text

        def countdown(t, clock_t):
            for i in range(t+1):
                Clock.schedule_once(partial(display, "[size=100]" + str(t-i) + "[/size]"), clock_t + i)
                Clock.schedule_once(
                    partial(audio.play_audio, assets.UI_POP),
                    clock_t + i
                )

        def leave(self, *args):
            sm.transition.direction = "up"
            sm.current = 'end'

        def announce(text, audio_file, clock_t):
            Clock.schedule_once(partial(display, text), clock_t)
            if audio_file:
                Clock.schedule_once(partial(audio.play_audio, audio_file), clock_t)

        def disable_checkboxes(*args):
            fadein = Animation(opacity=0)

            for i in range(game.plr_num):
                check = self.ids["check" + str(i+1)]
                check.active = False
                check.state = "normal"
                check.disabled = True
                check.value = False
                fadein.start(check)

        def enable_checkboxes(action_text, *args):
            action.text = action_text
            fadein = Animation(opacity=1)

            for i in range(game.plr_num):
                check = self.ids["check" + str(i+1)]
                check.disabled = False
                fadein.start(check)

        def remove_card(*args):
            fadeout = Animation(opacity=0)

            for i in range(game.plr_num):
                n = str(i+1)
                card = self.ids["name" + n]

                if game.get_player(card.text).is_alive is False:
                    card.disabled = True
                    fadeout.start(card)
        disable_checkboxes()

        def doctor_stage(*args):
            announce(narrative.DOCTOR, assets.DOCTOR, 9)
            game.set_stage("Doctor")
            if game.doctor_player in game.living_players:
                Clock.schedule_once(partial(enable_checkboxes, "Heal"), 12)
            else:
                announce("Doctor is dead.", None, 15)
                if game.include_det:
                    Clock.schedule_once(detective_stage, 15 + randint(1, 7))
                else:
                    Clock.schedule_once(voting, 15 + randint(1, 7))

        def detective_stage(*args):
            announce(narrative.DETECTIVE, assets.DETECTIVE, 9)
            game.set_stage("Detective")
            if game.detective_player in game.living_players:
                Clock.schedule_once(partial(enable_checkboxes, "Investigate"), 12)
            else:
                announce("Detective is dead.", None, 15)
                Clock.schedule_once(voting, 15 + randint(1, 7))

        def reveal_votes(*args):
            fadein = Animation(opacity=1)

            for i in range(game.plr_num):
                n = str(i+1)
                card = self.ids["name" + n]
                vote = self.ids["vote" + n]
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
                card = self.ids["name" + n]
                vote = self.ids["vote" + n]
                if not card.disabled:
                    fadeout.start(vote)

            game.reset_votes()

        def end(*args):
            if game.game_is_over():
                announce(narrative.GAME_OVER, assets.GAME_OVER, 1)
                Clock.schedule_once(leave, 6)
            else:
                announce(narrative.GAME_CONTINUES, assets.GAME_CONTINUES, 1)
                Clock.schedule_once(game_stages.night, 6)

        def voting(*args):
            announce(narrative.MORNING, assets.MORNING, 7)
            game.remove_dead_players()

            if len(game.living_players) == len(game.players):
                announce(narrative.FORTUNATELY, assets.FORTUNATELY, 11)
            else:
                announce(narrative.UNFORTUNATELY, assets.UNFORTUNATELY, 11)
                announce(game.last_player_eliminated.name, None, 15)
                Clock.schedule_once(remove_card, 15)
            announce(narrative.VOTE, assets.VOTE, 18)
            announce(game.living_players[game.vote_count].name + "'s turn to vote.", None, 22)
            enable_checkboxes("Vote")
            game.set_stage("Voting")

        if game.game_stage == "Mafia":
            announce(narrative.MAFIA_SLEEP, assets.MAFIA_SLEEP, 3)
            if game.include_doc:
                doctor_stage()
            elif game.include_det:
                detective_stage()
            else:
                voting()
        elif game.game_stage == "Doctor":
            announce(narrative.DOCTOR_SLEEP, assets.DOCTOR_SLEEP, 3)
            if game.include_det:
                detective_stage()
            else:
                voting()
        elif game.game_stage == "Detective":
            announce(narrative.DETECTIVE_SLEEP, assets.DETECTIVE_SLEEP, 3)
            voting()
        elif game.game_stage == "Voting":
            game.vote_count += 1
            if game.vote_count == len(game.living_players):
                for plr in game.living_players:
                    print(plr.name + " has " + str(plr.votes))
                announce(narrative.REVEAL, assets.REVEAL, 3)
                Clock.schedule_once(reveal_votes, 3)
                announce(narrative.EXECUTION, assets.EXECUTION, 9)

                Clock.schedule_once(game.execute_voted_player, 13)
                announce(game.last_player_eliminated.name, None, 15)
                Clock.schedule_once(game.remove_dead_players, 14)
                Clock.schedule_once(remove_votes, 15)
                Clock.schedule_once(remove_card, 18)
                Clock.schedule_once(end, 19)
            else:
                announce(game.living_players[game.vote_count].name + "'s turn to vote.", None, 3)
                enable_checkboxes("Vote")

    def click(self):
        run_concurrent(audio.play_audio, assets.UI_CLICK)

    def hover(self, widget):
        widget.bold = True

    def quit(self, widget):
        manager = widget.parent.parent
        continue_btn = MDFlatButton(
            text="Continue"
        )

        quit_btn = MDFlatButton(
            text="Quit",
            theme_text_color="Custom",
            text_color=self.theme_cls.primary_color,
        )

        popup = MDDialog(
            title="Quit Game",
            text=narrative.QUIT_MSG,
            auto_dismiss=False,
            buttons=[continue_btn, quit_btn],

        )

        def complete_quit(manager):
            popup.dismiss()
            manager.transition.direction = "down"
            manager.current = 'setup'

        def quit_button_pressed(self):
            complete_quit(manager)
            game.__init__()  # Resets game for the next one
            # for event in list(Clock._events):
            #     try:
            #         event.cancel()
            #     except Exception:
            #         pass
            # Clock._events.clear()

        continue_btn.bind(on_release=popup.dismiss)
        quit_btn.bind(on_release=quit_button_pressed)

        popup.open()
