import gui
import game_stages
# Modules


def main():
    gui.setup()
    game_stages.intro()
    while True:  # Main Game Loop
        game_stages.night()
        game_stages.announcement()
        if game_stages.hasGameEnded():
            break
        game_stages.day()
        game_stages.vote()
        game_stages.execution()
        if game_stages.hasGameEnded():
            break
    game_stages.endGame()


if __name__ == "__main__":
    main()
