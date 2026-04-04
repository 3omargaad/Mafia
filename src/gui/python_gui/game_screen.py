from kivy.clock import Clock

from kivymd.uix.screen import MDScreen, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from concurrency import run_concurrent
from game_setup import game

import narrative
import assets
import audio
import game_stages
import ui_control

# from host import wait


class GameScreen(MDScreen, Screen):
    rye_font = assets.RYE
    roboto_font = assets.ROBOTO
    selected_player = ""

    def on_enter(self):
        ui_control.current_screen = self
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
        ui_control.disable_checkboxes()

        def end(*args):
            if game.game_is_over():
                ui_control.announce(narrative.GAME_OVER, assets.GAME_OVER, 1)
                Clock.schedule_once(ui_control.leave, 6)
            else:
                ui_control.announce(
                    narrative.GAME_CONTINUES, assets.GAME_CONTINUES, 1
                )
                Clock.schedule_once(game_stages.night, 6)

        if game.game_stage == "Mafia":
            ui_control.announce(narrative.MAFIA_SLEEP, assets.MAFIA_SLEEP, 3)
            if game.include_doc:
                game_stages.doctor_stage()
            elif game.include_det:
                game_stages.game_stages.detective_stage()
            else:
                game_stages.voting()
        elif game.game_stage == "Doctor":
            ui_control.announce(narrative.DOCTOR_SLEEP, assets.DOCTOR_SLEEP, 3)
            if game.include_det:
                game_stages.detective_stage()
            else:
                game_stages.voting()
        elif game.game_stage == "Detective":
            ui_control.announce(
                narrative.DETECTIVE_SLEEP, assets.DETECTIVE_SLEEP, 3
            )
            game_stages.voting()
        elif game.game_stage == "Voting":
            game.vote_count += 1
            if game.vote_count == len(game.living_players):
                for plr in game.living_players:
                    print(plr.name + " has " + str(plr.votes))
                ui_control.announce(narrative.REVEAL, assets.REVEAL, 3)
                Clock.schedule_once(ui_control.reveal_votes, 3)
                ui_control.announce(narrative.EXECUTION, assets.EXECUTION, 9)

                Clock.schedule_once(game.execute_voted_player, 13)
                ui_control.announce(game.last_player_eliminated.name, None, 15)
                Clock.schedule_once(game.remove_dead_players, 14)
                Clock.schedule_once(ui_control.remove_votes, 15)
                Clock.schedule_once(ui_control.remove_card, 18)
                Clock.schedule_once(end, 19)
            else:
                ui_control.announce(
                    game.living_players[game.vote_count].name
                    + "'s turn to vote.",
                    None,
                    3
                )
                ui_control.enable_checkboxes("Vote")

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
