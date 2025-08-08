from random import choice
from time import sleep

import audio
import player

def mostFrequent(List):
    return max(set(List),key=List.count)

def wait(t):
    sleep(t)


def countdown(t):
    for i in range(t+1):
        print(t-i)
        audio.playAudio(audio.POP)


def clear():
    print("\033c", end="")


def printPlayerList(list, exception=None):
    for i in range(len(list)):
        if list[i].role == exception:
            print(str(i+1) + ") " + list[i].name + " (YOU)")
        else:
            print(str(i+1) + ") " + list[i].name)


def checkIfDead():
    for i in range(livingPlayers):
        if livingPlayers[i].isAlive == False:
            return livingPlayers[i].name
            # Assuming 1 player MAX dies each night


def eliminate(playerNumber): 
    livingPlayers[playerNumber-1].die()
    livingPlayers.remove(livingPlayers[playerNumber-1])

# Functions

def hasGameEnded():
    if badTeamNumber == 0:
        winningTeam = "Good"
        return True
    elif goodTeamNumber == badTeamNumber:
        winningTeam = "Bad"
        return True
    else:
        return False
    # Check to see if game ended

def intro():
    clear()
    print("Welcome to Mafia! I am your host ChadGPT.")
    audio.playAudio(audio.WELCOME)
    
    
    playerNumber = int(input("How many players are there (minimum 4)? "))
    global goodTeamNumber 
    goodTeamNumber = playerNumber - 1

    global badTeamNumber 
    badTeamNumber = 1

    for i in range(playerNumber):
        plrName = input("Enter name of player #" + str(i+1) + " ")
        #nameAudio = audio.textToSpeech(plrName, "plr_" + plrName)
        plrObject = player.Player(name=plrName, role="Civilian", team="Good", isAlive=True, audioFile=None) #nameAudio)
        players.append(plrObject)
        livingPlayers.append(plrObject)
        clear()


    clear()

    #Adds every player to the array of players and sets them as civilian by default

    mafiaPlayer = choice(players)
    mafiaPlayer.role = "Mafia"
    mafiaPlayer.team = "Bad"

    # Chooses Player as mafia

    doctorPlayer = None
    while True:
        doctorPlayer = choice(players)
        if doctorPlayer.role != "Mafia":
            break

        
    doctorPlayer.role = "Doctor"

    # Chooses Player as doctor


    detectivePlayer = None
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
        wait(1)
        print("You are " + players[i].role)
        wait(1)
        input("Press Enter to clear")
        wait(1)
        clear()

    # Shows each player their role seperately

    print("The game has begun!")
    print("You Have 15 seconds to talk before night!")
    audio.playAudio(audio.INTRO)
    wait(3)
    #countdown(15)

def night():
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
        print(victim.name + " had been attacked!")
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
    print("List of players:")
    printPlayerList(livingPlayers, "Doctor")
    print()
    healedNum = int(input("Enter the NUMBER of the player you want to heal: "))
    healed = livingPlayers[healedNum-1]
    healed.heal()
    print(healed.name + " had been healed!")
    wait(2)
    print("Doctor go back to sleep.")
    audio.playAudio(audio.DOCTOR_SLEEP)
    wait(4)
    # DOCTOR STAGE

    clear()

    print("Then... The detective wakes up. The detective chooses who to investigate tonight.")
    audio.playAudio(audio.DETECTIVE)
    wait(1)
    print()
    print("List of players:")
    printPlayerList(livingPlayers, "Detective")

    print()
    investigatedNum = int(input("Enter the NUMBER of the player you want to investigate: "))
    investigated = livingPlayers[investigatedNum-1]
    print(investigated.name + " had been investigated!")
    investigated.reveal()
    wait(2)
    print("The detective goes back to sleep.")
    audio.playAudio(audio.DETECTIVE_SLEEP)
    wait(4)
    # DETECTIVE STAGE
    movePlayer = None
    for i in range(len(livingPlayers)):
        currentPlayer = livingPlayers[i]
        if currentPlayer.isAlive == False:
            movePlayer = currentPlayer

    if movePlayer != None:
        livingPlayers.remove(movePlayer)
        deadPlayers.append(movePlayer)
        
        if movePlayer.team == "Bad":
            global badTeamNumber
            badTeamNumber -= 1
        elif movePlayer.team == "Good":
            global goodTeamNumber
            goodTeamNumber -= 1
    
    # Moves dead player to correct list
    clear()
    

def announcement():
    wait(1)
    audio.playAudio(audio.GOODMORNING)
    print("Good morning everyone!")
    wait(2)
    print("Unfortunately, the following players are no longer alive:")
    audio.playAudio(audio.ANNOUNCEMENT)
    printPlayerList(deadPlayers)
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
    try:
        for i in range(len(livingPlayers)):
            print(livingPlayers[i].name + " choose who to vote.")
            print("List of players:")
            printPlayerList(livingPlayers)
            votedNum = int(input("Enter the NUMBER of the player you want to vote: "))
            voted.append(votedNum)
            wait(2)
            clear()
    except Exception as e:
        print(e)
    

def execution():
    print("It's execution time! The player being executed is...")
    audio.playAudio(audio.EXECUTION)
    print(mostFrequent(voted.name))
    wait(5)

def endGame():
    print("THE " + str(winningTeam) + " TEAM HAS WON!!!")

# Procedures

badTeamNumber = 0
goodTeamNumber = 0
winningTeam = ""
# Variables


players = []
livingPlayers = []
deadPlayers = []
voted = []

# Arrays