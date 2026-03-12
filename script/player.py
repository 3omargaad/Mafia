class Player:
    def __init__(self, name, role, team, isAlive, audioFile, votes):
        self.name = name
        self.role = role
        self.team = team
        self.isAlive = isAlive
        self.audioFile = audioFile
        self.votes = votes
    # Initialises Default Attributes such as name, role, team, isAlive etc.

    def die(self):
        self.isAlive = False
    # Eliminates the player

    def heal(self):
        if self.isAlive is False:
            self.isAlive = True
    # Saves the player who has been aliminates

    def revealTeam(self):
        print(self.name + " is " + self.team)
    # Reveals the team which the player is in

    def revealRole(self):
        print(self.name + " is " + self.role)
    # Reveals the role which the player has (not in use)

    def finalReveal(self):
        status = "Dead"
        if self.isAlive:
            status = "Alive"

        print(self.name + " is " + self.role + " (" + status + ")")

    def addVote(self):
        self.votes += 1
    # Adds a vote onto the player

    def resetVote(self):
        self.votes = 0
    # Removes all the player's votes

    # def sayName(self):
    #     newAudio = audio.convertToWav(inputFile=self.audioFile,
    #                   newName=self.name + ".wav")
    #     audio.playAudio(audio.newAudio)

# Player Object

# plrObject = player.Player(
#             name=plrName,
#             role="Civilian",
#             team="Good",
#             isAlive=True,
#             audioFile=None,
#             votes=0
# )
# DEFAULT SETTINGS FOR PLAYEROBJECT
