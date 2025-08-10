import app
import game_logic
# Modules


if __name__ == "__main__": 
    game_logic.plrObject = game_logic.player.Player(name="ali", role="Civilian", team="Good", isAlive=True, audioFile=None) #nameAudio)
    game_logic.players.append(game_logic.plrObject)
    game_logic.livingPlayers.append(game_logic.plrObject)

    game_logic.plrObject = game_logic.player.Player(name="belal", role="Doctor", team="Good", isAlive=True, audioFile=None) #nameAudio)
    game_logic.players.append(game_logic.plrObject)
    game_logic.livingPlayers.append(game_logic.plrObject)

    game_logic.plrObject = game_logic.player.Player(name="omar", role="Detective", team="Good", isAlive=True, audioFile=None) #nameAudio)
    game_logic.players.append(game_logic.plrObject)
    game_logic.livingPlayers.append(game_logic.plrObject)

    game_logic.plrObject = game_logic.player.Player(name="hamza", role="Mafia", team="Bad", isAlive=True, audioFile=None) #nameAudio)
    game_logic.players.append(game_logic.plrObject)
    game_logic.livingPlayers.append(game_logic.plrObject)

    game_logic.clear()
    while True: # Main Game Loop
        game_logic.vote()
        game_logic.execution()
        if game_logic.hasGameEnded() == True:
            break
        game_logic.night()        
        game_logic.announcement()
        if game_logic.hasGameEnded() == True:
            break
        game_logic.day()
        
        
        if game_logic.hasGameEnded() == True:
            break

    print("Game ended")
    game_logic.endGame()
