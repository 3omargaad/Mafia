from time import sleep
from random import choice

from player import Player

import game_setup


def clear_player_list():
    game_setup.players.clear()
    game_setup.living_players.clear()


def create_player(plr_name):
    plrObject = Player(
        name=plr_name,
        role="Civilian",
        team="Good",
        isAlive=True,
        audioFile=None,
        votes=0
    )

    # Creates player object with default attributes

    game_setup.players.append(plrObject)
    game_setup.living_players.append(plrObject)
    # Adds player object to relevent arrays


def assign_mafia():
    for maf in range(game_setup.maf_num):
        while True:
            mafiaPlayer = choice(game_setup.players)
            if mafiaPlayer.role != "Mafia":
                mafiaPlayer.role = "Mafia"
                mafiaPlayer.team = "Bad"
                break

    # Chooses Player(s) as mafia


def assign_doctor():
    if game_setup.include_doc is True:
        while True:
            doctorPlayer = choice(game_setup.players)
            if doctorPlayer.role != "Mafia":
                doctorPlayer.role = "Doctor"
                break

    # Chooses Player as doctor


def assign_detective():
    if game_setup.include_det is True:
        while True:
            detectivePlayer = choice(game_setup.players)
            if detectivePlayer.role not in ("Mafia", "Doctor"):
                detectivePlayer.role = "Detective"
                break


def assign_roles():
    assign_mafia()
    assign_doctor()
    assign_detective()


def wait(t):
    sleep(t)
