#import audio_setup
import app
import game_logic
# Modules

if __name__ == "__main__":
    #app.setup() 
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
