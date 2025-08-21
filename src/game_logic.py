from random import choice
import random
from time import sleep
from pathlib import Path
import os

import audio
import player

wait = lambda t : sleep(t)
clear = lambda : print("\033c", end="")
# Lambda Functions

def countdown(t):
    for i in range(t+1):
        print(t-i)
        audio.playAudio(audio.POP)

def resetVotes():
    for plr in players:
        plr.resetVote()

def revealRoles():
    for plr in players:
        plr.finalReveal()

def printPlayerList(list, exception=None):
    i = 0
    for plr in list:
        i += 1
        if plr.role == exception:
            print(str(i) + ") " + plr.name + " (YOU)")
        else:
            print(str(i) + ") " + plr.name)

def removeDeadPlayers():
    for plr in livingPlayers:
        if plr.isAlive == False:
            deadPlayer = plr

            deadPlayers.append(deadPlayer)
            livingPlayers.remove(deadPlayer)

            if deadPlayer.team == "Bad":
                global badTeamNumber
                badTeamNumber -= 1
            elif deadPlayer.team == "Good":
                global goodTeamNumber
                goodTeamNumber -= 1
            # Assuming 1 player MAX dies each night

def eliminate(playerNumber): 
    livingPlayers[playerNumber-1].die()
    livingPlayers.remove(livingPlayers[playerNumber-1])

def hasGameEnded():
    global winningTeam
    if badTeamNumber == 0:
        winningTeam = "Good"
        return True
    elif goodTeamNumber == badTeamNumber:
        winningTeam = "Bad"
        return True
    else:
        return False
    # Check to see if game ended

# Functions

def intro():
    audio.clearAudioFiles()
    clear()
    print("Welcome to Mafia! I am your host ChadGPT.")
    audio.playAudio(audio.WELCOME)
    
    playerNumber = int(input("How many players are there (minimum 4)? "))
    mafiaNumber = int(input("How many mafia are there (minimum 1)? "))


    global goodTeamNumber 
    goodTeamNumber = playerNumber - mafiaNumber

    global badTeamNumber 
    badTeamNumber = mafiaNumber

    for i in range(playerNumber):
        plrName = input("Enter name of player #" + str(i+1) + " ")
        #nameAudio = audio.textToSpeech(plrName, "plr_" + plrName)
        plrObject = player.Player(name=plrName, role="Civilian", team="Good", isAlive=True, audioFile=None, votes=0)
        # DEFAULT SETTINGS FOR PLAYER OBJECT
        players.append(plrObject)
        livingPlayers.append(plrObject)
        try:
            audio.textToSpeech(plrName, f'plr_{plrName}')
            audio.convertToWav(str(Path(f'assets\\audio\\player_names\\plr_{plrName}.mp3')))
            os.remove(str(Path(f'assets\\audio\\player_names\\plr_{plrName}.mp3')))
        except Exception as error:
            print(error)
        clear()


    clear()

    #Adds every player to the array of players and sets them as civilian by default
    global mafiaPlayer1
    mafiaPlayer1 = choice(players)
    mafiaPlayer1.role = "Mafia"
    mafiaPlayer1.team = "Bad"
    
    global mafiaPlayer2
    mafiaPlayer2 = None

    if mafiaNumber == 2:
        while True:
            mafiaPlayer2 = choice(players)
            if mafiaPlayer2.role != "Mafia":
                break   
        mafiaPlayer2.role = "Mafia"
        mafiaPlayer2.team = "Bad"

    # Chooses Player as mafia

    global doctorPlayer
    while True:
        doctorPlayer = choice(players)
        if doctorPlayer.role != "Mafia":
            break

        
    doctorPlayer.role = "Doctor"

    # Chooses Player as doctor


    global detectivePlayer
    while True:
        detectivePlayer = choice(players)
        if detectivePlayer.role != "Mafia" and detectivePlayer.role != "Doctor":
            break

    detectivePlayer.role = "Detective"

    # Chooses Player as detective

    for i in range(playerNumber):
        wait(1)
        #players[i].sayName()
        input(players[i].name + " Press Enter to check your role ")
        print("You are " + players[i].role)
        wait(1)
        input("Press Enter to clear")
        clear()

    # Shows each player their role seperately

    print("The game has begun!")
    print("You Have 15 seconds to talk before night!")
    audio.playAudio(audio.INTRO)
    wait(1)
    countdown(15)

def night():
    print("The game continues!")
    audio.playAudio(audio.GAMECONTINUES)
    wait(2)
    clear()
    print("The night approached... Everyone falls asleep")
    audio.playAudio(audio.GOODNIGHT)
    wait(5)
    print("While everyone else is fast alseep... the mafia wakes up. The mafia chooses who to eliminate tonight.")
    audio.playAudio(audio.MAFIA)
    wait(1)
    print()
    print("List of players:")
    printPlayerList(livingPlayers, "Mafia")

    print()
    #------------- changes by ali
    try:
        victimNum = int(input("Enter the NUMBER of the player you want to eliminate: "))
        victim = livingPlayers[victimNum-1]
        victim.die()
        print(victim.name + " has been attacked!")
        wait(2)
        print("Mafia go back to sleep")
        audio.playAudio(audio.MAFIA_SLEEP)
        wait(4)
        # MAFIA STAGE
    except Exception as e:
        print(e)
    
    clear()

    print("Soon after... The doctor wakes up. The doctor chooses who to heal tonight.")
    audio.playAudio(audio.DOCTOR)
    wait(1)
    print()
    if doctorPlayer.isAlive or doctorPlayer in livingPlayers:
        print("List of players:")
        printPlayerList(livingPlayers, "Doctor")
        print()
        healedNum = int(input("Enter the NUMBER of the player you want to heal: "))
        healed = livingPlayers[healedNum-1]
        healed.heal()
        print(healed.name + " has been healed!")
    else:
        randWait = random.randint(3, 8)
        print("Doctor is dead :P")
        print("Continuing game in " + str(randWait) + " seconds...")
        wait(randWait)
    wait(2)
    print("Doctor go back to sleep.")
    audio.playAudio(audio.DOCTOR_SLEEP)
    wait(4)
    # DOCTOR STAGE

    clear()

    print("Then... The detective wakes up. The detective chooses who to investigate tonight.")
    audio.playAudio(audio.DETECTIVE)
    wait(1)
    if detectivePlayer.isAlive or detectivePlayer in livingPlayers:
        print()
        print("List of players:")
        printPlayerList(livingPlayers, "Detective")
        print()
        investigatedNum = int(input("Enter the NUMBER of the player you want to investigate: "))
        investigated = livingPlayers[investigatedNum-1]
        print(investigated.name + " has been investigated!")
        investigated.revealTeam()
    else:
        randWait = random.randint(3, 8)
        print("Detective is dead :P")
        print("Continuing game in " + str(randWait) + " seconds...")
        wait(randWait)
    wait(2)
    print("The detective goes back to sleep.")
    audio.playAudio(audio.DETECTIVE_SLEEP)
    wait(4)
    # DETECTIVE STAGE

    # Checks if attacked player is dead
    # If dead then move to deadPlayers array and remove from livingPlayers

    removeDeadPlayers()
    clear()
    

def announcement():
    clear()
    wait(1)
    print("Good morning everyone!")
    audio.playAudio(audio.GOODMORNING)
    wait(2)
    if len(deadPlayers) == 0:
        print("Fortunately, everyone is still alive.")
        audio.playAudio(audio.FORTUNATELY)
    else:
        print("Unfortunately, the following players are no longer alive:")
        audio.playAudio(audio.ANNOUNCEMENT)
        printPlayerList(deadPlayers)
        #for i in deadPlayers:
        #    audio.playAudio(f"assets\\audio\\player_names\\{i.name}_tts.wav")
        wait(4)


def day():
    print("You have 30 seconds to discuss who you think is the Mafia!")
    audio.playAudio(audio.DISCUSS)
    wait(2)
    countdown(30)

def vote():
    print("Times up! Now you must vote on which player to execute!")
    audio.playAudio(audio.VOTE)
    wait(1)

    while True:
        try:
            for i in range(len(livingPlayers)):
                print(livingPlayers[i].name + " choose who to vote.")
                print("List of players:")
                printPlayerList(livingPlayers)
                vote = int(input("Enter the NUMBER of the player you want to vote: "))
                playerVoted = livingPlayers[vote-1]
                playerVoted.addVote()
                wait(2)
                clear()
            break
        except Exception as e:
            resetVotes()
            print(e)
            print("invalid input")
            continue
    
    for plr in livingPlayers:
        #global votes
        votes.append(plr.votes)

    maxVoteVal = max(votes)

    for plr in livingPlayers:
        if plr.votes == maxVoteVal:
            executedPlayers.append(plr)

    

def execution():
    print("It's time to reveal the votes!")
    audio.playAudio(audio.REVEAL)
    wait(3)
    executedVotes = 0
    for i in range(len(livingPlayers)):
        currentPlayer = livingPlayers[i]
        if currentPlayer.votes >= executedVotes:
            executedPlayer = currentPlayer

        print(currentPlayer.name + " has " + str(currentPlayer.votes) + " votes")

    wait(5)
    
    print("It's execution time! The player being executed is...")

    
    executedPlayer = random.choice(executedPlayers)


    audio.playAudio(audio.EXECUTION)

    print(executedPlayer.name)
    wait(2)
    executedPlayer.die()
    executedPlayers.clear()
    resetVotes()
    votes.clear()
    removeDeadPlayers()
    print(executedPlayer.name + " has been executed and is no longer alive!")

    #print(executedPlayer.name)
    #audio.playAudio(f"assets\\audio\\player_names\\{executedPlayer.name}_tts.wav")
    wait(3)
    clear()

def endGame():
    print("The game is over!")
    audio.playAudio(audio.GAMEOVER)
    wait(2)
    print("THE " + str(winningTeam) + " TEAM HAS WON!!!")
    wait(2)
    print("---------------------------------------------------------")
    revealRoles()


# Procedures

badTeamNumber = 0
goodTeamNumber = 0
winningTeam = ""

mafiaPlayer1 = None
mafiaPlayer2 = None
doctorPlayer = None
detectivePlayer = None


# Variables

players = []
livingPlayers = []
deadPlayers = []
votes = []
executedPlayers = []

# Arrays