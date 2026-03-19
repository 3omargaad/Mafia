from time import sleep
from random import choice

from game_setup import Game

game = Game()


def wait(t):
    sleep(t)


def assign_mafia():
    for maf in range(game.maf_num):
        while True:
            mafia_player = choice(game.players)
            if mafia_player.role != "Mafia":
                mafia_player.role = "Mafia"
                mafia_player.team = "Bad"
                break

    # Chooses Player(s) as mafia


def assign_doctor():
    if game.include_doc is True:
        while True:
            doctor_player = choice(game.players)
            if doctor_player.role != "Mafia":
                doctor_player.role = "Doctor"
                break

    # Chooses Player as doctor


def assign_detective():
    if game.include_det is True:
        while True:
            detective_player = choice(game.players)
            if detective_player.role not in ("Mafia", "Doctor"):
                detective_player.role = "Detective"
                break


def assign_roles():
    assign_mafia()
    assign_doctor()
    assign_detective()

# Host manages the game and performs key actions
# assigns roles
# makes announcements
# countdown
# executes player
