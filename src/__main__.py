import gui
import game_logic
# Modules

def main():
    gui.setup()
    game_logic.intro()
    while True: # Main Game Loop
        game_logic.night()
        game_logic.announcement()
        if game_logic.hasGameEnded() == True:
            break
        game_logic.day()
        game_logic.vote()
        game_logic.execution()
        if game_logic.hasGameEnded() == True:
            break
        
    game_logic.endGame()

if __name__ == "__main__":
    main()