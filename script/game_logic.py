from time import sleep

from player import Player

import game_setup


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


def wait(t):
    sleep(t)
